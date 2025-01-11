from typing import List
from openai import OpenAI
from functools import lru_cache
from fastapi import HTTPException
from modules.logger import logger
from api.schemas.error import ErrorCode
from modules.env import OPENAI_API_KEY
from modules.embedding_conf import CURRENT_MODEL, ACTIVE_CONFIG
import time

openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Cache common query embeddings (uses very little RAM, big speed win)
@lru_cache(maxsize=1000)
def get_query_embedding(text: str) -> List[float]:
    """Get single query embedding from OpenAI with cache."""
    try:
        start_time = time.time()
        logger.debug("Getting query embedding for text: %s", text)
        response = openai_client.embeddings.create(
            model=CURRENT_MODEL,
            input=[text]
        )
        end_time = time.time()
        logger.debug("Query embedding retrieved in %s seconds", end_time - start_time)
        return response.data[0].embedding
    except Exception as e:
        logger.error("Failed to get query embedding: %s", str(e))
        raise HTTPException(
            status_code=500,
            detail={
                "error": {
                    "code": ErrorCode.PROCESSING_ERROR,
                    "message": f"Failed to get query embedding: {str(e)}"
                }
            }
        )

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
            raise ValueError(f"Chunk too large for model {CURRENT_MODEL}")
            
        # Log API request details
        logger.debug("Making OpenAI API request with model: %s", CURRENT_MODEL)
        logger.debug("Request payload size: %d bytes", 
            sum(len(t.encode('utf-8')) for t in texts)
        )
        response = openai_client.embeddings.create(
            model=CURRENT_MODEL,
            input=texts
        )
        logger.debug("Successfully got embeddings")
        return [data.embedding for data in response.data]
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