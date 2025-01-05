from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
from openai import OpenAI
import os
from modules.collection_manager import init_collection
from modules.logger import logger
from ..schemas.error import ErrorCode

router = APIRouter(prefix="/api/v1/search", tags=["search"])

# Initialize clients
openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
chroma_client, collection = init_collection()

class SearchRequest(BaseModel):
    query: str
    limit: int = Field(default=5, ge=1, le=20)

    class Config:
        json_schema_extra = {
            "example": {
                "query": "Timing the fundraising cycle",
                "limit": 3
            }
        }

class SearchResult(BaseModel):
    text: str
    metadata: dict
    similarity: float

class SearchResponse(BaseModel):
    results: List[SearchResult]

    class Config:
        json_schema_extra = {
            "example": {
                "results": [
                    {
                        "text": "The best time to start fundraising is typically 18-24 months before you run out of money. This gives you enough runway to run a proper process and maintain leverage in negotiations.",
                        "metadata": {
                            "source": "fundraising/timing.md",
                            "chunk": 0
                        },
                        "similarity": 0.89
                    }
                ]
            }
        }

def get_embeddings(text: str) -> List[float]:
    """Get embeddings from OpenAI."""
    try:
        response = openai_client.embeddings.create(
            model="text-embedding-3-large",
            input=[text]
        )
        return response.data[0].embedding
    except Exception as e:
        logger.error("Failed to get embeddings: %s", str(e))
        raise HTTPException(
            status_code=500,
            detail={
                "error": {
                    "code": ErrorCode.PROCESSING_ERROR,
                    "message": f"Failed to get embeddings: {str(e)}"
                }
            }
        )

@router.post("", response_model=SearchResponse)
async def search_documents(request: SearchRequest):
    try:
        # Get query embedding
        query_embedding = get_embeddings(request.query)
        
        # Search in ChromaDB
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=request.limit
        )
        
        # Format response
        search_results = [
            SearchResult(
                text=doc,
                metadata=meta,
                similarity=1 - dist  # Convert distance to similarity score
            )
            for doc, meta, dist in zip(
                results['documents'][0],
                results['metadatas'][0],
                results['distances'][0]
            )
        ]
        
        return SearchResponse(results=search_results)
        
    except Exception as e:
        logger.error("Search failed: %s", str(e))
        raise HTTPException(
            status_code=500,
            detail={
                "error": {
                    "code": ErrorCode.PROCESSING_ERROR,
                    "message": f"Search failed: {str(e)}"
                }
            }
        ) 