"""
Ingest pipeline: load policy documents → chunk → embed → store in ChromaDB.
Also persists raw chunks for BM25 sparse retrieval.
Run this script once (or whenever documents change) before starting the app.

Usage:
    python ingest.py
"""

import pickle

from dotenv import load_dotenv

load_dotenv()

from config import (
    DATA_DIR, CHROMA_DIR, CHUNK_SIZE, CHUNK_OVERLAP,
    EMBEDDING_MODEL, CHUNKS_PATH,
)
from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.embeddings import get_embedding_model
from src.vector_store import create_vector_store


def main():
    print("=== XanhSM Policy Ingestion Pipeline ===\n")

    print("[1/5] Loading documents...")
    documents = load_documents(DATA_DIR)

    print("\n[2/5] Splitting into chunks...")
    chunks = split_documents(documents, CHUNK_SIZE, CHUNK_OVERLAP)

    print("\n[3/5] Initializing embedding model...")
    embedding_model = get_embedding_model(EMBEDDING_MODEL)

    print("\n[4/5] Creating vector store...")
    create_vector_store(chunks, embedding_model, CHROMA_DIR)

    print("\n[5/5] Saving chunks for BM25 retriever...")
    CHUNKS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CHUNKS_PATH, "wb") as f:
        pickle.dump(chunks, f)
    print(f"Saved {len(chunks)} chunks to {CHUNKS_PATH}")

    print("\n=== Ingestion complete! ===")


if __name__ == "__main__":
    main()
