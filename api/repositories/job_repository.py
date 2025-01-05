from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
import uuid

from ..models import Job
from ..schemas.job import JobCreate, JobUpdate

class JobRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, job_data: JobCreate) -> Job:
        """Create a new job."""
        job = Job(
            job_id=str(uuid.uuid4()),
            status="processing",
            bucket=job_data.bucket,
            file_key=job_data.key,
            created_at=datetime.utcnow()
        )
        self.session.add(job)
        await self.session.flush()
        return job

    async def get(self, job_id: str) -> Job | None:
        """Get a job by ID."""
        query = select(Job).where(Job.job_id == job_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def update(self, job_id: str, job_data: JobUpdate) -> Job | None:
        """Update a job."""
        job = await self.get(job_id)
        if job is None:
            return None

        for key, value in job_data.model_dump(exclude_unset=True).items():
            setattr(job, key, value)

        await self.session.flush()
        return job

    async def complete_job(self, job_id: str, chunks_processed: int) -> Job | None:
        """Mark a job as completed."""
        return await self.update(
            job_id,
            JobUpdate(
                status="completed",
                completed_at=datetime.utcnow(),
                chunks_processed=chunks_processed
            )
        )

    async def fail_job(self, job_id: str, error: str) -> Job | None:
        """Mark a job as failed."""
        return await self.update(
            job_id,
            JobUpdate(
                status="failed",
                completed_at=datetime.utcnow(),
                error=error
            )
        ) 