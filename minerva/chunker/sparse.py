import re
from typing import List, Optional, Tuple

from .base import TextChunker
from .types import Chunk, SparseChunk

class SparseChunker(TextChunker):
    """Chunker that splits text by semantic boundaries like headings."""
    
    def __init__(self, min_chunk_size: int = 50):
        """
        Initialize chunker.
        
        Args:
            min_chunk_size: Minimum characters per chunk
        """
        if min_chunk_size <= 0:
            raise ValueError("min_chunk_size must be > 0")
        self.min_chunk_size = min_chunk_size
        
    def _parse_heading(self, line: str) -> Tuple[Optional[str], int]:
        """Parse heading and its level from a line."""
        # First check for markdown style headings
        heading_match = re.match(r'^(#{1,5})\s+(.+)$', line.strip())
        if heading_match:
            return heading_match.group(2).strip(), len(heading_match.group(1))
        
        # Check for underlined headings by looking ahead
        if line and hasattr(self, '_next_line') and self._next_line:
            if all(c == '=' for c in self._next_line.strip()):
                return line.strip(), 1
            elif all(c == '-' for c in self._next_line.strip()):
                return line.strip(), 2
            
        return None, -1
        
    def chunk(self, text: str, source_id: str, metadata: Optional[dict] = None) -> List[Chunk]:
        """Split text into chunks based on semantic boundaries."""
        if not text:
            return []
            
        base_metadata = metadata.copy() if metadata is not None else {}
        lines = text.split('\n')
        chunks: List[SparseChunk] = []
        current_chunk_lines = []
        current_heading = None
        current_level = 0
        start_line = 1
        
        i = 0
        while i < len(lines):
            line = lines[i]
            self._next_line = lines[i + 1] if i + 1 < len(lines) else None
            
            heading, level = self._parse_heading(line)
            
            if heading is not None:
                # Save current chunk if it exists
                if current_chunk_lines:
                    chunk_text = '\n'.join(current_chunk_lines)
                    chunks.append(SparseChunk(
                        text=chunk_text,
                        start_line=start_line,
                        end_line=start_line + len(current_chunk_lines) - 1,
                        source_id=source_id,
                        metadata=base_metadata.copy(),
                        hierarchy_level=current_level,
                        heading=current_heading
                    ))
                
                # Start new chunk with heading
                current_chunk_lines = [line]
                if self._next_line and (all(c == '=' for c in self._next_line.strip()) or 
                                      all(c == '-' for c in self._next_line.strip())):
                    current_chunk_lines.append(self._next_line)
                    i += 1  # Skip the underline line
                current_heading = heading
                current_level = level
                start_line = i + 1
            else:
                current_chunk_lines.append(line)
            i += 1

        # Handle last chunk
        if current_chunk_lines:
            chunk_text = '\n'.join(current_chunk_lines)
            chunks.append(SparseChunk(
                text=chunk_text,
                start_line=start_line,
                end_line=start_line + len(current_chunk_lines) - 1,
                source_id=source_id,
                metadata=base_metadata.copy(),
                hierarchy_level=current_level,
                heading=current_heading
            ))
        
        self._set_chunk_relationships(chunks)
        return chunks
        
    def _set_chunk_relationships(self, chunks: List[SparseChunk]) -> None:
        """Set parent-child relationships between chunks based on hierarchy."""
        if not chunks:
            return
            
        # Process chunks in order
        stack = []  # Stack of potential parent chunks
        
        for chunk in chunks:
            # Pop chunks from stack if they're at same or higher level
            while stack and stack[-1].hierarchy_level >= chunk.hierarchy_level:
                stack.pop()
                
            # Set parent-child relationship if we have a parent
            if stack:
                parent = stack[-1]
                chunk.parent_id = id(parent)
                parent.child_ids.append(id(chunk))
                
            stack.append(chunk)
    
    def validate_chunk(self, chunk: Chunk) -> bool:
        """Simplified validation with fast fails"""
        if not isinstance(chunk, SparseChunk):
            return False
            
        try:
            # Basic structure checks
            if not chunk.text or not chunk.source_id:
                return False
                
            if not isinstance(chunk.metadata, dict):
                return False
                
            if chunk.start_line <= 0 or chunk.end_line < chunk.start_line:
                return False
                
            # Hierarchy checks
            if chunk.hierarchy_level < 0:
                return False
                
            # Size check - allow small chunks only if they're heading-only
            if chunk.hierarchy_level > 0 and len(chunk.text) < self.min_chunk_size:
                if not chunk.heading:
                    return False
                    
            return True
        except AttributeError:
            return False 