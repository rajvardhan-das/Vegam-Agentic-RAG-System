from backend.ingest.chunker import recursive_chunk_text

text = """
Artificial intelligence is transforming the world.

It enables machines to reason, learn, and act.

RAG systems combine retrieval and generation.

This improves factual accuracy.

""" * 20

chunks = recursive_chunk_text(text)

print("Chunks:", len(chunks))
print("\n--- Chunk 1 ---\n", chunks[0][:300])
print("\n--- Chunk 2 ---\n", chunks[1][:300])
