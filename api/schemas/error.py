from pydantic import BaseModel
from enum import Enum

class ErrorCode(str, Enum):
    AUTH_FAILED = "auth_failed"
    INVALID_REQUEST = "invalid_request"
    PROCESSING_ERROR = "processing_error"
    NOT_FOUND = "not_found"
    SERVER_ERROR = "server_error"

class ErrorResponse(BaseModel):
    error: dict[str, str] = {
        "code": str,  # from ErrorCode enum
        "message": str
    }

    class Config:
        json_schema_extra = {
            "example": {
                "error": {
                    "code": "invalid_request",
                    "message": "Only markdown (.md) files are supported"
                }
            }
        } 