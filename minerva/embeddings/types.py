from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Dict, List, Optional

@dataclass
class Embedding:
    """Data class representing a text embedding with metadata."""
    # Required fields (no defaults) must come first
    text: str
    vector: List[float]
    model: str
    source_id: str
    metadata: Dict[str, str]
    start_line: int
    end_line: int
    
    # Optional fields with defaults must come after
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    parent_id: Optional[str] = None
    child_ids: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        if not self.text or not self.text.strip():
            raise ValueError("text cannot be empty")
        if not self.vector:
            raise ValueError("vector cannot be empty")
        if not self.model:
            raise ValueError("model cannot be empty")
        if not self.source_id:
            raise ValueError("source_id cannot be empty")
        if not isinstance(self.metadata, dict):
            raise ValueError("metadata must be a dict")
        if self.start_line < 1:
            raise ValueError("start_line must be >= 1")
        if self.end_line < self.start_line:
            raise ValueError("end_line must be >= start_line")
            
        # Create copy of metadata to ensure immutability
        self.metadata = self.metadata.copy()
        
        # Initialize child_ids if None
        if self.child_ids is None:
            self.child_ids = [] 