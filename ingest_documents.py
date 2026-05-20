#!/usr/bin/env python3
"""
Script to ingest documents into the RAG system.
Example usage to help you get started quickly.
"""

import os
import sys
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from rag.rag_engine import RAGEngine
from rag.document_processor import DocumentProcessor


def ingest_from_directory(rag_engine: RAGEngine, directory: str, doc_type: str) -> int:
    """Ingest all text files from a directory."""
    processor = DocumentProcessor()
    data_path = Path(directory)
    
    if not data_path.exists():
        print(f"Directory not found: {directory}")
        return 0
    
    all_chunks = []
    for file_path in data_path.glob("*.txt"):
        if "_placeholder" in file_path.name:
            print(f"Skipping placeholder file: {file_path.name}")
            continue
        
        print(f"Processing: {file_path.name}")
        chunks = processor.process_document(str(file_path), doc_type=doc_type)
        all_chunks.extend(chunks)
    
    if all_chunks:
        result = rag_engine.ingest_documents(all_chunks)
        print(f"Ingested {result['total_vectors']} vectors from {len(all_chunks)} chunks")
        return len(all_chunks)
    
    return 0


def main():
    """Main ingestion function."""
    print("=" * 60)
    print("RAG Document Ingestion Script")
    print("=" * 60)
    
    # Check for API keys
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not set in .env")
        return 1
    
    if not os.getenv("PINECONE_API_KEY"):
        print("Error: PINECONE_API_KEY not set in .env")
        return 1
    
    try:
        # Initialize RAG Engine
        print("Initializing RAG Engine...")
        rag_engine = RAGEngine(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            pinecone_api_key=os.getenv("PINECONE_API_KEY"),
            index_name=os.getenv("PINECONE_INDEX_NAME", "bufete-legal-rag")
        )
        print("✓ RAG Engine initialized\n")
        
        # Ingest documents
        data_dir = os.path.join(os.path.dirname(__file__), "backend", "data")
        
        print("Ingesting documents from data/ directory...")
        print("-" * 60)
        
        # Ingest by document type
        counts = {
            "info": ingest_from_directory(rag_engine, data_dir, "info"),
            "email": ingest_from_directory(rag_engine, data_dir, "email"),
            "template": ingest_from_directory(rag_engine, data_dir, "template"),
        }
        
        print("-" * 60)
        print("\nIngestion Summary:")
        print(f"  Info documents: {counts['info']} chunks")
        print(f"  Email templates: {counts['email']} chunks")
        print(f"  Legal templates: {counts['template']} chunks")
        print(f"  Total: {sum(counts.values())} chunks\n")
        
        # Show index stats
        print("Index Statistics:")
        stats = rag_engine.get_index_stats()
        print(f"  Total vectors: {stats.get('total_vector_count', 'N/A')}")
        print(f"  Dimension: {stats.get('dimension', 'N/A')}")
        
        print("\nSuccess! RAG system is ready to use.")
        print("Start the API with: uvicorn backend.main:app --reload")
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
