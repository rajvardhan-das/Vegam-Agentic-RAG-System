from backend.services.reranker import rerank
from backend.services.embeddings import embed_texts, embed_query

query = "Where is Paris?"

chunks = [
    "Paris is in France",
    "Apple is a fruit",
    "Car is a vehicle"
]

query_vec = embed_query(query)
chunk_embeddings = embed_texts(chunks)

ranked = rerank(query_vec, chunks, chunk_embeddings)
print(ranked)
