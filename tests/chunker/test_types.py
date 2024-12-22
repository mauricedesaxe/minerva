import pytest
from datetime import datetime

from minerva.chunker.types import Chunk, DenseChunk, SparseChunk

def test_base_chunk_initialization():
    """Test basic Chunk initialization."""
    chunk = Chunk(
        text="Test content",
        start_line=1,
        end_line=2,
        source_id="test-doc",
        metadata={"type": "test"}
    )
    
    assert chunk.text == "Test content"
    assert chunk.start_line == 1
    assert chunk.end_line == 2
    assert chunk.source_id == "test-doc"
    assert chunk.metadata == {"type": "test"}
    assert isinstance(chunk.created_at, datetime)
    assert chunk.parent_id is None
    assert chunk.child_ids == []

def test_chunk_post_init():
    """Test Chunk post_init behavior with None child_ids."""
    chunk = Chunk(
        text="Test content",
        start_line=1,
        end_line=2,
        source_id="test-doc",
        metadata={},
        child_ids=None
    )
    
    assert chunk.child_ids == []

def test_chunk_with_relationships():
    """Test Chunk with parent-child relationships."""
    parent_id = "parent123"
    child_ids = ["child1", "child2"]
    
    chunk = Chunk(
        text="Test content",
        start_line=1,
        end_line=2,
        source_id="test-doc",
        metadata={},
        parent_id=parent_id,
        child_ids=child_ids
    )
    
    assert chunk.parent_id == parent_id
    assert chunk.child_ids == child_ids

def test_dense_chunk_initialization():
    """Test DenseChunk initialization."""
    chunk = DenseChunk(
        text="Test content",
        start_line=1,
        end_line=2,
        source_id="test-doc",
        metadata={},
        token_count=10,
        overlap_next=5
    )
    
    assert chunk.token_count == 10
    assert chunk.overlap_next == 5
    assert isinstance(chunk, Chunk)  # Verify inheritance

def test_dense_chunk_defaults():
    """Test DenseChunk default values."""
    chunk = DenseChunk(
        text="Test content",
        start_line=1,
        end_line=2,
        source_id="test-doc",
        metadata={},
        token_count=10
    )
    
    assert chunk.overlap_next is None

def test_sparse_chunk_initialization():
    """Test SparseChunk initialization."""
    chunk = SparseChunk(
        text="Test content",
        start_line=1,
        end_line=2,
        source_id="test-doc",
        metadata={},
        hierarchy_level=1,
        heading="Test Section"
    )
    
    assert chunk.hierarchy_level == 1
    assert chunk.heading == "Test Section"
    assert isinstance(chunk, Chunk)  # Verify inheritance

def test_sparse_chunk_defaults():
    """Test SparseChunk default values."""
    chunk = SparseChunk(
        text="Test content",
        start_line=1,
        end_line=2,
        source_id="test-doc",
        metadata={},
        hierarchy_level=0
    )
    
    assert chunk.heading is None

def test_metadata_immutability():
    """Test that metadata dict is properly copied."""
    metadata = {"key": "value"}
    chunk = Chunk(
        text="Test content",
        start_line=1,
        end_line=2,
        source_id="test-doc",
        metadata=metadata
    )
    
    # Modify original metadata
    metadata["key"] = "new_value"
    
    # Chunk's metadata should be unchanged
    assert chunk.metadata["key"] == "value"

def test_invalid_line_numbers():
    """Test chunk creation with invalid line numbers."""
    with pytest.raises(ValueError, match="end_line must be >= start_line"):
        Chunk(
            text="Test content",
            start_line=2,  # Start line greater than end line
            end_line=1,
            source_id="test-doc",
            metadata={}
        )
        
    with pytest.raises(ValueError, match="start_line must be >= 1"):
        Chunk(
            text="Test content",
            start_line=0,  # Invalid start line
            end_line=1,
            source_id="test-doc",
            metadata={}
        )

def test_empty_text():
    """Test chunk creation with empty text."""
    with pytest.raises(ValueError, match="Chunk text cannot be empty"):
        Chunk(
            text="",
            start_line=1,
            end_line=1,
            source_id="test-doc",
            metadata={}
        )
        
    with pytest.raises(ValueError, match="Chunk text cannot be empty"):
        Chunk(
            text="   ",  # Only whitespace
            start_line=1,
            end_line=1,
            source_id="test-doc",
            metadata={}
        )

def test_dense_chunk_validation():
    """Test DenseChunk validation rules."""
    # Test invalid token count
    with pytest.raises(ValueError, match="token_count must be >= 1"):
        DenseChunk(
            text="Test content",
            start_line=1,
            end_line=2,
            source_id="test-doc",
            metadata={},
            token_count=0
        )
        
    # Test invalid overlap
    with pytest.raises(ValueError, match="overlap_next must be >= 0"):
        DenseChunk(
            text="Test content",
            start_line=1,
            end_line=2,
            source_id="test-doc",
            metadata={},
            token_count=10,
            overlap_next=-1
        )

def test_sparse_chunk_validation():
    """Test SparseChunk validation rules."""
    # Test invalid hierarchy level
    with pytest.raises(ValueError, match="hierarchy_level must be >= 0"):
        SparseChunk(
            text="Test content",
            start_line=1,
            end_line=2,
            source_id="test-doc",
            metadata={},
            hierarchy_level=-1
        )
        
    # Test valid hierarchy levels
    for level in range(5):  # Test levels 0-4
        chunk = SparseChunk(
            text="Test content",
            start_line=1,
            end_line=2,
            source_id="test-doc",
            metadata={},
            hierarchy_level=level
        )
        assert chunk.hierarchy_level == level 