"""Pinecone vector database client for RAG retrieval."""

import os
from typing import List, Dict, Any, Optional
from pinecone import Pinecone, ServerlessSpec


class PineconeManager:
    """Manages Pinecone vector database operations."""

    def __init__(self, api_key: str = None, index_name: str = "bufete-legal-rag"):
        """Initialize Pinecone manager.
        
        Args:
            api_key: Pinecone API key. If None, reads from PINECONE_API_KEY env var.
            index_name: Name of the Pinecone index
        """
        self.api_key = api_key or os.getenv("PINECONE_API_KEY")
        if not self.api_key:
            raise ValueError("Pinecone API key not provided or found in environment")
        
        self.index_name = index_name
        self.pc = Pinecone(api_key=self.api_key)
        self.index = None
        self._ensure_index_exists()

    def _ensure_index_exists(self) -> None:
        """Create index if it doesn't exist."""
        existing_indexes = self.pc.list_indexes()
        
        if self.index_name not in [idx.name for idx in existing_indexes]:
            print(f"Creating Pinecone index '{self.index_name}'...")
            self.pc.create_index(
                name=self.index_name,
                dimension=1536,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1")
            )
        
        self.index = self.pc.Index(self.index_name)

    def upsert_vectors(self, vectors: List[tuple]) -> Dict[str, Any]:
        """Insert or update vectors in Pinecone.
        
        Args:
            vectors: List of tuples (id, embedding, metadata)
            
        Returns:
            Upsert response
        """
        if not self.index:
            raise RuntimeError("Pinecone index not initialized")
        
        upsert_response = self.index.upsert(vectors=vectors)
        return upsert_response

    def query_vectors(self, query_embedding: List[float], top_k: int = 5,
                     filter_dict: Optional[Dict] = None) -> List[Dict]:
        """Query vectors from Pinecone.
        
        Args:
            query_embedding: Query embedding vector
            top_k: Number of results to return
            filter_dict: Optional metadata filter
            
        Returns:
            List of matching documents with scores
        """
        if not self.index:
            raise RuntimeError("Pinecone index not initialized")
        
        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True,
            filter=filter_dict
        )
        
        matches = []
        for match in results.matches:
            matches.append({
                "id": match.id,
                "score": match.score,
                "metadata": match.metadata
            })
        
        return matches

    def delete_vectors(self, ids: List[str]) -> Dict[str, Any]:
        """Delete vectors by ID.
        
        Args:
            ids: List of vector IDs to delete
            
        Returns:
            Delete response
        """
        if not self.index:
            raise RuntimeError("Pinecone index not initialized")
        
        return self.index.delete(ids=ids)

    def get_index_stats(self) -> Dict[str, Any]:
        """Get statistics about the index.
        
        Returns:
            Index statistics
        """
        if not self.index:
            raise RuntimeError("Pinecone index not initialized")
        
        return self.index.describe_index_stats()

    def clear_index(self) -> Dict[str, Any]:
        """Clear all vectors from the index.
        
        Returns:
            Deletion response
        """
        if not self.index:
            raise RuntimeError("Pinecone index not initialized")
        
        return self.index.delete(delete_all=True)
