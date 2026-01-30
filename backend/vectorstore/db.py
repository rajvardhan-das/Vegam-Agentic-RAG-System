from pymilvus import (
    connections,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
    utility
)

from backend.utils.logger import logger
from backend.utils.exceptions import VectorStoreError

# -----------------------------
# Config
# -----------------------------

COLLECTION_NAME = "documents"
EMBEDDING_DIM = 384


# -----------------------------
# Connect to Milvus
# -----------------------------

try:
    connections.connect(
        alias="default",
        host="localhost",
        port="19530"
    )
    logger.info("Connected to Milvus successfully")
except Exception as e:
    logger.error(f"Milvus connection failed: {e}")
    raise VectorStoreError("Could not connect to Milvus")


# -----------------------------
# Create / Load Collection
# -----------------------------

def get_or_create_collection():
    try:
        if utility.has_collection(COLLECTION_NAME):
            return Collection(COLLECTION_NAME)

        fields = [
            FieldSchema(
                name="id",
                dtype=DataType.INT64,
                is_primary=True,
                auto_id=True
            ),
            FieldSchema(
                name="embedding",
                dtype=DataType.FLOAT_VECTOR,
                dim=EMBEDDING_DIM
            ),
            FieldSchema(
                name="text",
                dtype=DataType.VARCHAR,
                max_length=65535
            )
        ]

        schema = CollectionSchema(
            fields=fields,
            description="Document embeddings"
        )

        collection = Collection(
            name=COLLECTION_NAME,
            schema=schema
        )

        index_params = {
            "metric_type": "COSINE",
            "index_type": "IVF_FLAT",
            "params": {"nlist": 128}
        }

        collection.create_index(
            field_name="embedding",
            index_params=index_params
        )

        return collection

    except Exception as e:
        logger.error(f"Collection creation failed: {e}")
        raise VectorStoreError("Failed to create/load collection")


collection = get_or_create_collection()


def reset_collection():
    try:
        global collection
        collection.drop()
        collection = get_or_create_collection()
        logger.info("Collection reset successful")
    except Exception as e:
        logger.error(f"Collection reset failed: {e}")
        raise VectorStoreError("Failed to reset collection")


# -----------------------------
# Insert Documents
# -----------------------------

def add_documents(texts, embeddings):
    try:
        if not texts or not embeddings:
            raise ValueError("Empty texts or embeddings")

        collection.insert([
            embeddings,
            texts
        ])

        collection.flush()

        logger.info(f"Inserted {len(texts)} documents")

    except Exception as e:
        logger.error(f"Insert failed: {e}")
        raise VectorStoreError("Failed to insert documents")


# -----------------------------
# Similarity Search
# -----------------------------

def similarity_search(query_embedding, k=5):
    try:
        collection.load()

        search_params = {
            "metric_type": "COSINE",
            "params": {"nprobe": 10}
        }

        results = collection.search(
            data=[query_embedding],
            anns_field="embedding",
            param=search_params,
            limit=k,
            output_fields=["text"]
        )

        return [hit.entity.get("text") for hit in results[0]]

    except Exception as e:
        logger.error(f"Search failed: {e}")
        raise VectorStoreError("Vector search failed")
