from abc import ABC, abstractmethod
from typing import List, Optional

from .types import Chunk

class TextChunker(ABC):
    """Base interface for text chunkers."""
    
    @abstractmethod
    def chunk(self, text: str, source_id: str, metadata: Optional[dict] = None) -> List[Chunk]:
        """
        Split text into chunks.
        
        Args:
            text: The text to split into chunks
            source_id: Unique identifier for the text source
            metadata: Optional metadata about the text source
            
        Returns:
            List of chunks
            
        Raises:
            ChunkingError: If text cannot be chunked
        """
        pass

    @abstractmethod
    def validate_chunk(self, chunk: Chunk) -> bool:
        """
        Validate a chunk meets the chunker's requirements.
        
        Args:
            chunk: The chunk to validate
            
        Returns:
            True if chunk is valid, False otherwise
        """
        pass 