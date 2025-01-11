# TODO: change this to the model you want to use
CURRENT_MODEL = "text-embedding-3-large"

MODEL_CONFIGS = {
    "text-embedding-3-large": {
        "max_tokens": 8191,
        "chunk_size": 3000,
        "dimensions": 3072,
    },
    "text-embedding-3-small": {
        "max_tokens": 8191,
        "chunk_size": 2000,
        "dimensions": 1536,
    },
    # ... other models ...
}

# Set of usage by outside code (e.g. embeddings.py, splitter.py)
ACTIVE_CONFIG = MODEL_CONFIGS[CURRENT_MODEL]