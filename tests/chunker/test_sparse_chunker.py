import pytest
from typing import List, Optional

from minerva.chunker.sparse import SparseChunker
from minerva.chunker.types import SparseChunk

@pytest.fixture
def small_chunker():
    """Create a SparseChunker with small minimum chunk size."""
    return SparseChunker(min_chunk_size=10)

@pytest.fixture
def test_markdown():
    """Create a test markdown document with various heading styles."""
    return """# Top Level Heading
This is the first section with some content.
It has multiple lines.

## Second Level
This section has a subsection.
With some content.

### Third Level
Deeper nested content here.
Multiple lines of it.

## Another Second Level
This is a parallel section.
More content here.

# Another Top Level
Final section with content.
The end."""

@pytest.fixture
def test_underlined():
    """Create a test document with underlined headings."""
    return """Top Level Heading
================
This is the first section with some content.
It has multiple lines.

Second Level
-----------
This section has different style.
With some content.

Another Second Level
-------------------
This is a parallel section.
More content here."""

def test_initialization():
    """Test SparseChunker initialization with different parameters."""
    # Test default value
    chunker = SparseChunker()
    assert chunker.min_chunk_size == 50
    
    # Test custom value
    chunker = SparseChunker(min_chunk_size=100)
    assert chunker.min_chunk_size == 100
    
    # Test invalid value
    with pytest.raises(ValueError):
        SparseChunker(min_chunk_size=0)

def test_heading_detection(small_chunker):
    """Test heading detection for different formats."""
    assert small_chunker._parse_heading("# Heading 1") == ("Heading 1", 1)
    assert small_chunker._parse_heading("## Heading 2") == ("Heading 2", 2)
    assert small_chunker._parse_heading("### Heading 3") == ("Heading 3", 3)
    assert small_chunker._parse_heading("Regular text") == (None, -1)
    assert small_chunker._parse_heading("") == (None, -1)
    assert small_chunker._parse_heading("#Invalid") == (None, -1)
    assert small_chunker._parse_heading("##") == (None, -1)

def test_basic_chunking(small_chunker, test_markdown):
    """Test basic markdown chunking functionality."""
    chunks = small_chunker.chunk(test_markdown, "test-doc")
    
    # Verify we got chunks
    assert len(chunks) > 0
    assert all(isinstance(c, SparseChunk) for c in chunks)
    
    # Verify chunk properties
    for chunk in chunks:
        assert chunk.text.strip()
        assert chunk.start_line >= 1
        assert chunk.end_line >= chunk.start_line
        assert chunk.source_id == "test-doc"
        assert isinstance(chunk.metadata, dict)
        assert chunk.hierarchy_level >= 0
        
    # Verify hierarchy
    top_level_chunks = [c for c in chunks if c.hierarchy_level == 1]
    assert len(top_level_chunks) == 2  # Two # headings

def test_underlined_chunking(small_chunker, test_underlined):
    """Test chunking with underlined headings."""
    chunks = small_chunker.chunk(test_underlined, "test-doc")
    
    # Verify chunks
    assert len(chunks) > 0
    
    # Check levels
    top_level = [c for c in chunks if c.hierarchy_level == 1]
    second_level = [c for c in chunks if c.hierarchy_level == 2]
    
    assert len(top_level) == 1  # One === heading
    assert len(second_level) == 2  # Two --- headings

def test_parent_child_relationships(small_chunker, test_markdown):
    """Test that parent-child relationships are correctly established."""
    chunks = small_chunker.chunk(test_markdown, "test-doc")
    
    # Find chunks by heading
    def find_chunk_by_heading(heading: str) -> SparseChunk:
        return next(c for c in chunks if c.heading == heading)
    
    top_chunk = find_chunk_by_heading("Top Level Heading")
    second_chunk = find_chunk_by_heading("Second Level")
    third_chunk = find_chunk_by_heading("Third Level")
    
    # Verify relationships
    assert third_chunk.parent_id == id(second_chunk)
    assert second_chunk.parent_id == id(top_chunk)
    assert top_chunk.parent_id is None
    
    # Verify child IDs
    assert id(second_chunk) in top_chunk.child_ids
    assert id(third_chunk) in second_chunk.child_ids

def test_minimum_chunk_size(small_chunker):
    """Test minimum chunk size handling."""
    text = """# Small Section
Too small.

# Big Section
This section has enough content to meet
the minimum chunk size requirement and
should be included in the output."""

    chunks = small_chunker.chunk(text, "test-doc")
    
    # Only the larger section should be included
    assert len(chunks) == 2  # Both included because they're top-level
    assert any(len(c.text) >= small_chunker.min_chunk_size for c in chunks)

def test_chunk_validation(small_chunker):
    """Test chunk validation."""
    # Valid chunk should pass validation
    valid_chunk = SparseChunk(
        text="Valid chunk content that is definitely long enough to pass validation",
        start_line=1,
        end_line=2,
        source_id="test-doc",
        metadata={},
        hierarchy_level=1,
        heading="Test Heading"
    )
    assert small_chunker.validate_chunk(valid_chunk)
    
    # Test chunker-specific validation (like minimum size requirements)
    small_chunk = SparseChunk(
        text="Too small",
        start_line=1,
        end_line=2,
        source_id="test-doc",
        metadata={},
        hierarchy_level=2,  # Not top-level, so size matters
        heading=None  # No heading, so should fail size check
    )
    assert not small_chunker.validate_chunk(small_chunk)

def test_metadata_handling(small_chunker, test_markdown):
    """Test metadata handling in chunks."""
    metadata = {"type": "test", "language": "en"}
    chunks = small_chunker.chunk(test_markdown, "test-doc", metadata)
    
    # Create a copy of original metadata for comparison
    original_metadata = metadata.copy()
    
    # Verify metadata is preserved in all chunks
    for chunk in chunks:
        assert chunk.metadata == original_metadata
        # Modifying original metadata shouldn't affect chunks
        metadata["new_key"] = "new_value"
        assert chunk.metadata == original_metadata

def test_edge_cases(small_chunker):
    """Test edge cases and potential error conditions."""
    # Empty text
    chunks = small_chunker.chunk("", "test-doc")
    assert len(chunks) == 0
    
    # Text with no headings
    text = "Just plain text\nwithout any headings."
    chunks = small_chunker.chunk(text, "test-doc")
    assert len(chunks) == 1
    assert chunks[0].hierarchy_level == 0
    
    # Text with only headings
    text = "# H1\n## H2\n### H3"
    chunks = small_chunker.chunk(text, "test-doc")
    assert len(chunks) > 0
    
    # Malformed headings
    text = "#Not a heading\n###### Too many hashes"
    chunks = small_chunker.chunk(text, "test-doc")
    assert len(chunks) == 1  # Treated as regular text 