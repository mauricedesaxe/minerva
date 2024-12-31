import os
from typing import List, Dict
from openai import OpenAI
import chromadb
from dotenv import load_dotenv
import argparse
from logger import logger
import logging

# Load environment variables
load_dotenv()

# Initialize clients
openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("docs")

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

def get_relevant_context(query: str, limit: int = 3) -> str:
    """Get relevant documents from ChromaDB."""
    query_embedding = get_embeddings(query)
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=limit
    )
    
    # Combine all relevant documents into one context string
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
            model="gpt-4o-mini",
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
    
    print("Welcome to DocChat! Type 'quit' to exit.")
    print("Loading knowledge base...")
    
    while True:
        try:
            query = input("\nYou: ").strip()
            
            if query.lower() in ['quit', 'exit']:
                print("Goodbye!")
                break
                
            if not query:
                continue
            
            logger.debug("Getting relevant context")
            context = get_relevant_context(query)
            
            logger.debug("Getting GPT response")
            response = chat_with_gpt(query, context)
            
            print("\nAssistant:", response)
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            logger.error("Error: %s", str(e))
            print("\nSorry, something went wrong. Please try again.")

if __name__ == "__main__":
    main() 