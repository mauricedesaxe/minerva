from datetime import datetime
import pytest

from minerva.parser.markdown import MarkdownParser
from minerva.parser.types import ParsedDocument

def test_parse_simple_markdown():
    parser = MarkdownParser()
    content = b"# Test Document\n\nThis is a test paragraph."
    
    result = parser.parse(
        content=content,
        content_type="text/markdown",
        source_id="test-doc"
    )
    
    assert isinstance(result, ParsedDocument)
    assert result.text == "# Test Document\n\nThis is a test paragraph."
    assert result.title == "Test Document"
    assert result.content_type == "text/markdown"
    assert result.size == len(content)
    assert isinstance(result.parsed_at, datetime)

def test_parse_complex_markdown():
    parser = MarkdownParser()
    content = b"""# Main Title
    
## Section 1
This is *emphasized* and this is **bold**.

[Link text](http://example.com)
![Image](image.jpg)

* List item 1
* List item 2
    """
    
    result = parser.parse(
        content=content,
        content_type="text/markdown",
        source_id="test-doc",
        metadata={"source": "test"}
    )
    
    expected_text = content.decode('utf-8')
    
    assert result.text == expected_text
    assert result.title == "Main Title"
    assert result.metadata == {"source": "test"}

def test_parse_invalid_encoding():
    parser = MarkdownParser()
    content = b"\xFF\xFE Invalid UTF-8 bytes"
    
    with pytest.raises(UnicodeDecodeError):
        parser.parse(
            content=content,
            content_type="text/markdown",
            source_id="test-doc"
        )

def test_parse_empty_document():
    parser = MarkdownParser()
    content = b""
    
    result = parser.parse(
        content=content,
        content_type="text/markdown",
        source_id="test-doc"
    )
    
    assert result.text == ""
    assert result.title is None
    assert result.size == 0

def test_parse_nested_lists():
    parser = MarkdownParser()
    content = b"""# Lists Test
    
* Level 1
    * Level 2
        * Level 3
    * Back to level 2
* Back to level 1

1. Ordered 1
    * Unordered in ordered
    * Another one
2. Ordered 2"""
    
    result = parser.parse(
        content=content,
        content_type="text/markdown",
        source_id="test-doc"
    )
    
    assert result.text == content.decode('utf-8')
    assert result.title == "Lists Test"

def test_parse_code_blocks():
    parser = MarkdownParser()
    content = b"""# Code Test
    
Here is `inline code` and here's a block:

```python
def hello():
    print("world")
```

And another:

    Indented code block
    should work too"""
    
    result = parser.parse(
        content=content,
        content_type="text/markdown",
        source_id="test-doc"
    )
    
    assert result.text == content.decode('utf-8')
    assert result.title == "Code Test"

def test_parse_tables():
    parser = MarkdownParser()
    content = b"""# Table Test
    
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |"""
    
    result = parser.parse(
        content=content,
        content_type="text/markdown",
        source_id="test-doc"
    )
    
    assert result.text == content.decode('utf-8')
    assert result.title == "Table Test"

def test_parse_special_characters():
    parser = MarkdownParser()
    content = """# Special Characters
    
HTML entities: &copy; &amp; &lt; &gt;
Escaped chars: \\* \\_ \\` \\# \\[
Unicode: 你好 • é ñ 🌟""".encode('utf-8')
    
    result = parser.parse(
        content=content,
        content_type="text/markdown",
        source_id="test-doc"
    )
    
    assert result.text == content.decode('utf-8')
    assert result.title == "Special Characters"
    # Additional checks for special characters
    assert "&copy;" in result.text
    assert "\\*" in result.text
    assert "你好" in result.text
    assert "🌟" in result.text

def test_parse_long_document():
    parser = MarkdownParser()
    # Create a long document with repeated markdown content
    base_content = b"## Section\n\nThis is a test paragraph with *emphasis* and **bold**.\n\n"
    content = b"# Long Document\n\n" + base_content * 1000
    
    result = parser.parse(
        content=content,
        content_type="text/markdown",
        source_id="test-doc"
    )
    
    assert result.title == "Long Document"
    assert "## Section" in result.text
    assert "*emphasis*" in result.text
    assert "**bold**" in result.text
    assert result.size == len(content)

def test_parse_multiple_newlines():
    parser = MarkdownParser()
    content = b"""# Multiple Newlines



Between these lines



Should be normalized"""
    
    result = parser.parse(
        content=content,
        content_type="text/markdown",
        source_id="test-doc"
    )
    
    assert result.text == content.decode('utf-8')
    assert result.title == "Multiple Newlines"

def test_parse_complex_metadata():
    parser = MarkdownParser()
    metadata = {
        "author": "Test Author",
        "created_at": "2023-01-01",
        "tags": ["test", "markdown"],
        "version": 1,
        "is_draft": True
    }
    
    content = b"""# Metadata Test
This is a paragraph with *markdown* formatting."""
    
    result = parser.parse(
        content=content,
        content_type="text/markdown",
        source_id="test-doc",
        metadata=metadata
    )
    
    assert result.text.strip() == "# Metadata Test\nThis is a paragraph with *markdown* formatting."
    assert result.metadata == metadata
    assert result.metadata["author"] == "Test Author"
    assert result.metadata["tags"] == ["test", "markdown"]

def test_invalid_content_type():
    parser = MarkdownParser()
    content = b"# Test\nContent"
    
    with pytest.raises(ValueError):
        parser.parse(
            content=content,
            content_type="invalid/type",
            source_id="test-doc"
        )

def test_content_type_case_sensitivity():
    parser = MarkdownParser()
    content = b"""# Test
Content with *markdown* formatting"""
    
    # Both of these should work
    result1 = parser.parse(
        content=content,
        content_type="text/markdown",
        source_id="test-doc"
    )
    
    result2 = parser.parse(
        content=content,
        content_type="TEXT/MARKDOWN",
        source_id="test-doc"
    )
    
    assert result1.text == result2.text
    assert "*markdown*" in result1.text