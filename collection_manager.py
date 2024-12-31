import chromadb
from logger import logger

def check_collection_health(collection) -> dict:
    """Tell if collection good or bad and why."""
    try:
        # Count documents
        doc_count = collection.count()
        
        # Get collection info
        embedding_size = None
        try:
            if doc_count > 0:
                # Try get first document to see embedding size
                first_doc = collection.get(limit=1)
                if first_doc and first_doc['embeddings']:
                    embedding_size = len(first_doc['embeddings'][0])
                    # If wrong size, collection not healthy
                    if embedding_size != 3072:
                        return {
                            "is_healthy": False,
                            "doc_count": doc_count,
                            "can_query": False,
                            "embedding_size": embedding_size,
                            "error": f"Collection has wrong embedding size: {embedding_size} (expected 3072)"
                        }
        except Exception:
            pass
        
        # Get one document to check if can read
        if doc_count > 0:
            test_results = collection.query(
                query_embeddings=[[0] * 3072],  # always use 3072
                n_results=1
            )
            can_query = len(test_results['documents'][0]) > 0
        else:
            can_query = True  # empty but working
            
        return {
            "is_healthy": True,
            "doc_count": doc_count,
            "can_query": can_query,
            "embedding_size": embedding_size,
            "error": None
        }
        
    except Exception as e:
        return {
            "is_healthy": False,
            "doc_count": 0,
            "can_query": False,
            "embedding_size": None,
            "error": str(e)
        }

def init_collection(path: str = "./chroma_db") -> tuple[chromadb.PersistentClient, chromadb.Collection]:
    """Start up collection, tell if something wrong."""
    try:
        # Try connect to database
        client = chromadb.PersistentClient(path=path)
        collection = client.get_or_create_collection("docs")
        
        # Check if collection good
        health = check_collection_health(collection)
        
        if health["is_healthy"]:
            size_info = f" (embedding size: {health['embedding_size']})" if health['embedding_size'] else ""
            logger.info(f"Collection ready - {health['doc_count']} documents found{size_info}")
        else:
            logger.error(f"Collection not healthy: {health['error']}")
            
        return client, collection
        
    except Exception as e:
        logger.error(f"Could not start collection: {str(e)}")
        raise

def check_document_exists(collection, doc_id: str) -> bool:
    """See if document already in collection."""
    try:
        results = collection.get(ids=[doc_id])
        return len(results['documents']) > 0
    except Exception as e:
        logger.error(f"Error checking document existence: {str(e)}")
        return False

def get_all_document_ids(collection) -> list[str]:
    """Get list of all document IDs in collection."""
    try:
        return collection.get()['ids']
    except Exception as e:
        logger.error(f"Error getting all document IDs: {str(e)}")
        return [] 

def delete_collection(client: chromadb.PersistentClient) -> None:
    """Delete collection if exists."""
    try:
        client.delete_collection("docs")
        logger.info("Collection deleted successfully")
    except Exception as e:
        logger.error(f"Failed to delete collection: {str(e)}")
        raise 