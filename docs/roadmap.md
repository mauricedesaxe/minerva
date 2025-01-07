# Roadmap

This shouldn't be treated as a hard roadmap. It's more of a wishlist.

## Best practice sort of things
- [ ] add e2e tests for processing a wide range of files
- [ ] add e2e tests for evaluating /search responses
- [ ] add better observability (metrics, tracing, logging)
- [ ] add performance benchmarks (how fast can we process a file?)
- [ ] add more robust authentication, authorization, and rate limiting
- [ ] export of TypeScript types for the API
- [ ] explore performance improvements (e.g. batch processing, parallel/streaming processing, porting to Go/Rust, etc.)
- [ ] add cleanup for old jobs
- [ ] add timeout for processing jobs?
- [ ] handle OpenAI rate limits
- [ ] add caching (for search, for embeddings)
- [ ] what happens if Minerva crashes during a job processing?
- [ ] should there be a limit to how many jobs can be running at once?

## Feature ideation
- [ ] add S3 bucket listener for auto-processing
- [ ] add support for more file formats (e.g. PDF, DOCX, etc.)
- [ ] add support for more file types (e.g. images, videos, etc.)
- [ ] add support for other embedding models (e.g. OpenAI, Groq, Cohere, etc.)
- [ ] add support for other vector stores (e.g. PGVector, Pinecone, etc.)
- [ ] add webhook support for job completion
- [ ] add special handling for code blocks in markdown files
- [ ] add document / chunk deletion API
- [ ] add pagination for search results
- [ ] add reranking for search results
- [ ] add similarity threshold for search results
- [ ] add direct embedding generation endpoint (you pass in text, you get back embeddings)
- [ ] add more metadata? (e.g. line of chunk in text, tags, etc.)
- [ ] add query destructuring for search or query destructuring API endpoint
- [ ] add chunk context retrieval (get surrounding chunks)
- [ ] add backup/restore functionality for vector store
- [ ] add document preprocessing hooks? (custom transformations)
- [ ] add route to list all documents
- [ ] add openai SDK compatible embedding models