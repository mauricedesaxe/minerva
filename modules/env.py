import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables from .env file
load_dotenv()

def get_required_env(key: str) -> str:
    """Get required environment variable or raise error."""
    value = os.getenv(key)
    if not value:
        raise ValueError(f"Required environment variable {key} not set")
    return value

def get_optional_env(key: str, default: Optional[str] = None) -> Optional[str]:
    """Get optional environment variable with default."""
    return os.getenv(key, default)

# Required environment variables
EMBEDDING_MODEL = get_required_env("EMBEDDING_MODEL")
AWS_ACCESS_KEY_ID = get_required_env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = get_required_env("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = get_required_env("BUCKET_NAME")

# Optional environment variables
OPENAI_API_KEY = get_optional_env("OPENAI_API_KEY")
OLLAMA_URL = get_optional_env("OLLAMA_URL", "http://localhost:11434")
API_KEY = get_optional_env("API_KEY")
STORAGE_URL = get_optional_env("STORAGE_URL")
LOG_LEVEL = get_optional_env("LOG_LEVEL", "DEBUG")