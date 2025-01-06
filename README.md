# Minerva

Smart document assistant that helps you vectorize documents from S3.

## What It Does

- Processes markdown documents with smart chunking strategy
- Stores document chunks with embeddings in vector database
- Lets you ask questions about your documents using natural language

## Quick Start

1. Set up environment:
```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials
```

3. Process a document from S3:
```bash
python scripts/process_docs.py path/to/your/doc.md
```

4. Chat with your documents:
```bash
python scripts/chatbot.py
```

5. Turn on the server:
```bash
uvicorn api.main:app --reload --log-level debug
```
