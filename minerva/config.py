from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class MinervaConfig(BaseSettings):
    """Base configuration for Minerva, loaded from environment variables."""
    
    # OpenAI settings
    openai_api_key: Optional[str] = None
    
    # AWS settings
    aws_access_key_id: Optional[str] = None
    aws_secret_access_key: Optional[str] = None
    
    # Database settings
    postgres_dsn: Optional[str] = None
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )
    
    def model_post_init(self, _) -> None:
        """Validate that all required fields are set."""
        missing_fields = []
        required_fields = [
            ('openai_api_key', self.openai_api_key),
            ('aws_access_key_id', self.aws_access_key_id),
            ('aws_secret_access_key', self.aws_secret_access_key),
            ('postgres_dsn', self.postgres_dsn)
        ]
        
        for field_name, value in required_fields:
            if value is None:
                missing_fields.append(field_name)
        
        if missing_fields:
            raise ValueError(f"Missing required configuration values: {', '.join(missing_fields)}")

def get_config() -> MinervaConfig:
    """Load and return the configuration."""
    try:
        return MinervaConfig()
    except Exception as e:
        raise RuntimeError(f"Failed to load configuration: {str(e)}")