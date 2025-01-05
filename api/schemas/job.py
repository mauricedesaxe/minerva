from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JobBase(BaseModel):
    """Base job schema with common attributes."""
    bucket: str
    key: str

class JobCreate(JobBase):
    """Schema for creating a new job."""
    force_reload: bool = False

class JobUpdate(BaseModel):
    """Schema for updating a job."""
    status: Optional[str] = None
    completed_at: Optional[datetime] = None
    chunks_processed: Optional[int] = None
    error: Optional[str] = None

class JobResponse(JobBase):
    """Schema for job responses."""
    job_id: str
    status: str
    created_at: datetime
    completed_at: Optional[datetime] = None
    chunks_processed: Optional[int] = None
    error: Optional[str] = None

    class Config:
        from_attributes = True 