from sentence_transformers import SentenceTransformer

# Load once (global)
_model = SentenceTransformer("all-MiniLM-L6-v2")



def embed_texts(texts: list[str]) -> list[list[float]]:
    """
    Convert list of texts to embeddings.
    """
    embeddings = _model.encode(texts)
    return embeddings.tolist()


def embed_query(text: str) -> list[float]:
    """
    Convert query text to embedding.
    """
    embedding = _model.encode([text])[0]
    return embedding.tolist()
