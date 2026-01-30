from backend.services.embeddings import embed_query, embed_texts
from backend.vectorstore.db import similarity_search
from backend.services.keyword_search import keyword_search
from backend.services.reranker import rerank


def retrieve(query: str, k: int = 5) -> list[str]:
    """
    Hybrid retrieval:
    Dense search + keyword search + reranking
    """

    # Dense retrieval
    query_vec = embed_query(query)
    dense_results = similarity_search(query_vec, k=k)

    # Keyword retrieval
    keyword_results = keyword_search(query, dense_results, k=k)

    # Fuse results
    combined = list(dict.fromkeys(dense_results + keyword_results))

    # Rerank
    chunk_embeddings = embed_texts(combined)
    ranked = rerank(query_vec, combined, chunk_embeddings)

    return ranked[:k]
