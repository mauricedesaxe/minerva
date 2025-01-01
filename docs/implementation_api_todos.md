# Implementation TODOs

## 1. Project Setup
1. Create FastAPI project structure
2. Add API key middleware using environment variables
3. Set up error handling utilities (reuse modules/logger.py)

## 2. Database Layer
1. Create SQLite schema for jobs (reuse existing schema from strategy):
   ```sql
   CREATE TABLE jobs (
       job_id TEXT PRIMARY KEY,
       status TEXT NOT NULL,
       created_at TIMESTAMP NOT NULL,
       completed_at TIMESTAMP,
       bucket TEXT NOT NULL,
       file_key TEXT NOT NULL,
       chunks_processed INTEGER,
       error TEXT
   );
   ```
2. Create job repository (simple CRUD operations)

## 3. API Endpoints - Processing
1. Implement POST /api/v1/documents/process
   - Reuse modules/s3_connection.py for bucket/file validation
   - Create job record
   - Start background task using process_docs.process_markdown_file() from scripts/process_docs.py (may want to move to modules/process_docs.py, remove CLI-specific code, and modify to adapt to API strategy)
2. Implement GET /api/v1/documents/jobs/{job_id}
   - Query job status from SQLite
   - Return status format from API strategy

## 4. API Endpoints - Search 
1. Implement POST /api/v1/search
   - Reuse process_docs.search_similar() from scripts/process_docs.py (may want to move to modules/process_docs.py, remove CLI-specific code, and modify to adapt to API strategy)
   - Convert response format to match API strategy:
     - Rename 'distance' to 'similarity'
     - Format metadata correctly

## 5. Error Handling
1. Create error response models matching API strategy:
   ```python
   {
       "error": {
           "code": str,  # from strategy error codes
           "message": str
       }
   }
   ```
2. Add error handlers for:
   - auth_failed (invalid API key)
   - invalid_request (bad input)
   - processing_error (from process_docs.py)
   - not_found (job/document missing)
   - server_error (catch-all)

## 6. Testing
1. Set up test environment
2. Write API tests for endpoints
3. Test error responses
4. Add integration tests using test documents (might need to use scripts/upload_test_docs.py or logic from it)

## 7. Documentation
1. Add FastAPI docs
2. Update example usage for API context

## 8. Deployment
1. Create Dockerfile (include all dependencies)
2. Set up docker-compose.yml
3. Write deployment scripts 