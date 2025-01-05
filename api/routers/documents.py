from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

router = APIRouter(prefix="/api/v1/documents", tags=["documents"])

class ProcessRequest(BaseModel):
    bucket: str
    key: str
    force_reload: bool = False

class FileInfo(BaseModel):
    bucket: str
    key: str

class JobResponse(BaseModel):
    job_id: str
    status: str
    created_at: datetime
    completed_at: Optional[datetime] = None
    file_info: FileInfo
    result: Optional[dict] = None

@router.post("/process", response_model=JobResponse)
async def process_document(request: ProcessRequest):
    # TODO: Implement document processing
    raise HTTPException(
        status_code=501,
        detail={
            "error": {
                "code": "not_implemented",
                "message": "Document processing not yet implemented"
            }
        }
    )

@router.get("/jobs/{job_id}", response_model=JobResponse)
async def get_job_status(job_id: str):
    # TODO: Implement job status retrieval
    raise HTTPException(
        status_code=501,
        detail={
            "error": {
                "code": "not_implemented",
                "message": "Job status retrieval not yet implemented"
            }
        }
    ) 