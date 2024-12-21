# Minerva

Minerva is a document processing service designed for RAG (Retrieval Augmented Generation) applications. 
It processes documents from various sources, chunks them semantically, generates embeddings, and stores them in a PostgreSQL database for efficient retrieval.

*Fun fact: Minerva is the Roman goddess of wisdom, knowledge, and the patron saint of libraries.*
We are providing knowledge to LLMs.

## Features

- Document processing from S3 storage
- Support for multiple file formats (Markdown, PDF, Google Docs, Notion exports)
- Semantic text chunking with both dense and sparse representations
- OpenAI embeddings generation
- Vector storage using PostgreSQL with pgvector/PGAI

## Requirements

- Python 3.11+
- PostgreSQL with pgvector extension
- OpenAI API key
- AWS credentials for S3 access

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/minerva.git
cd minerva

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"
```

## Usage

```bash
uv run main.py
```

## Testing

```bash
uv run pytest
```

## Linting and Formatting

```bash
uv black .
uv isort .
```

## Type Checking

```bash
uv mypy .
```
