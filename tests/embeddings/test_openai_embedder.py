import pytest
from datetime import datetime
from unittest.mock import Mock, patch

from minerva.chunker.types import Chunk
from minerva.embeddings.openai import OpenAIEmbedder
from minerva.embeddings.types import Embedding
from minerva.embeddings.exceptions import EmbeddingGenerationError

@pytest.fixture
def mock_openai_response():
    """Create a mock OpenAI API response."""
    class MockEmbedding:
        def __init__(self):
            self.embedding = [0.1] * 3072  # text-embedding-3-large dimension
    
    class MockResponse:
        def __init__(self):
            self.data = [MockEmbedding()]
    
    return MockResponse()

@pytest.fixture
def test_chunk():
    """Create a test chunk."""
    return Chunk(
        text="This is a test chunk",
        start_line=1,
        end_line=2,
        source_id="test-doc",
        metadata={"type": "test"}
    )

@pytest.fixture
def embedder():
    """Create an OpenAIEmbedder instance."""
    with patch('minerva.embeddings.openai.get_config') as mock_config:
        mock_config.return_value.openai_api_key = "test-key"
        return OpenAIEmbedder()

def test_initialization():
    """Test OpenAIEmbedder initialization."""
    with patch('minerva.embeddings.openai.get_config') as mock_config:
        # Test successful initialization
        mock_config.return_value.openai_api_key = "test-key"
        embedder = OpenAIEmbedder()
        assert embedder.model == "text-embedding-3-large"
        
        # Test missing API key
        mock_config.return_value.openai_api_key = None
        with pytest.raises(ValueError):
            OpenAIEmbedder()

def test_embed(embedder, test_chunk, mock_openai_response):
    """Test embedding generation."""
    with patch.object(embedder.client.embeddings, 'create') as mock_create:
        mock_create.return_value = mock_openai_response
        
        # Test successful embedding
        embedding = embedder.embed(test_chunk)
        assert isinstance(embedding, Embedding)
        assert embedding.text == test_chunk.text
        assert len(embedding.vector) == 3072
        assert embedding.model == embedder.model
        assert embedding.source_id == test_chunk.source_id
        assert embedding.metadata == test_chunk.metadata
        
        # Test API error
        mock_create.side_effect = Exception("API Error")
        with pytest.raises(EmbeddingGenerationError):
            embedder.embed(test_chunk)

def test_validate_embedding(embedder):
    """Test embedding validation."""
    # Create valid embedding
    valid_embedding = Embedding(
        text="Test text",
        vector=[0.1] * 3072,  # Correct dimension
        model="text-embedding-3-large",
        source_id="test",
        metadata={},
        start_line=1,
        end_line=2
    )
    assert embedder.validate_embedding(valid_embedding)
    
    # Test invalid cases by modifying valid embedding
    # Wrong vector dimension
    invalid_embedding = Embedding(
        text="Test text",
        vector=[0.1] * 100,  # Wrong dimension
        model="text-embedding-3-large",
        source_id="test",
        metadata={},
        start_line=1,
        end_line=2
    )
    assert not embedder.validate_embedding(invalid_embedding)
    
    # Wrong model
    invalid_embedding = Embedding(
        text="Test text",
        vector=[0.1] * 3072,
        model="wrong-model",
        source_id="test",
        metadata={},
        start_line=1,
        end_line=2
    )
    assert not embedder.validate_embedding(invalid_embedding) 