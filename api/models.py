from sqlalchemy import Column, String, Integer, DateTime, func
from .database import Base

class Job(Base):
    __tablename__ = "jobs"

    job_id = Column(String, primary_key=True)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    completed_at = Column(DateTime, nullable=True)
    bucket = Column(String, nullable=False)
    file_key = Column(String, nullable=False)
    chunks_processed = Column(Integer, nullable=True)
    error = Column(String, nullable=True) 