Here's a step-by-step approach to building Minerva v1:

Step 1: Core Infrastructure (The Basics)
- Make base config class with Pydantic that loads from env
- Set up PostgreSQL connection with SQLAlchemy
- Write tests that ensure config loads and DB connects
- Make simple logging setup
- Test all pieces work independently

Step 2: S3 Handler (The File Getter)
- Make simple class that gets file from S3 bucket
- Class only does ONE thing: get file bytes and metadata
- Return simple data class with bytes and metadata
- Test with mock S3 bucket
- No processing logic here, just get file

Step 3: Document Parser (The Text Extractor)
- Make base parser interface class
- Make markdown parser that implements interface
- Parser only does ONE thing: bytes to clean text
- Return simple data class with text and metadata
- Test with sample markdown files
- No chunking yet, just extraction

Step 4: Text Chunker (The Splitter)
- Make base chunker interface
- Implement two chunking strategies:
  1. DenseChunker:
     - Splits text into small overlapping chunks (e.g., 512 tokens with 128 token overlap)
     - Preserves sentence boundaries
     - Good for detailed QA
  2. SparseChunker:
     - Splits text by semantic boundaries (headings, sections)
     - Keeps logical units together
     - Good for topic-level retrieval
- Each chunk should contain:
  - Text content
  - Metadata about position
  - Parent-child relationships (sparse chunks know their dense chunks)
  - Hierarchy level (for sparse chunks)
- Test with:
  - Different document structures
  - Various heading depths
  - Edge cases (very short/long sections)
- Include chunk validation (min/max sizes, proper nesting)

Step 5: Embedding Generator (The AI Part)
- Make embedding interface class
- Make OpenAI embedder implementation
- Class only does ONE thing: text to vector
- Test with mock OpenAI responses
- Just generate embeddings, no storage yet

Step 6: Database Layer (The Storage)
- Make SQLAlchemy models for documents and chunks
- Make repository classes for each model
- Each repo has basic CRUD operations
- Test with temporary test database
- Just storage, no business logic

Step 7: Pipeline Orchestrator (The Glue)
- Make pipeline class that uses all above pieces
- Pipeline follows simple steps:
  1. Get file from S3
  2. Parse to text
  3. Split into chunks
  4. Generate embeddings
  5. Store in database
- Test full pipeline with mocks
- Add error handling and retries

Step 8: API Layer (The Interface)
- Make FastAPI app with basic endpoints:
  - Health check
  - Process document (async)
  - Get document status
  - Query similar chunks
- Test each endpoint independently
- Keep routes thin, logic in services
