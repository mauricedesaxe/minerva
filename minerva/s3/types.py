from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional

@dataclass
class S3File:
    """Data class representing a file from S3 with its metadata."""
    bytes: bytes
    content_type: str
    size: int
    last_modified: datetime
    metadata: Dict[str, str]
    etag: str
    version_id: Optional[str] = None 