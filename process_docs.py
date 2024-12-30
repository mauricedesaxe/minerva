import os
from typing import List, Dict
from openai import OpenAI
import chromadb
from dotenv import load_dotenv
import argparse
from s3_connection import get_s3_client, check_bucket_exists, get_file_content

# Load environment variables
load_dotenv()

# Initialize clients
s3_client = get_s3_client()
openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("docs")

def split_text(text: str, chunk_size: int = 1000) -> List[str]:
    """Split text into chunks, trying to preserve markdown structure."""
    # Split by double newline (markdown paragraphs)
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""
    
    for para in paragraphs:
        if len(current_chunk) + len(para) < chunk_size:
            current_chunk += para + "\n\n"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

def get_embeddings(texts: List[str]) -> List[List[float]]:
    """Get embeddings from OpenAI."""
    try:
        response = openai_client.embeddings.create(
            model="text-embedding-3-large",
            input=texts
        )
        return [data.embedding for data in response.data]
    except Exception as e:
        print(f"Error getting embeddings: {str(e)}")
        raise

def process_markdown_file(bucket: str, key: str) -> Dict:
    """Process a single markdown file."""
    try:
        # Get content from S3
        content = get_file_content(bucket, key, s3_client)
        
        # Split into chunks
        chunks = split_text(content)
        
        # Get embeddings
        embeddings = get_embeddings(chunks)
        
        # Store in ChromaDB
        collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=[f"{key}_{i}" for i in range(len(chunks))],
            metadatas=[{"source": key, "chunk": i} for i in range(len(chunks))]
        )
        
        return {
            "status": "success",
            "chunks_processed": len(chunks),
            "source": key
        }
        
    except Exception as e:
        print(f"Error processing file {key}: {str(e)}")
        return {
            "status": "error",
            "error": str(e),
            "source": key
        }

def search_similar(query: str, limit: int = 5) -> List[Dict]:
    """Search for similar chunks."""
    # Get query embedding
    query_embedding = get_embeddings([query])[0]
    
    # Search in ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=limit
    )
    
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

    args = parser.parse_args()

    bucket = os.getenv('BUCKET_NAME')
    if not bucket:
        print("Error: BUCKET_NAME environment variable not set")
        exit(1)

    # Check if bucket exists first
    if not check_bucket_exists(bucket):
        print(f"Error: Bucket '{bucket}' not found or not accessible")
        print("Check your credentials and bucket name")
        exit(1)
    
    # Process the file
    result = process_markdown_file(bucket, args.file_path)
    print("\nProcessing result:", result)
    
    if result["status"] == "success":
        # Try a search
        query = "What is Minerva?"
        results = search_similar(query)
        print("\nSearch results for:", query)
        for r in results:
            print(f"\nText: {r['text'][:200]}...")
            print(f"Source: {r['metadata']['source']}")
            print(f"Distance: {r['distance']}")