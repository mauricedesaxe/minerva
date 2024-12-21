from datetime import datetime
import re
from typing import Optional, Dict

from .base import DocumentParser
from .types import ParsedDocument
from ..logging import get_logger

class MarkdownParser(DocumentParser):
    """Parser for Markdown documents."""
    
    def __init__(self):
        self.logger = get_logger(__name__)
    
    def _strip_markdown(self, text: str) -> str:
        """Strip markdown formatting from text."""
        # Remove bold and emphasis
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
        text = re.sub(r'\*(.*?)\*', r'\1', text)
        # Remove other markdown formatting as needed
        return text.strip()

    def _validate_metadata(self, metadata: Optional[Dict]) -> Dict:
        """Validate metadata is a dict with string keys."""
        if metadata is None:
            return {}
        if not isinstance(metadata, dict):
            raise TypeError("Metadata must be a dictionary")
        # Validate all keys are strings
        for key in metadata:
            if not isinstance(key, str):
                raise TypeError("Metadata keys must be strings")
        return metadata

    def parse(self, content: bytes, content_type: str, source_id: str,
             metadata: Optional[Dict] = None) -> ParsedDocument:
        """Parse markdown content while preserving the original text and markdown formatting."""
        self.logger.debug(f"Parsing markdown document: {source_id}")
        
        # Validate content type
        if content_type.lower() != "text/markdown":
            raise ValueError(f"Invalid content type: {content_type}. Expected text/markdown")
        
        # Validate metadata
        validated_metadata = self._validate_metadata(metadata)
        
        # Decode bytes to string
        text = content.decode('utf-8')
        
        # Extract title from first heading if present
        title = None
        first_line = text.splitlines()[0] if text else ''
        title_match = re.match(r'^#\s+(.+)$', first_line)
        if title_match:
            title = self._strip_markdown(title_match.group(1))
        
        # Return the document with original text preserved
        return ParsedDocument(
            text=text,
            content_type=content_type,
            size=len(content),
            parsed_at=datetime.utcnow(),
            metadata=validated_metadata,
            source_id=source_id,
            title=title
        )