def build_context(chunks: list[str], max_chars: int = 3000) -> str:
    """
    Combine retrieved chunks into a single context string.
    Truncate if exceeds max_chars.
    """

    context = ""
    for chunk in chunks:
        if len(context) + len(chunk) <= max_chars:
            context += chunk + "\n\n"
        else:
            break

    return context.strip()
