import time
from openai import OpenAI
from functools import lru_cache
from fastapi import HTTPException
from modules.logger import logger
from api.schemas.error import ErrorCode
from modules.env import OPENAI_API_KEY, OLLAMA_URL
from modules.embedding_conf import EMBEDDING_MODEL, ACTIVE_CONFIG
import ollama

# Initialize clients based on provider
if ACTIVE_CONFIG["provider"] == "openai":
    if not OPENAI_API_KEY:
        raise ValueError("OpenAI API key required for OpenAI models")
    openai_client = OpenAI(api_key=OPENAI_API_KEY)
else:  # ollama
    ollama_client = ollama.Client(host=OLLAMA_URL)

# Cache common query embeddings (uses very little RAM, big speed win)
@lru_cache(maxsize=1000)
def get_query_embedding(text: str | list[str]) -> list[list[float]] | list[float]:
    """Get embeddings from the active provider."""
    start_time = time.time()
    logger.debug("Getting query embedding for text: %s", text)
    if ACTIVE_CONFIG["provider"] == "openai":
        embeddings = _get_openai_embedding(text)
    else:
        embeddings = _get_ollama_embedding(text)
    end_time = time.time()
    logger.debug("Query embedding retrieved in %s seconds with model %s", end_time - start_time, EMBEDDING_MODEL)
    return embeddings

def get_document_chunk_embeddings(texts: list[str]) -> list[list[float]]:
    """Get embeddings for multiple document chunks from OpenAI."""
    try:
        # Log chunk statistics
        logger.debug("Chunk statistics:")
        logger.debug("Number of chunks: %d", len(texts))
        logger.debug("Chunk sizes: min=%d, max=%d, avg=%d",
            min(len(t) for t in texts),
            max(len(t) for t in texts),
            sum(len(t) for t in texts) // len(texts)
        )
        
        # Log sample of first chunk and largest chunk
        largest_chunk = max(texts, key=len)
        logger.debug("First chunk sample (first 100 chars): %s", texts[0][:100])
        logger.debug("Largest chunk sample (first 100 chars): %s", largest_chunk[:100])
        
        # Validate input
        if not texts:
            raise ValueError("Empty text list provided")
        if any(not isinstance(t, str) for t in texts):
            raise ValueError("All chunks must be strings")
        if any(len(t.strip()) == 0 for t in texts):
            raise ValueError("Empty chunks detected")
            
        # Add config-based validation
        max_tokens = ACTIVE_CONFIG["max_tokens"]
        if any(len(t) > max_tokens for t in texts):
            raise ValueError(f"Chunk too large for model {EMBEDDING_MODEL}")
            
        # Log API request details
        logger.debug("Making OpenAI API request with model: %s", EMBEDDING_MODEL)
        logger.debug("Request payload size: %d bytes", 
            sum(len(t.encode('utf-8')) for t in texts)
        )
        
        if ACTIVE_CONFIG["provider"] == "openai":
            embeddings = _get_openai_embedding(texts)
        else:
            embeddings = _get_ollama_embedding(texts)
        
        logger.debug("Successfully got embeddings")
        return embeddings
    except Exception as e:
        logger.error("Failed to get embeddings: %s", str(e))
        # Log more error details if available
        if hasattr(e, 'response'):
            logger.error("API Response details: %s", e.response)
        raise HTTPException(
            status_code=500,
            detail={
                "error": {
                    "code": ErrorCode.PROCESSING_ERROR,
                    "message": f"Failed to get embeddings: {str(e)}"
                }
            }
        )
    
def _get_openai_embedding(text: str | list[str]) -> list[list[float]] | list[float]:
    """Get embeddings from OpenAI."""
    response = openai_client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )
    return response.data[0].embedding if isinstance(text, str) else [d.embedding for d in response.data]

def _get_ollama_embedding(text: str | list[str]) -> list[list[float]] | list[float]:
    """Get embeddings from Ollama."""
    if isinstance(text, str):
        texts = [text]
    else:
        texts = text

    embeddings = []
    for chunk in texts:
        response = ollama_client.embeddings(model=EMBEDDING_MODEL, prompt=chunk)
        embeddings.append(response['embedding'])
    
    return embeddings[0] if isinstance(text, str) else embeddings

def test_embedding_provider() -> list[float]:
    """Test the embedding provider."""
    text = "This is a test embedding."
    if ACTIVE_CONFIG["provider"] == "openai":
        embeddings = _get_openai_embedding(text)
    else:
        embeddings = _get_ollama_embedding(text)
    return embeddings