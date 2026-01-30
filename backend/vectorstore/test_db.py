from backend.vectorstore.db import add_documents, similarity_search, reset_collection
from backend.services.embeddings import embed_texts, embed_query

reset_collection()   # <-- add this

texts = [
    "Apple is a fruit",
    "Car is a vehicle",
    "Paris is in France"
]

embeddings = embed_texts(texts)
add_documents(texts, embeddings)

query_vec = embed_query("What is apple?")
results = similarity_search(query_vec)

print(results)
