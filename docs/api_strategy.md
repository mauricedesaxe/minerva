# FastAPI Strategy Document

## Overview

This document outlines the REST API design for interfacing with our document processing and search system. The API provides async document ingestion and semantic search capabilities.

## Goals

- Simple, predictable REST endpoints
- Async processing for large files
- Basic API key security
- Clear error responses
- Easy integration with RAG applications

## API Endpoints

### Authentication
- API key passed via header: `X-API-Key`
- Key configured through environment variables
- All endpoints require authentication

### 1. Document Processing

#### Start Processing
```
POST /api/v1/documents/process
Content-Type: application/json
X-API-Key: <api_key>

{
    "bucket": "string",
    "key": "string",
    "force_reload": false
}
```

Response:
```json
{
    "job_id": "string",
    "status": "processing",
    "created_at": "timestamp",
    "file_info": {
        "bucket": "string",
        "key": "string"
    }
}
```

#### Check Job Status
```
GET /api/v1/documents/jobs/{job_id}
X-API-Key: <api_key>
```

Response:
```json
{
    "job_id": "string",
    "status": "processing|completed|failed",
    "created_at": "timestamp",
    "completed_at": "timestamp|null",
    "file_info": {
        "bucket": "string",
        "key": "string"
    },
    "result": {
        "chunks_processed": 0,
        "error": "string|null"
    }
}
```

### 2. Search

#### Semantic Search
```
POST /api/v1/search
Content-Type: application/json
X-API-Key: <api_key>

{
    "query": "string",
    "limit": 5
}
```

Response:
```json
{
    "results": [
        {
            "text": "string",
            "metadata": {
                "source": "string",
                "chunk": 0
            },
            "similarity": 0.95
        }
    ]
}
```

## Implementation Notes

### Document Constraints
- Maximum file size: 5MB
- Supported format: Markdown (.md) only

### Job Storage
- Use SQLite database for job tracking
- Simple schema:
```sql
CREATE TABLE jobs (
    job_id TEXT PRIMARY KEY,
    status TEXT NOT NULL,  -- processing|completed|failed
    created_at TIMESTAMP NOT NULL,
    completed_at TIMESTAMP,
    bucket TEXT NOT NULL,
    file_key TEXT NOT NULL,
    chunks_processed INTEGER,
    error TEXT
);
```
- Benefits:
  - Persistent across restarts
  - Easy to query job history
  - No extra dependencies (SQLite built into Python)
  - Simple backup/restore
  - Can evolve schema as needed

### Error Handling
```json
{
    "error": {
        "code": "string",
        "message": "string",
    }
}
```

Common error codes:
- `auth_failed`: Invalid API key
- `invalid_request`: Bad input data
- `processing_error`: Document processing failed
- `not_found`: Job/Document not found
- `server_error`: Internal error

### Future Considerations
- Rate limiting
- Webhook callbacks for job completion
- Batch document processing
- Direct embedding generation endpoint
- Result pagination
- Document deletion API
- Health check endpoint
- Cleanup strategy for old jobs
- Timeouts for long-running jobs

## Usage Example

```python
# Process new document
response = requests.post(
    "http://api/v1/documents/process",
    headers={"X-API-Key": "your-key"},
    json={
        "bucket": "my-bucket",
        "key": "docs/example.md"
    }
)
job_id = response.json()["job_id"]

# Check status
status = requests.get(
    f"http://api/v1/documents/jobs/{job_id}",
    headers={"X-API-Key": "your-key"}
)

# Search
results = requests.post(
    "http://api/v1/search",
    headers={"X-API-Key": "your-key"},
    json={
        "query": "What is Minerva?",
        "limit": 5
    }
)
```

This design:
- Keeps endpoints simple and focused
- Uses standard REST patterns
- Provides clear error responses
- Follows existing code patterns
- Easy to extend later
