from modules.env import EMBEDDING_MODEL

MODEL_CONFIGS = {
    "text-embedding-3-large": {
        "provider": "openai",
        "max_tokens": 8191,
        "chunk_size": 3000,
        "dimensions": 3072,
    },
    "text-embedding-3-small": {
        "provider": "openai",
        "max_tokens": 8191,
        "chunk_size": 2000,
        "dimensions": 1536,
    },
    "bge-m3": {
        "provider": "ollama",
        "max_tokens": 2048,
        "chunk_size": 1000,
        "dimensions": 1024,
    },
}

if EMBEDDING_MODEL not in MODEL_CONFIGS:
    raise ValueError(f"Model {EMBEDDING_MODEL} not found in MODEL_CONFIGS")

ACTIVE_CONFIG = MODEL_CONFIGS[EMBEDDING_MODEL]