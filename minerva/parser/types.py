from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional

@dataclass
class ParsedDocument:
    """Data class representing a parsed document with its metadata."""
    text: str
    content_type: str
    size: int
    parsed_at: datetime
    metadata: Dict[str, str]
    source_id: str
    title: Optional[str] = None 