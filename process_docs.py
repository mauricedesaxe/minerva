import os
from typing import List, Dict
from openai import OpenAI
import chromadb
from dotenv import load_dotenv
import argparse
from s3_connection import get_s3_client, check_bucket_exists, get_file_content
from splitter import split_text
from logger import logger
import logging

# Load environment variables
load_dotenv()

# Initialize clients
s3_client = get_s3_client()
openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("docs")

def get_embeddings(texts: List[str]) -> List[List[float]]:
    """Get embeddings from OpenAI."""
    try:
        logger.info("Getting embeddings for %d chunks", len(texts))
        response = openai_client.embeddings.create(
            model="text-embedding-3-large",
            input=texts
        )
        logger.debug("Successfully got embeddings")
        return [data.embedding for data in response.data]
    except Exception as e:
        logger.error("Failed to get embeddings: %s", str(e))
        raise

def process_markdown_file(bucket: str, key: str) -> Dict:
    """Process a single markdown file."""
    try:
        logger.info("Processing file: %s from bucket: %s", key, bucket)
        
        # Get content from S3
        logger.debug("Fetching content from S3")
        content = get_file_content(bucket, key, s3_client)
        
        # Split into chunks
        logger.debug("Splitting content into chunks")
        chunks = split_text(content)
        logger.info("Split into %d chunks", len(chunks))
        
        # Get embeddings
        embeddings = get_embeddings(chunks)
        
        # Store in ChromaDB
        logger.debug("Storing chunks in ChromaDB")
        collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=[f"{key}_{i}" for i in range(len(chunks))],
            metadatas=[{"source": key, "chunk": i} for i in range(len(chunks))]
        )
        
        logger.info("Successfully processed file %s", key)
        return {
            "status": "success",
            "chunks_processed": len(chunks),
            "source": key
        }
        
    except Exception as e:
        logger.error("Failed to process file %s: %s", key, str(e))
        return {
            "status": "error",
            "error": str(e),
            "source": key
        }

def search_similar(query: str, limit: int = 5) -> List[Dict]:
    """Search for similar chunks."""
    logger.info("Searching for: %s (limit: %d)", query, limit)
    
    # Get query embedding
    query_embedding = get_embeddings([query])[0]
    
    # Search in ChromaDB
    logger.debug("Querying ChromaDB")
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=limit
    )
    
    logger.info("Found %d results", len(results['documents'][0]))
    return [
        {
            "text": doc,
            "metadata": meta,
            "distance": dist
        }
        for doc, meta, dist in zip(
            results['documents'][0],
            results['metadatas'][0],
            results['distances'][0]
        )
    ]

if __name__ == "__main__":
    # Set up command line arguments
    parser = argparse.ArgumentParser(
        description="Process markdown documents from Google Cloud Storage"
    )
    parser.add_argument(
        "file_path",
        help="Path to the markdown file in the bucket"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging"
    )

    args = parser.parse_args()

    # Set debug level if requested
    if args.debug:
        logger.setLevel(logging.DEBUG)

    bucket = os.getenv('BUCKET_NAME')
    if not bucket:
        logger.error("BUCKET_NAME environment variable not set")
        exit(1)

    # Check if bucket exists first
    if not check_bucket_exists(bucket):
        logger.error("Bucket '%s' not found or not accessible", bucket)
        logger.error("Check your credentials and bucket name")
        exit(1)
    
    # Process the file
    result = process_markdown_file(bucket, args.file_path)
    
    if result["status"] == "success":
        logger.info("Processing completed successfully")
        logger.info("Processed %d chunks from %s", 
                   result["chunks_processed"], 
                   result["source"])
        
        # Try a search
        query = "What is Minerva?"
        logger.info("Trying sample search: %s", query)
        results = search_similar(query)
        
        for i, r in enumerate(results, 1):
            logger.info("Result %d:", i)
            logger.info("Text: %s...", r['text'][:200])
            logger.info("Source: %s", r['metadata']['source'])
            logger.info("Distance: %f", r['distance'])
    else:
        logger.error("Processing failed: %s", result["error"])