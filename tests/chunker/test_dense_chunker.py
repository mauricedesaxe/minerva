import pytest
import tiktoken
from typing import List

from minerva.chunker.dense import DenseChunker
from minerva.chunker.types import DenseChunk

@pytest.fixture
def chunker():
    """Create a DenseChunker with default settings."""
    return DenseChunker()

@pytest.fixture
def small_chunker():
    """Create a DenseChunker with small chunk size for testing."""
    return DenseChunker(chunk_size=10, chunk_overlap=3, max_sentences=2)

@pytest.fixture
def test_text():
    """Create a test text with multiple sentences."""
    return (
        "This is the first sentence. This is the second sentence with more words. "
        "Here comes the third sentence. And a fourth one here. "
        "Finally, the fifth sentence ends this paragraph."
    )

def test_initialization():
    """Test DenseChunker initialization with different parameters."""
    # Test default values
    chunker = DenseChunker()
    assert chunker.chunk_size == 512
    assert chunker.chunk_overlap == 128
    assert isinstance(chunker.tokenizer, tiktoken.Encoding)
    
    # Test custom values
    chunker = DenseChunker(chunk_size=256, chunk_overlap=64)
    assert chunker.chunk_size == 256
    assert chunker.chunk_overlap == 64
    
    # Test invalid values
    with pytest.raises(ValueError):
        DenseChunker(chunk_size=0)
    with pytest.raises(ValueError):
        DenseChunker(chunk_overlap=-1)
    with pytest.raises(ValueError):
        DenseChunker(chunk_size=100, chunk_overlap=200)  # Overlap > size

def test_token_counting(chunker):
    """Test token counting functionality."""
    # Test empty string
    assert chunker._count_tokens("") == 0
    
    # Test simple string
    text = "This is a test."
    token_count = chunker._count_tokens(text)
    assert token_count > 0
    assert isinstance(token_count, int)
    
    # Test string with special characters
    text = "This is a test with special chars: !@#$%^&*()"
    token_count = chunker._count_tokens(text)
    assert token_count > 0
    
    # Test string with numbers
    text = "123 456 789"
    token_count = chunker._count_tokens(text)
    assert token_count > 0

def test_sentence_splitting(chunker):
    """Test sentence splitting functionality."""
    # Test basic sentence splitting
    text = "First sentence. Second sentence! Third sentence?"
    sentences = chunker._split_into_sentences(text)
    assert len(sentences) == 3
    assert sentences[0] == "First sentence"
    
    # Test with multiple punctuation marks
    text = "What?! No way... But maybe!!!"
    sentences = chunker._split_into_sentences(text)
    assert len(sentences) > 0
    
    # Test with newlines
    text = "First line.\nSecond line.\nThird line."
    sentences = chunker._split_into_sentences(text)
    assert len(sentences) == 3
    
    # Test with abbreviations (current implementation might split these)
    text = "Dr. Smith went to St. Mary's Hospital."
    sentences = chunker._split_into_sentences(text)
    assert len(sentences) > 0

def test_basic_chunking(chunker, test_text):
    """Test basic text chunking functionality."""
    chunks = chunker.chunk(test_text, "test-doc")
    
    # Verify we got some chunks
    assert len(chunks) > 0
    assert all(isinstance(c, DenseChunk) for c in chunks)
    
    # Verify chunk properties
    for chunk in chunks:
        assert chunk.text.strip()
        assert chunk.start_line >= 1
        assert chunk.end_line >= chunk.start_line
        assert chunk.source_id == "test-doc"
        assert chunk.token_count > 0
        
    # Verify overlaps
    for i in range(len(chunks) - 1):
        assert chunks[i].overlap_next is not None
        assert 0 <= chunks[i].overlap_next <= chunker.chunk_overlap

def test_small_chunks(small_chunker):
    """Test chunking with small chunk size."""
    text = "One. Two. Three. Four. Five."
    chunks = small_chunker.chunk(text, "test-doc")
    
    # Should get multiple small chunks
    assert len(chunks) > 1
    
    # Verify each chunk is within size limit
    for chunk in chunks:
        assert chunk.token_count <= small_chunker.chunk_size

def test_chunk_validation(chunker, test_text):
    """Test chunk validation."""
    chunks = chunker.chunk(test_text, "test-doc")
    
    # All generated chunks should be valid
    assert all(chunker.validate_chunk(c) for c in chunks)
    
    # Test invalid chunks
    invalid_chunk = DenseChunk(
        text="Test",
        start_line=1,
        end_line=1,
        source_id="test-doc",
        metadata={},
        token_count=100  # Incorrect token count
    )
    assert not chunker.validate_chunk(invalid_chunk)

def test_metadata_handling(chunker):
    """Test metadata handling in chunks."""
    metadata = {"type": "test", "language": "en"}
    chunks = chunker.chunk("Test sentence one. Test sentence two.", "test-doc", metadata)
    
    # Verify metadata is preserved in all chunks
    for chunk in chunks:
        assert chunk.metadata == metadata
        # Modifying the original metadata shouldn't affect chunks
        metadata["new_key"] = "new_value"
        assert "new_key" not in chunk.metadata

def test_edge_cases(chunker):
    """Test edge cases and potential error conditions."""
    # Empty text
    with pytest.raises(ValueError):
        chunker.chunk("", "test-doc")
    
    # Whitespace only
    with pytest.raises(ValueError):
        chunker.chunk("   \n   ", "test-doc")
    
    # Single very long sentence
    long_text = "word " * 1000
    chunks = chunker.chunk(long_text, "test-doc")
    assert len(chunks) > 1  # Should split even without sentence boundaries
    
    # Text with no sentence boundaries
    no_boundaries = "word word word"
    chunks = chunker.chunk(no_boundaries, "test-doc")
    assert len(chunks) > 0

def test_line_number_tracking(chunker):
    """Test line number tracking in chunks."""
    text = "Line one.\nLine two.\nLine three.\nLine four.\nLine five."
    chunks = chunker.chunk(text, "test-doc")
    
    # First chunk should start at line 1
    assert chunks[0].start_line == 1
    
    # Last chunk should end at the last line
    assert chunks[-1].end_line == text.count('\n') + 1

def test_overlap_consistency(chunker, test_text):
    """Test that chunk overlaps are consistent."""
    chunks = chunker.chunk(test_text, "test-doc")
    
    for i in range(len(chunks) - 1):
        current_chunk = chunks[i]
        
        # Overlap should never exceed configured overlap
        assert current_chunk.overlap_next <= chunker.chunk_overlap
        
        # Overlap should never exceed chunk sizes
        assert current_chunk.overlap_next <= current_chunk.token_count
        assert current_chunk.overlap_next <= chunks[i + 1].token_count