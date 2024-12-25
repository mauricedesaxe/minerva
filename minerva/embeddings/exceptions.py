class EmbeddingError(Exception):
    """Base exception for embedding-related errors."""
    pass

class ModelNotFoundError(EmbeddingError):
    """Raised when specified embedding model is not found."""
    pass

class EmbeddingGenerationError(EmbeddingError):
    """Raised when embedding generation fails."""
    pass 