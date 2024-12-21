from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from .config import get_config

def create_db_engine() -> Engine:
    """Create SQLAlchemy engine from config."""
    config = get_config()
    return create_engine(
        config.postgres_dsn,
        pool_pre_ping=True,  # Enable connection health checks
        pool_size=5,         # Set reasonable pool size
        max_overflow=10      # Allow some overflow connections
    )

# Create global engine instance
engine = create_db_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db() -> Generator[Session, None, None]:
    """Get database session with context management."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 