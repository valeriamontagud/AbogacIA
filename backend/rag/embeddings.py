"""Embeddings module for vectorizing documents using OpenAI."""

import os
from typing import List
from openai import OpenAI


class EmbeddingsManager:
    """Manages document embeddings using OpenAI's embedding API."""

    def __init__(self, api_key: str = None):
        """Initialize embeddings manager.
        
        Args:
            api_key: OpenAI API key. If None, reads from OPENAI_API_KEY env var.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not provided or found in environment")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = "text-embedding-3-small"

    def embed_text(self, text: str) -> List[float]:
        """Embed a single text string.
        
        Args:
            text: Text to embed
            
        Returns:
            List of embeddings
        """
        response = self.client.embeddings.create(
            input=text,
            model=self.model
        )
        return response.data[0].embedding

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """Embed multiple text strings.
        
        Args:
            texts: List of texts to embed
            
        Returns:
            List of embedding vectors
        """
        if not texts:
            return []
        
        response = self.client.embeddings.create(
            input=texts,
            model=self.model
        )
        return [item.embedding for item in response.data]

    def get_embedding_dimension(self) -> int:
        """Get the dimension of embeddings produced by this model.
        
        Returns:
            Embedding dimension
        """
        return 1536
