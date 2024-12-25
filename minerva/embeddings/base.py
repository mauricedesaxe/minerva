from abc import ABC, abstractmethod
from typing import Optional

from minerva.chunker.types import Chunk
from .types import Embedding

class TextEmbedder(ABC):
    """Base interface for text embedding generators."""
    
    @abstractmethod
    def embed(self, chunk: Chunk) -> Embedding:
        """
        Generate embedding vector for a text chunk.
        
        Args:
            chunk: The text chunk to embed
            
        Returns:
            Embedding containing the vector and metadata
            
        Raises:
            EmbeddingError: If embedding generation fails
        """
        pass

    @abstractmethod
    def validate_embedding(self, embedding: Embedding) -> bool:
        """
        Validate an embedding meets requirements.
        
        Args:
            embedding: The embedding to validate
            
        Returns:
            True if embedding is valid, False otherwise
        """
        pass 