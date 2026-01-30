from backend.services.embeddings import embed_texts, embed_query

texts = ["Hello world", "Machine learning is cool"]
vectors = embed_texts(texts)

print("Num vectors:", len(vectors))
print("Vector length:", len(vectors[0]))

q = embed_query("What is ML?")
print("Query vector length:", len(q))
