import re
from typing import List, Optional
import tiktoken
from dataclasses import dataclass

from .base import TextChunker
from .types import Chunk, DenseChunk

@dataclass
class AnnotatedSentence:
    text: str
    start_line: int
    end_line: int

class DenseChunker(TextChunker):
    """Chunker that splits text into small overlapping chunks."""
    
    def __init__(
        self,
        chunk_size: int = 512,
        chunk_overlap: int = 128,
        model: str = "gpt-3.5-turbo",
        max_sentences: int = 3  # Maximum sentences per chunk
    ):
        """
        Initialize chunker with size and overlap settings.
        
        Args:
            chunk_size: Target size of each chunk in tokens
            chunk_overlap: Number of tokens to overlap between chunks
            model: Model name to use for tokenization (default: gpt-3.5-turbo)
            max_sentences: Maximum number of sentences per chunk
        """
        # Validate parameters
        if chunk_size < 1:
            raise ValueError("chunk_size must be >= 1")
        if chunk_overlap < 0:
            raise ValueError("chunk_overlap must be >= 0")
        if chunk_overlap >= chunk_size:
            raise ValueError("chunk_overlap must be < chunk_size")
        if max_sentences < 1:
            raise ValueError("max_sentences must be >= 1")
            
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.tokenizer = tiktoken.encoding_for_model(model)
        self.max_sentences = max_sentences
        
    def _annotate_sentences_with_positions(self, text: str) -> List[AnnotatedSentence]:
        """
        Split text into lines, then into sentences, annotating each
        sentence with actual start_line/end_line.
        """
        if not text or not text.strip():
            return []

        lines = text.split('\n')
        annotated: List[AnnotatedSentence] = []
        current_line_num = 1

        for line in lines:
            stripped = line.strip()
            if not stripped:
                current_line_num += 1
                continue

            # Re-use the existing _split_into_sentences logic on this line
            # but each piece is physically in the same line number
            parts = self._split_into_sentences(line)
            for sent in parts:
                if sent.strip():
                    annotated.append(AnnotatedSentence(
                        text=sent.strip(),
                        start_line=current_line_num,
                        end_line=current_line_num
                    ))
            current_line_num += 1

        return annotated
    
    def _count_tokens(self, text: str) -> int:
        """Count tokens in text using the configured tokenizer."""
        return len(self.tokenizer.encode(text))
    
    def _split_into_sentences(self, text: str) -> List[str]:
        """Split text into sentences."""
        # Handle empty or whitespace text
        if not text or not text.strip():
            return []
            
        # Split on sentence boundaries
        sentences = []
        
        for line in text.split('\n'):
            if not line.strip():
                continue
                
            # Split line into sentences
            parts = re.split(r'([.!?]+(?:\s+|$))', line)
            current_sentence = []
            
            for i in range(len(parts)):
                part = parts[i].strip()
                if not part:
                    continue
                    
                if i % 2 == 0:  # Content
                    current_sentence.append(part)
                else:  # Punctuation
                    if current_sentence:
                        sentences.append(' '.join(current_sentence))
                        current_sentence = []
            
            # Handle any remaining text without sentence boundary
            if current_sentence:
                sentences.append(' '.join(current_sentence))
            
        return sentences if sentences else [text.strip()]
    
    def chunk(self, text: str, source_id: str, metadata: Optional[dict] = None) -> List[Chunk]:
        """Split text into overlapping chunks of roughly equal token size."""
        if not text or not text.strip():
            raise ValueError("text cannot be empty or whitespace")
        
        if metadata is None:
            metadata = {}
            
        # Get all sentences with their line numbers
        annotated = self._annotate_sentences_with_positions(text)
        chunks: List[DenseChunk] = []
        
        # Variables for current chunk we're building
        current_sentences = []
        current_tokens = 0
        current_start = 0
        current_end = 0
        
        for sentence in annotated:
            sentence_tokens = self._count_tokens(sentence.text)
            
            # If this single sentence is too big, force split it
            if sentence_tokens > self.chunk_size:
                # First save any accumulated sentences as their own chunk
                if current_sentences:
                    chunks.append(DenseChunk(
                        text=' '.join(s.text for s in current_sentences),
                        start_line=current_start,
                        end_line=current_end,
                        source_id=source_id,
                        metadata=metadata,
                        token_count=current_tokens,
                        overlap_next=None
                    ))
                    current_sentences = []
                    current_tokens = 0
                
                # Split long sentence into chunks of chunk_size
                tokens = self.tokenizer.encode(sentence.text)
                for i in range(0, len(tokens), self.chunk_size):
                    sub_tokens = tokens[i:i + self.chunk_size]
                    chunks.append(DenseChunk(
                        text=self.tokenizer.decode(sub_tokens),
                        start_line=sentence.start_line,
                        end_line=sentence.end_line,
                        source_id=source_id,
                        metadata=metadata,
                        token_count=len(sub_tokens),
                        overlap_next=None
                    ))
                continue
            
            # If adding this sentence would exceed limits, save current chunk
            if (current_tokens + sentence_tokens > self.chunk_size or 
                len(current_sentences) >= self.max_sentences):
                if current_sentences:
                    chunks.append(DenseChunk(
                        text=' '.join(s.text for s in current_sentences),
                        start_line=current_start,
                        end_line=current_end,
                        source_id=source_id,
                        metadata=metadata,
                        token_count=current_tokens,
                        overlap_next=None
                    ))
                    # Keep last sentence for overlap if needed
                    if self.chunk_overlap > 0 and current_sentences:
                        last = current_sentences[-1]
                        current_sentences = [last]
                        current_tokens = self._count_tokens(last.text)
                        current_start = last.start_line
                        current_end = last.end_line
                    else:
                        current_sentences = []
                        current_tokens = 0
            
            # Add sentence to current chunk
            if not current_sentences:
                current_start = sentence.start_line
            current_sentences.append(sentence)
            current_tokens += sentence_tokens
            current_end = sentence.end_line
        
        # Save final chunk if anything remains
        if current_sentences:
            chunks.append(DenseChunk(
                text=' '.join(s.text for s in current_sentences),
                start_line=current_start,
                end_line=current_end,
                source_id=source_id,
                metadata=metadata,
                token_count=current_tokens,
                overlap_next=None
            ))
        
        # Calculate overlaps by taking fixed number of tokens from end/start
        for i in range(len(chunks) - 1):
            chunks[i].overlap_next = min(
                self.chunk_overlap,
                chunks[i].token_count,
                chunks[i + 1].token_count
            )
        
        return chunks
    
    def validate_chunk(self, chunk: Chunk) -> bool:
        """Validate chunk meets dense chunking requirements."""
        if not isinstance(chunk, DenseChunk):
            return False
            
        # Check chunk has required fields
        if not all([
            chunk.text,
            chunk.start_line > 0,
            chunk.end_line >= chunk.start_line,
            chunk.source_id,
            isinstance(chunk.metadata, dict),
            chunk.token_count > 0
        ]):
            return False
            
        # Validate token count is within expected range
        actual_tokens = self._count_tokens(chunk.text)
        if abs(actual_tokens - chunk.token_count) > 10:  # Allow small difference
            return False
            
        # Validate overlap if not last chunk
        if chunk.overlap_next is not None:
            if not 0 <= chunk.overlap_next <= self.chunk_overlap:
                return False
                
        return True