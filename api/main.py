from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security.api_key import APIKeyHeader
import os
from dotenv import load_dotenv
from typing import Annotated
import sys
from pathlib import Path

# Add parent directory to path so we can import from modules
sys.path.append(str(Path(__file__).parent.parent))
from modules.logger import setup_logger
from api.routers import documents, search

# Load environment variables
load_dotenv()

# Initialize logger
logger = setup_logger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Minerva API",
    description="Document processing and semantic search API",
    version="1.0.0"
)

# API Key security
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def verify_api_key(api_key: Annotated[str | None, Depends(api_key_header)]):
    if api_key != os.getenv("API_KEY"):
        raise HTTPException(
            status_code=401,
            detail={"error": {"code": "auth_failed", "message": "Invalid API key"}}
        )
    return api_key

# Global error handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": "server_error",
                "message": "An unexpected error occurred"
            }
        }
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