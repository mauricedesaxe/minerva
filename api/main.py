from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.security.api_key import APIKeyHeader
import os
from typing import Annotated
import sys
from pathlib import Path
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
from sqlalchemy.exc import SQLAlchemyError
from fastapi.middleware.cors import CORSMiddleware
import botocore.exceptions
from modules.env import API_KEY

# Add parent directory to path so we can import from modules
sys.path.append(str(Path(__file__).parent.parent))
from modules.logger import setup_logger, logger
from api.routers import documents, search
from api.schemas.error import ErrorCode, ErrorResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Set up logging
    if app.debug:
        os.environ["LOG_LEVEL"] = "DEBUG"
    
    # Reinitialize logger
    global logger
    logger = setup_logger("minerva")
    logger.debug("Application starting up in debug mode")
    
    yield  # Server is running and handling requests
    
    # Shutdown: Clean up resources if needed
    logger.info("Application shutting down")

# Initialize FastAPI app with lifespan and custom docs
app = FastAPI(
    title="Minerva API",
    description="Document processing and semantic search API",
    version="1.0.0",
    lifespan=lifespan,
    docs_url=None  # Disable default docs
)

# TODO: Restrict to specific origins (maybe make it configurable)
# Allow any origin for now
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="api/static"), name="static")

# Custom docs with dark theme
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    swagger_ui = get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui.css",
        swagger_favicon_url="https://fastapi.tiangolo.com/img/favicon.png",
    )
    body = swagger_ui.body.decode()
    css_url = app.url_path_for("static", path="swagger_dark_theme.css")
    body = body.replace(
        "</head>",
        f'<link rel="stylesheet" href="{css_url}">\n</head>'
    )
    return HTMLResponse(body)

# API Key security
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def verify_api_key(api_key: Annotated[str | None, Depends(api_key_header)]):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail={
                "error": {
                    "code": ErrorCode.AUTH_FAILED,
                    "message": "Invalid API key"
                }
            }
        )
    return api_key

# Global error handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    # If detail is already formatted as our error response, use it directly
    if isinstance(exc.detail, dict) and "error" in exc.detail:
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.detail
        )
    
    # Otherwise, format it according to our schema
    error_code = ErrorCode.INVALID_REQUEST
    if exc.status_code == 401:
        error_code = ErrorCode.AUTH_FAILED
    elif exc.status_code == 404:
        error_code = ErrorCode.NOT_FOUND
    elif exc.status_code == 500:
        error_code = ErrorCode.SERVER_ERROR
    
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            error={
                "code": error_code,
                "message": str(exc.detail)
            }
        ).model_dump()
    )

@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    logger.error(f"Database error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error={
                "code": ErrorCode.SERVER_ERROR,
                "message": "Database error occurred"
            }
        ).model_dump()
    )

@app.exception_handler(botocore.exceptions.ClientError)
async def s3_client_error_handler(request: Request, exc: botocore.exceptions.ClientError):
    logger.error(f"S3 error occurred: {str(exc)}")
    error_code_from_s3 = exc.response.get("Error", {}).get("Code", "")
    if error_code_from_s3 == "NoSuchKey":
        return JSONResponse(
            status_code=404,
            content=ErrorResponse(
                error={
                    "code": ErrorCode.NOT_FOUND,
                    "message": "Requested file not found in S3 bucket."
                }
            ).model_dump()
        )
    if error_code_from_s3 == "AccessDenied":
        return JSONResponse(
            status_code=403,
            content=ErrorResponse(
                error={
                    "code": ErrorCode.AUTH_FAILED,
                    "message": "Access denied to S3 bucket."
                }
            ).model_dump()
        )
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error={
                "code": ErrorCode.SERVER_ERROR,
                "message": "A general S3 error occurred."
            }
        ).model_dump()
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error={
                "code": ErrorCode.SERVER_ERROR,
                "message": "An unexpected error occurred"
            }
        ).model_dump()
    )

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Apply API key middleware to all routes
app.dependency_overrides[api_key_header] = verify_api_key

# Include routers
app.include_router(documents.router)
app.include_router(search.router) 