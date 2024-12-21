import pytest
from dotenv import load_dotenv
import os
from minerva.config import MinervaConfig

def test_config_loads_from_env():
    # Load environment variables from .env file
    load_dotenv()
    
    # Load config
    config = MinervaConfig()
    
    # Verify all values loaded correctly
    assert config.openai_api_key == os.getenv("OPENAI_API_KEY")
    assert config.aws_access_key_id == os.getenv("AWS_ACCESS_KEY_ID")
    assert config.aws_secret_access_key == os.getenv("AWS_SECRET_ACCESS_KEY")
    assert config.postgres_dsn == os.getenv("POSTGRES_DSN")
