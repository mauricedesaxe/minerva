from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from openai import OpenAI
import os
from dotenv import load_dotenv

from ..database import get_db, AsyncSessionLocal
from ..repositories.job_repository import JobRepository
from ..schemas.job import JobCreate, JobResponse
from modules.s3_connection import get_s3_client, check_bucket_exists, get_file_content
from modules.splitter import split_text
from modules.collection_manager import init_collection, check_document_exists
from modules.logger import logger

# Load environment variables and initialize clients
load_dotenv()
openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
s3_client = get_s3_client()
chroma_client, collection = init_collection()

router = APIRouter(prefix="/api/v1/documents", tags=["documents"])

class ProcessRequest(BaseModel):
    bucket: str
    key: str
    force_reload: bool = False

class FileInfo(BaseModel):
    bucket: str
    key: str

def get_embeddings(texts: list[str]) -> list[list[float]]:
    """Get embeddings from OpenAI."""
    try:
        logger.info("Getting embeddings for %d chunks", len(texts))
        response = openai_client.embeddings.create(
            model="text-embedding-3-large",
            input=texts
        )
        logger.debug("Successfully got embeddings")
        return [data.embedding for data in response.data]
    except Exception as e:
        logger.error("Failed to get embeddings: %s", str(e))
        raise

async def process_document_task(job_id: str, bucket: str, key: str, force_reload: bool = False):
    # Create a new database session specifically for this background task
    async with AsyncSessionLocal() as db:
        repo = JobRepository(db)
        try:
            # Validate bucket exists
            if not check_bucket_exists(bucket, s3_client):
                raise Exception(f"Bucket '{bucket}' not found or not accessible")

            # Check if already processed
            doc_ids = [f"{key}_{i}" for i in range(1000)]  # Check reasonable range
            existing_docs = [id for id in doc_ids if check_document_exists(collection, id)]
            logger.debug(f"Found {len(existing_docs)} documents")
            
            if existing_docs and not force_reload:
                logger.info("File %s already processed (%d chunks)", key, len(existing_docs))
                await repo.complete_job(job_id, chunks_processed=len(existing_docs))
                await db.commit()
                return

            # Get content from S3
            logger.debug("Fetching content from S3")
            content = get_file_content(bucket, key, s3_client)
            
            # Split into chunks
            logger.debug("Splitting content into chunks")
            chunks = split_text(content)
            logger.info("Split into %d chunks", len(chunks))
            
            # Get embeddings
            embeddings = get_embeddings(chunks)
            
            # Delete old chunks if reloading
            if existing_docs and force_reload:
                logger.info("Removing old chunks before reload")
                collection.delete(ids=existing_docs)
            
            # Store in ChromaDB
            logger.debug("Storing chunks in ChromaDB")
            collection.add(
                documents=chunks,
                embeddings=embeddings,
                ids=[f"{key}_{i}" for i in range(len(chunks))],
                metadatas=[{"source": key, "chunk": i} for i in range(len(chunks))]
            )
            
            logger.info("Successfully processed file %s", key)
            await repo.complete_job(job_id, chunks_processed=len(chunks))
            await db.commit()

        except Exception as e:
            error_msg = f"Failed to process file {key}: {str(e)}"
            logger.error(error_msg)
            await repo.fail_job(job_id, error_msg)
            await db.commit()

@router.post("/process", response_model=JobResponse)
async def process_document(
    request: ProcessRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    if not request.key.lower().endswith('.md'):
        raise HTTPException(
            status_code=400,
            detail={
                "error": {
                    "code": "invalid_request",
                    "message": "Only markdown (.md) files are supported"
                }
            }
        )
    
    if not check_bucket_exists(request.bucket, s3_client):
        raise HTTPException(
            status_code=400,
            detail={
                "error": {
                    "code": "invalid_request",
                    "message": f"Bucket '{request.bucket}' not found or not accessible"
                }
            }
        )

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
        request.key,
        request.force_reload
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