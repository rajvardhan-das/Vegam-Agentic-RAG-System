from backend.ingest.loader import load_document
from backend.ingest.cleaner import clean_text
from backend.ingest.chunker import recursive_chunk_text
from backend.services.embeddings import embed_texts
from backend.vectorstore.db import add_documents


def ingest_file(file_path: str):
    """
    Full ingestion pipeline:
    load -> clean -> chunk -> embed -> store
    """

    # 1. Load
    text = load_document(file_path)

    # 2. Clean
    text = clean_text(text)

    # 3. Chunk
    chunks = recursive_chunk_text(text)

    # 4. Embed
    embeddings = embed_texts(chunks)

    # 5. Store
    add_documents(chunks, embeddings)

    return len(chunks)
