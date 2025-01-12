from modules.embeddings import get_query_embedding
import numpy as np
from modules.logger import logger

def cosine_similarity(v1, v2):
    """Get cosine similarity between two vectors."""
    dot_product = np.dot(v1, v2)
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)
    return dot_product / (norm1 * norm2)

def main():
    # Words to compare
    word1 = "soccer"
    word2 = "football"
    
    logger.info("Getting embeddings for '%s' and '%s'", word1, word2)
    
    # Get embeddings
    embedding1 = get_query_embedding(word1)
    embedding2 = get_query_embedding(word2)
    
    # Calculate similarity
    similarity = cosine_similarity(embedding1, embedding2)
    
    # Print results
    logger.info("Similarity score: %.4f", similarity)
    logger.info("Words are %d%% similar", int(similarity * 100))

if __name__ == "__main__":
    main() 