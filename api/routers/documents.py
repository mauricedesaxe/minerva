from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_db, AsyncSessionLocal
from ..repositories.job_repository import JobRepository
from ..schemas.job import JobCreate, JobResponse

router = APIRouter(prefix="/api/v1/documents", tags=["documents"])

class ProcessRequest(BaseModel):
    bucket: str
    key: str
    force_reload: bool = False

class FileInfo(BaseModel):
    bucket: str
    key: str

async def process_document_task(job_id: str, bucket: str, key: str):
    # Create a new database session specifically for this background task
    async with AsyncSessionLocal() as db:
        # TODO: Implement actual document processing using process_docs.process_markdown_file()
        # For now, just simulate processing
        repo = JobRepository(db)
        try:
            await repo.complete_job(job_id, chunks_processed=0)
            await db.commit()
        except Exception as e:
            await repo.fail_job(job_id, str(e))
            await db.commit()

@router.post("/process", response_model=JobResponse)
async def process_document(
    request: ProcessRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    repo = JobRepository(db)
    
    job = await repo.create(JobCreate(
        bucket=request.bucket,
        key=request.key,
        force_reload=request.force_reload
    ))
    
    background_tasks.add_task(
        process_document_task,
        job.job_id,
        request.bucket,
        request.key
    )
    
    return JobResponse(
        job_id=job.job_id,
        status=job.status,
        created_at=job.created_at,
        completed_at=job.completed_at,
        bucket=job.bucket,
        key=job.file_key,
        file_info=FileInfo(bucket=job.bucket, key=job.file_key)
    )

@router.get("/jobs/{job_id}", response_model=JobResponse)
async def get_job_status(
    job_id: str,
    db: AsyncSession = Depends(get_db)
):
    repo = JobRepository(db)
    job = await repo.get(job_id)
    
    if job is None:
        raise HTTPException(
            status_code=404,
            detail={
                "error": {
                    "code": "not_found",
                    "message": f"Job {job_id} not found"
                }
            }
        )
    
    return JobResponse(
        job_id=job.job_id,
        status=job.status,
        created_at=job.created_at,
        completed_at=job.completed_at,
        bucket=job.bucket,
        key=job.file_key,
        chunks_processed=job.chunks_processed,
        error=job.error
    ) 