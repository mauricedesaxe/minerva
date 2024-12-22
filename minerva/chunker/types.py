from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Dict, List, Optional

@dataclass
class Chunk:
    """Base class for text chunks."""
    text: str
    start_line: int
    end_line: int
    source_id: str
    metadata: Dict[str, str]
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    parent_id: Optional[str] = field(default=None)
    child_ids: List[str] = field(default_factory=list)

    def __post_init__(self):
        # These should never be invalid
        if not self.text or not self.text.strip():
            raise ValueError("Chunk text cannot be empty")
        if self.start_line < 1:
            raise ValueError("start_line must be >= 1")
        if self.end_line < self.start_line:
            raise ValueError("end_line must be >= start_line")
        if not self.source_id:
            raise ValueError("source_id cannot be empty")
        if not isinstance(self.metadata, dict):
            raise ValueError("metadata must be a dict")
            
        # Create copy of metadata to ensure immutability
        self.metadata = self.metadata.copy()
        
        # Initialize child_ids if None
        if self.child_ids is None:
            self.child_ids = []

@dataclass(init=False)
class DenseChunk(Chunk):
    """Dense chunk with small, overlapping text segments."""
    token_count: int
    overlap_next: Optional[int] = field(default=None)
    
    def __init__(
        self,
        text: str,
        start_line: int,
        end_line: int,
        source_id: str,
        metadata: Dict[str, str],
        token_count: int,
        overlap_next: Optional[int] = None,
        created_at: Optional[datetime] = None,
        parent_id: Optional[str] = None,
        child_ids: Optional[List[str]] = None
    ):
        super().__init__(
            text=text,
            start_line=start_line,
            end_line=end_line,
            source_id=source_id,
            metadata=metadata,
            created_at=created_at or datetime.now(UTC),
            parent_id=parent_id,
            child_ids=child_ids
        )
        self.token_count = token_count
        self.overlap_next = overlap_next
        
        # Validate token count
        if self.token_count < 1:
            raise ValueError("token_count must be >= 1")
        # Validate overlap if present
        if self.overlap_next is not None and self.overlap_next < 0:
            raise ValueError("overlap_next must be >= 0")

@dataclass(init=False)
class SparseChunk(Chunk):
    """Sparse chunk representing semantic sections."""
    hierarchy_level: int
    heading: Optional[str] = field(default=None)
    
    def __init__(
        self,
        text: str,
        start_line: int,
        end_line: int,
        source_id: str,
        metadata: Dict[str, str],
        hierarchy_level: int,
        heading: Optional[str] = None,
        created_at: Optional[datetime] = None,
        parent_id: Optional[str] = None,
        child_ids: Optional[List[str]] = None
    ):
        # Validate hierarchy_level - should never be negative
        if hierarchy_level < 0:
            raise ValueError("hierarchy_level must be >= 0")
            
        super().__init__(
            text=text,
            start_line=start_line,
            end_line=end_line,
            source_id=source_id,
            metadata=metadata,
            created_at=created_at or datetime.now(UTC),
            parent_id=parent_id,
            child_ids=child_ids
        )
        
        self.hierarchy_level = hierarchy_level
        self.heading = heading

    def __post_init__(self):
        # No need to validate text/lines - base class does that
        # Just ensure metadata and child_ids are properly initialized
        self.metadata = self.metadata.copy()
        if self.child_ids is None:
            self.child_ids = []