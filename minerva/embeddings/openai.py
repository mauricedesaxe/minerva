from openai import OpenAI
from typing import Optional

from minerva.config import get_config
from minerva.logging import get_logger
from minerva.chunker.types import Chunk
from .base import TextEmbedder
from .types import Embedding
from .exceptions import EmbeddingGenerationError, ModelNotFoundError

class OpenAIEmbedder(TextEmbedder):
    """Embedder that uses OpenAI's text-embedding-3-large model."""
    
    def __init__(self, model: str = "text-embedding-3-large"):
        self.logger = get_logger(__name__)
        self.model = model
        
        # Initialize OpenAI client
        config = get_config()
        if not config.openai_api_key:
            raise ValueError("OpenAI API key not found in config")
        self.client = OpenAI(api_key=config.openai_api_key)
        
        # TODO: Add input length validation
        # TODO: Add response caching
    
    def embed(self, chunk: Chunk) -> Embedding:
        """Generate embedding for text chunk using OpenAI."""
        self.logger.debug(f"Generating embedding for chunk from {chunk.source_id}")
        
        try:
            response = self.client.embeddings.create(
                model=self.model,
                input=chunk.text,
                encoding_format="float"
            )
            
            # OpenAI returns a list of embeddings, but we only send one text
            vector = response.data[0].embedding
            
            return Embedding(
                text=chunk.text,
                vector=vector,
                model=self.model,
                source_id=chunk.source_id,
                metadata=chunk.metadata,
                start_line=chunk.start_line,
                end_line=chunk.end_line,
                parent_id=chunk.parent_id,
                child_ids=chunk.child_ids
            )
            
        except Exception as e:
            self.logger.error(f"Failed to generate embedding: {str(e)}")
            raise EmbeddingGenerationError(f"Failed to generate embedding: {str(e)}")
    
    def validate_embedding(self, embedding: Embedding) -> bool:
        """Validate embedding meets requirements."""
        try:
            # Basic structure validation
            if not embedding.text or not embedding.vector:
                return False
                
            if not isinstance(embedding.metadata, dict):
                return False
                
            # Model validation
            if embedding.model != self.model:
                return False
                
            # Vector dimension validation for text-embedding-3-large (3072 dimensions)
            if len(embedding.vector) != 3072:
                return False
                
            return True
            
        except Exception:
            return False 