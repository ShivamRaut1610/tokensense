"""
Prompt chunker - splits long text into token-safe pieces.
"""

def chunk_prompt(text: str, max_tokens: int = 500) -> list:
    """
    Split a long prompt into chunks within the token limit.
    
    Args:
        text: The input string to chunk.
        max_tokens: Maximum tokens per chunk.
    
    Returns:
        List of string chunks.
    """
    # TODO: Implement chunking logic
    raise NotImplementedError("Implement chunking logic")
