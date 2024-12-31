import chromadb
import json

# Initialize client
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("docs")

# Get all items
results = collection.get()

# Print each document with its ID and metadata
for i, (doc, metadata, id) in enumerate(zip(results['documents'], results['metadatas'], results['ids'])):
    print(f"\n=== Document {i+1} ===")
    print(f"ID: {id}")
    print(f"Metadata: {json.dumps(metadata, indent=2)}")
    print(f"Content: {doc[:200]}...")  # First 200 chars