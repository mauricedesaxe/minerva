from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from openai import OpenAI
from datetime import datetime
from ..database import get_db, AsyncSessionLocal
from ..repositories.job_repository import JobRepository
from ..schemas.job import JobCreate, JobResponse
from ..schemas.error import ErrorCode
from modules.s3_connection import get_s3_client, check_bucket_exists, get_file_content
from modules.splitter import split_text
from modules.collection_manager import init_collection, check_document_exists
from modules.logger import logger
from modules.env import OPENAI_API_KEY
from modules.embeddings import get_document_chunk_embeddings
import time
from typing import List
openai_client = OpenAI(api_key=OPENAI_API_KEY)
s3_client = get_s3_client()
chroma_client, collection = init_collection()

router = APIRouter(prefix="/api/v1/documents", tags=["documents"])

class ProcessRequest(BaseModel):
    bucket: str
    key: str
    force_reload: bool = False

    class Config:
        json_schema_extra = {
            "example": {
                "bucket": "spacestation-labs-companion",
                "key": "the_falcon.md",
                "force_reload": True
            }
        }

class FileInfo(BaseModel):
    bucket: str
    key: str

class DocumentStats(BaseModel):
    document_id: str
    source: str
    chunk_count: int
    embedded_at: datetime
    
def log_performance(duration: float, context: str = "", failed: bool = False):
    """Log performance based on duration thresholds.
    
    Args:
        duration: Time in seconds
        context: Additional context for the log message
        failed: Whether this was a failed task
    """
    status = "failed" if failed else "successful"
    context = f" for {context}" if context else ""
    
    if duration > 1:
        logger.warning(f"PERF: ⚠️ Task {status}{context} - time concerning ({duration:.2f}s)")
    else:
        logger.info(f"PERF: Task {status}{context} - normal time ({duration:.2f}s)")

async def process_document_task(job_id: str, bucket: str, key: str, force_reload: bool = False):
    task_start = time.time()
    # Create a new database session specifically for this background task
    async with AsyncSessionLocal() as db:
        repo = JobRepository(db)
        try:
            # Validate bucket exists
            if not check_bucket_exists(bucket, s3_client):
                raise Exception(f"Bucket '{bucket}' not found or not accessible")

            # Check if already processed
            check_start = time.time()
            doc_ids = [f"{key}_{i}" for i in range(1000)]
            existing_docs = [id for id in doc_ids if check_document_exists(collection, id)]
            logger.debug(f"Found {len(existing_docs)} documents")
            log_performance(time.time() - check_start, "document existence check")
            
            if existing_docs and not force_reload:
                logger.info("File %s already processed (%d chunks)", key, len(existing_docs))
                await repo.complete_job(job_id, chunks_processed=len(existing_docs))
                await db.commit()
                log_performance(time.time() - task_start, "already processed file")
                return

            # Get content from S3
            s3_start = time.time()
            logger.debug("Fetching content from S3")
            content = get_file_content(bucket, key, s3_client)
            logger.debug("Content sample (first 500 chars): %s", content[:500])
            logger.debug("Content length: %d bytes", len(content))
            log_performance(time.time() - s3_start, "S3 content fetch")
            
            # Split into chunks
            split_start = time.time()
            logger.debug("Splitting content into chunks")
            chunks = split_text(content)
            logger.info("Split into %d chunks", len(chunks))
            log_performance(time.time() - split_start, "text splitting")
            
            # Chunk validation
            validation_start = time.time()
            empty_chunks = [i for i, chunk in enumerate(chunks) if not chunk.strip()]
            if empty_chunks:
                logger.error("Found %d empty chunks at indices: %s", 
                            len(empty_chunks), 
                            empty_chunks[:10])
                raise ValueError(f"Document contains {len(empty_chunks)} empty chunks")
            log_performance(time.time() - validation_start, "chunk validation")

            # Get embeddings
            embedding_start = time.time()
            embeddings = get_document_chunk_embeddings(chunks)
            log_performance(time.time() - embedding_start, "embedding generation")
            
            # Delete old chunks if reloading
            if existing_docs and force_reload:
                delete_start = time.time()
                logger.info("Removing old chunks before reload")
                collection.delete(ids=existing_docs)
                log_performance(time.time() - delete_start, "deleting old chunks")
            
            # Store in ChromaDB
            store_start = time.time()
            logger.debug("Storing chunks in ChromaDB")
            collection.add(
                documents=chunks,
                embeddings=embeddings,
                ids=[f"{key}_{i}" for i in range(len(chunks))],
                metadatas=[{"source": key, "chunk": i, "embedded_at": datetime.utcnow().isoformat()} for i in range(len(chunks))]
            )
            log_performance(time.time() - store_start, "ChromaDB storage")
            
            logger.info("Successfully processed file %s", key)
            await repo.complete_job(job_id, chunks_processed=len(chunks))
            await db.commit()
            log_performance(time.time() - task_start, f"processing {key}")

        except Exception as e:
            error_msg = f"Failed to process file {key}: {str(e)}"
            logger.error(error_msg)
            await repo.fail_job(job_id, error_msg)
            await db.commit()
            log_performance(time.time() - task_start, f"processing {key}", failed=True)

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
                    "code": ErrorCode.INVALID_REQUEST,
                    "message": "Only markdown (.md) files are supported"
                }
            }
        )
    
    if not check_bucket_exists(request.bucket, s3_client):
        raise HTTPException(
            status_code=400,
            detail={
                "error": {
                    "code": ErrorCode.INVALID_REQUEST,
                    "message": f"Bucket '{request.bucket}' not found or not accessible"
                }
            }
        )
    
    content = get_file_content(request.bucket, request.key, s3_client)
    size_threshold = 5 * 1024 * 1024 # 5MB
    if len(content) > size_threshold:
        raise HTTPException(
            status_code=400,
            detail={
                "error": {
                    "code": ErrorCode.INVALID_REQUEST,
                    "message": "File size exceeds 5MB"
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
                    "code": ErrorCode.NOT_FOUND,
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

@router.get("/jobs", response_model=list[JobResponse])
async def list_jobs(
    db: AsyncSession = Depends(get_db)
):
    repo = JobRepository(db)
    jobs = await repo.list_all()
    
    return [
        JobResponse(
            job_id=job.job_id,
            status=job.status, 
            created_at=job.created_at,
            completed_at=job.completed_at,
            bucket=job.bucket,
            key=job.file_key,
            chunks_processed=job.chunks_processed,
            error=job.error
        )
        for job in jobs
    ]

@router.get("/stats", response_model=List[DocumentStats])
async def get_document_stats():
    """Get statistics about processed documents in the collection."""
    try:
        # Get all documents from collection
        results = collection.get(
            include=['metadatas']
        )
        
        if not results or not results['metadatas']:
            return []
        
        # Group chunks by source document
        doc_stats = {}
        for metadata in results['metadatas']:
            source = metadata['source']
            if source not in doc_stats:
                doc_stats[source] = {
                    'document_id': source,
                    'source': source,
                    'chunk_count': 0,
                    'embedded_at': datetime.fromisoformat(metadata['embedded_at'])
                }
            doc_stats[source]['chunk_count'] += 1
        
        return list(doc_stats.values())
        
    except Exception as e:
        logger.error(f"Failed to get document stats: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail={
                "error": {
                    "code": ErrorCode.INTERNAL_ERROR,
                    "message": "Failed to retrieve document statistics"
                }
            }
        )
