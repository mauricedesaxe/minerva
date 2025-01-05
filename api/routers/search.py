from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List

router = APIRouter(prefix="/api/v1/search", tags=["search"])

class SearchRequest(BaseModel):
    query: str
    limit: int = Field(default=5, ge=1, le=20)

class SearchResult(BaseModel):
    text: str
    metadata: dict
    similarity: float

class SearchResponse(BaseModel):
    results: List[SearchResult]

@router.post("", response_model=SearchResponse)
async def search_documents(request: SearchRequest):
    # TODO: Implement semantic search
    raise HTTPException(
        status_code=501,
        detail={
            "error": {
                "code": "not_implemented",
                "message": "Semantic search not yet implemented"
            }
        }
    ) 