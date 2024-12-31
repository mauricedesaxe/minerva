import os
from typing import List
from openai import OpenAI
from dotenv import load_dotenv
import argparse
from logger import logger
import logging
from collection_manager import init_collection, check_collection_health

# Load environment variables
load_dotenv()

# Initialize clients
openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
chroma_client, collection = init_collection()

def get_embeddings(text: str) -> List[float]:
    """Get embeddings from OpenAI."""
    try:
        response = openai_client.embeddings.create(
            model="text-embedding-3-large",
            input=text
        )
        return response.data[0].embedding
    except Exception as e:
        logger.error("Failed to get embeddings: %s", str(e))
        raise

def get_relevant_context(query: str, limit: int = 5) -> str:
    """Get relevant documents from ChromaDB."""
    query_embedding = get_embeddings(query)
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=limit
    )
    
    for doc, dist in zip(results['documents'][0], results['distances'][0]):
        logger.debug(f"Distance {dist:.3f}: {doc[:100]}...")
    
    context = "\n\n".join(results['documents'][0])
    return context

def chat_with_gpt(query: str, context: str) -> str:
    """Get response from GPT-4 with context."""
    try:
        messages = [
            {"role": "system", "content": "You are a helpful assistant. Use the provided context to answer questions. If you can't find the answer in the context, say so."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
        ]
        
        response = openai_client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content
    except Exception as e:
        logger.error("Failed to get GPT response: %s", str(e))
        raise

def main():
    parser = argparse.ArgumentParser(description="Chat with your documents using GPT-4")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)
    
    print("\n=== DocChat - Your Document Assistant ===")
    print("Loading knowledge base...")
    
    # Check collection health
    health = check_collection_health(collection)
    if not health["is_healthy"]:
        print(f"\n⚠️  Warning: Collection not healthy - {health['error']}")
        print("Some features may not work correctly.")
    else:
        doc_count = health["doc_count"]
        if doc_count == 0:
            print("\n📚 No documents found in collection.")
            print("Please process some documents first using process_docs.py")
        else:
            print(f"\n📚 Found {doc_count} document chunks ready for chat")
    
    print("\nType your question or 'quit' to exit.")
    print("----------------------------------------")
    
    while True:
        try:
            query = input("\nYou: ").strip()
            
            if query.lower() in ['quit', 'exit']:
                print("\nGoodbye! 👋")
                break
                
            if not query:
                continue
            
            if health["doc_count"] == 0:
                print("\nℹ️  No documents to search through. Please add some documents first.")
                continue
            
            print("\nSearching for relevant information...")
            context = get_relevant_context(query)
            
            print("Thinking...")
            response = chat_with_gpt(query, context)
            
            print("\nAssistant:", response)
            
        except KeyboardInterrupt:
            print("\nGoodbye! 👋")
            break
        except Exception as e:
            logger.error("Error: %s", str(e))
            print("\n❌ Sorry, something went wrong. Please try again.")

if __name__ == "__main__":
    main() 