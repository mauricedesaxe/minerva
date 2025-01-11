from typing import List

def split_text(text: str, max_chunk_size: int = 1000) -> List[str]:
    """Split text using hierarchical chunking strategy.
    
    Main entry point for text splitting. Uses a hierarchical approach:
    1. Split by headings
    2. Split by paragraphs if needed
    3. Split by sentences if needed
    4. Split by words as last resort
    
    Args:
        text: Text content to split
        max_chunk_size: Maximum size for each chunk (default: 1000)
        
    Returns:
        List[str]: List of text chunks
    """
    return split_by_headings(text, max_chunk_size)

def split_by_headings(text: str, max_size: int) -> List[str]:
    """Split text by markdown headings (Level 1).
    
    Args:
        text: Text content to split
        max_size: Maximum size for each chunk
        
    Returns:
        List[str]: List of text chunks split by headings
    """
    sections = []
    current_section_lines = []
    
    for line in text.splitlines():
        if line.startswith('#'):
            if current_section_lines:
                section = '\n'.join(current_section_lines).strip()
                if section:
                    is_small_enough = len(section) <= max_size
                    if is_small_enough:
                        sections.append(section)
                    else:
                        sections.extend(split_by_paragraphs(section, max_size))
            current_section_lines = [line]
        else:
            current_section_lines.append(line)
    
    # Handle last section
    if current_section_lines:
        section = '\n'.join(current_section_lines).strip()
        if section:
            is_small_enough = len(section) <= max_size
            if is_small_enough:
                sections.append(section)
            else:
                sections.extend(split_by_paragraphs(section, max_size))
    
    return [s for s in sections if s.strip()]

def split_by_paragraphs(text: str, max_size: int) -> List[str]:
    """Split text by paragraphs (Level 2).
    
    Args:
        text: Text content to split
        max_size: Maximum size for each chunk
        
    Returns:
        List[str]: List of text chunks split by paragraphs
    """
    paragraphs = [p.strip() for p in text.split('\n\n')]
    paragraphs = [p for p in paragraphs if p]
    chunks = []
    
    for para in paragraphs:
        is_small_enough = len(para) <= max_size
        if is_small_enough:
            chunks.append(para)
        else:
            chunks.extend(split_by_sentences(para, max_size))
    
    return chunks

def split_by_sentences(text: str, max_size: int) -> List[str]:
    """Split text by sentences (Level 3).
    
    Args:
        text: Text content to split
        max_size: Maximum size for each chunk
        
    Returns:
        List[str]: List of text chunks split by sentences
    """
    sentence_boundaries = ['. ', '! ', '? ', '...', '.\n', '!\n', '?\n']
    current_sentence = ""
    sentences = []
    
    for char in text:
        current_sentence += char
        
        is_sentence_boundary = any(current_sentence.endswith(end) for end in sentence_boundaries)
        if is_sentence_boundary:
            is_small_enough = len(current_sentence) <= max_size
            if is_small_enough:
                sentences.append(current_sentence)
            else:
                sentences.extend(split_at_word_boundaries(current_sentence, max_size))
            current_sentence = ""
    
    if current_sentence:  # Handle any remaining text
        is_small_enough = len(current_sentence) <= max_size
        if is_small_enough:
            sentences.append(current_sentence)
        else:
            sentences.extend(split_at_word_boundaries(current_sentence, max_size))
    
    return sentences

def split_at_word_boundaries(text: str, max_size: int) -> List[str]:
    """Split text at word boundaries as last resort (Level 4).
    
    Args:
        text: Text content to split
        max_size: Maximum size for each chunk
        
    Returns:
        List[str]: List of text chunks split by word boundaries
    """
    chunks = []
    current_chunk = ""
    words = text.split()
    
    for word in words:
        is_small_enough = len(current_chunk) + len(word) + 1 <= max_size
        if is_small_enough:
            current_chunk += word + " "
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = word + " "
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks