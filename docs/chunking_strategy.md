# Document Chunking Strategy

## Overview

This document outlines the hierarchical chunking strategy for splitting documents into embeddings-friendly chunks while preserving as much natural structure as possible.

## Goals

- Preserve document structure where possible
- Create semantically meaningful chunks
- Ensure chunks don't exceed max token/character limits
- Keep implementation simple and maintainable
- No configuration required from users

## Chunking Hierarchy

The system attempts to split documents using increasingly granular boundaries, only moving to the next level when necessary:

### 1. Markdown Headings

- Split at all heading markers (# ## ###)
- Each section becomes its own chunk
- If any section exceeds max_size, that section moves to level 2
- Other valid-size sections remain as-is

### 2. Paragraphs

- Split oversized sections at paragraph boundaries (\n\n)
- Each paragraph becomes its own chunk
- If any paragraph exceeds max_size, that paragraph moves to level 3
- Other valid-size paragraphs remain as-is

### 3. Sentences

- Split oversized paragraphs at sentence boundaries (. ! ?)
- Each sentence becomes its own chunk
- If any sentence exceeds max_size, that sentence moves to level 4
- Other valid-size sentences remain as-is

### 4. Word Boundaries (Last Resort)

- For any text still exceeding max_size
- Find nearest word boundary (space) to max_size position
- Create chunk up to that boundary
- Repeat for remaining text
- Unlike other levels, does NOT split at EVERY word boundary

## Example

Given text:

```
# Section 1
Small paragraph here.

# Section 2
Very long paragraph that exceeds max_size...

# Section 3
Short sentence 1. Very very very long sentence that exceeds max_size...
```

Will result in:
1. `”# Section 1\nSmall paragraph here."` (Level 1)
2. `”# Section 2\n[chunk 1 of long paragraph]", "# Section 2\n[chunk 2 of long paragraph]"` (Level 4)
3. `”# Section 3\nShort sentence 1.", "# Section 3\n[chunk 1 of long sentence]"` (Level 3/4)

## Future Considerations
- Special handling of code blocks
- Streaming for large files
- Memory optimization
- Performance improvements

## Usage
```python
chunks = split_text(content, max_chunk_size=1000)
```
```

This design doc:
- Explains the strategy clearly
- Shows how each level works
- Provides concrete examples
- Documents future considerations
- Follows Grug rules (simple, clear, practical)

Want to implement this strategy now?
