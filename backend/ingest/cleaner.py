import re


def clean_text(text: str) -> str:
    """
    Basic text cleaning:
    - Remove extra whitespace
    - Remove multiple newlines
    - Normalize spaces
    """

    text = text.replace("\t", " ")
    text = re.sub(r"\n\s*\n", "\n\n", text)   # collapse empty lines
    text = re.sub(r" +", " ", text)           # collapse spaces
    return text.strip()
