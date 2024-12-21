from abc import ABC, abstractmethod
from typing import Optional
from .types import ParsedDocument

class DocumentParser(ABC):
    """Base interface for document parsers."""
    
    @abstractmethod
    def parse(self, content: bytes, content_type: str, source_id: str, 
             metadata: Optional[dict] = None) -> ParsedDocument:
        """
        Parse document bytes into clean text.
        
        Args:
            content: Raw bytes of the document
            content_type: MIME type of the document
            source_id: Unique identifier for the document source
            metadata: Optional metadata about the document
            
        Returns:
            ParsedDocument containing clean text and metadata
            
        Raises:
            ParserError: If document cannot be parsed
        """
        pass 