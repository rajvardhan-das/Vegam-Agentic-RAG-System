import numpy as np


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def rerank(query_embedding, chunks, chunk_embeddings):
    """
    Re-rank retrieved chunks using cosine similarity.

    query_embedding: List[float]
    chunks: List[str]
    chunk_embeddings: List[List[float]]
    """

    scored = []
    for chunk, emb in zip(chunks, chunk_embeddings):
        score = cosine_similarity(query_embedding, emb)
        scored.append((score, chunk))

    scored.sort(reverse=True, key=lambda x: x[0])
    return [c for _, c in scored]
