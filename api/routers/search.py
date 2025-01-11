from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
from modules.collection_manager import init_collection
from modules.logger import logger
from ..schemas.error import ErrorCode
from modules.embeddings import get_query_embedding

router = APIRouter(prefix="/api/v1/search", tags=["search"])

# Initialize clients
chroma_client, collection = init_collection()

class SearchRequest(BaseModel):
    query: str
    limit: int = Field(default=5, ge=1, le=20)
    rerank: bool = Field(default=False)

    class Config:
        json_schema_extra = {
            "example": {
                "query": "Timing the fundraising cycle",
                "limit": 3,
                "rerank": True
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

@router.post("", response_model=SearchResponse)
async def search_documents(request: SearchRequest):
    """Search documents using semantic search with optional keyword-based reranking.
    
    Flow:
    1. Convert query to embedding using OpenAI API
    2. Find similar documents using ChromaDB vector search
    3. If rerank=True:
       - Get more initial results (3x requested limit, max 20)
       - Score documents using both semantic and keyword matching
       - Keyword score = % of query words present in document
       - Final score = (0.7 * semantic_score) + (0.3 * keyword_score)
       - Return top K reranked results
    4. If rerank=False:
       - Return raw semantic search results
       - Similarity scores based on vector distances only
    """
    try:
        # Only use initial_limit if reranking
        initial_limit = min(request.limit * 3, 20) if request.rerank else request.limit
        logger.debug(f"Using initial limit of {initial_limit} for query: {request.query}")
        
        query_embedding = get_query_embedding(request.query)
        logger.debug(f"Got embeddings of length {len(query_embedding)}")
        
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=initial_limit
        )
        logger.debug(f"Raw query returned {len(results['documents'][0])} results")

        if not request.rerank:
            # Just return semantic search results
            search_results = [
                SearchResult(
                    text=doc,
                    metadata=meta,
                    similarity=1 - dist
                )
                for doc, meta, dist in zip(
                    results['documents'][0],
                    results['metadatas'][0],
                    results['distances'][0]
                )
            ]
            logger.debug("Skipping reranking as rerank=False")
            return SearchResponse(results=search_results)

        # Rest of reranking logic only runs if rerank=True
        query_words = set(request.query.lower().split())
        logger.debug(f"Query words: {query_words}")
        
        # Calculate basic keyword scores
        keyword_scores = []
        for doc in results['documents'][0]:
            doc_words = set(doc.lower().split())
            # What percent of query words appear in doc
            score = len(query_words & doc_words) / len(query_words)
            keyword_scores.append(score)
            logger.debug(f"Document keyword score: {score:.3f} - First 50 chars: {doc[:50]}...")
        
        # Rest same as before but with simpler scoring
        semantic_scores = [1 - dist for dist in results['distances'][0]]
        logger.debug(f"Semantic scores: {[f'{score:.3f}' for score in semantic_scores]}")
        
        final_scores = [
            0.7 * sem_score + 0.3 * key_score
            for sem_score, key_score in zip(semantic_scores, keyword_scores)
        ]
        logger.debug(f"Combined final scores: {[f'{score:.3f}' for score in final_scores]}")
        
        # Sort by combined score and take top k
        sorted_indices = sorted(
            range(len(final_scores)), 
            key=lambda i: final_scores[i], 
            reverse=True
        )[:request.limit]
        logger.debug(f"Top {len(sorted_indices)} indices selected: {sorted_indices}")
        
        # Format response with reranked results
        search_results = [
            SearchResult(
                text=results['documents'][0][idx],
                metadata=results['metadatas'][0][idx],
                similarity=final_scores[idx]
            )
            for idx in sorted_indices
        ]
        logger.debug(f"Returning {len(search_results)} results")
        
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