"""RAG Engine for generating documents using retrieved context."""

import os
import uuid
from typing import List, Dict, Any, Optional
from openai import OpenAI
from .embeddings import EmbeddingsManager
from .pinecone_client import PineconeManager
from .document_processor import DocumentProcessor


class RAGEngine:
    """Main RAG engine for document generation."""

    def __init__(self, openai_api_key: str = None, pinecone_api_key: str = None,
                 index_name: str = "bufete-legal-rag"):
        """Initialize RAG engine.
        
        Args:
            openai_api_key: OpenAI API key
            pinecone_api_key: Pinecone API key
            index_name: Pinecone index name
        """
        self.embeddings = EmbeddingsManager(api_key=openai_api_key)
        self.pinecone = PineconeManager(api_key=pinecone_api_key, index_name=index_name)
        self.processor = DocumentProcessor()
        
        self.openai_api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
        self.openai_client = OpenAI(api_key=self.openai_api_key)

    def ingest_documents(self, documents: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Ingest documents into the RAG system.
        
        Args:
            documents: List of documents with 'text', 'doc_type', and 'doc_name'
            
        Returns:
            Ingestion statistics
        """
        vectors_to_upsert = []
        
        for doc in documents:
            chunk_id = str(uuid.uuid4())
            text = doc.get("text", "")
            
            embedding = self.embeddings.embed_text(text)
            
            metadata = {
                "doc_type": doc.get("doc_type", "general"),
                "doc_name": doc.get("doc_name", "unknown"),
                "source_file": doc.get("source_file", ""),
                "chunk_start": doc.get("chunk_start", 0),
                "chunk_end": doc.get("chunk_end", len(text)),
                "text_preview": text[:200]
            }
            
            vectors_to_upsert.append((chunk_id, embedding, metadata))
        
        if vectors_to_upsert:
            self.pinecone.upsert_vectors(vectors_to_upsert)
        
        return {
            "status": "success",
            "documents_ingested": len(documents),
            "total_vectors": len(vectors_to_upsert)
        }

    def retrieve_context(self, query: str, top_k: int = 5,
                        doc_type_filter: Optional[str] = None) -> List[Dict[str, Any]]:
        """Retrieve relevant context for a query.
        
        Args:
            query: Query text
            top_k: Number of results to retrieve
            doc_type_filter: Optional filter by document type
            
        Returns:
            List of relevant documents
        """
        query_embedding = self.embeddings.embed_text(query)
        
        filter_dict = None
        if doc_type_filter:
            filter_dict = {"doc_type": {"$eq": doc_type_filter}}
        
        results = self.pinecone.query_vectors(query_embedding, top_k=top_k, filter_dict=filter_dict)
        
        return results

    def generate_with_context(self, prompt: str, query: str = None,
                             context_docs: List[Dict] = None, model: str = "gpt-4",
                             temperature: float = 0.7, max_tokens: int = 2000) -> str:
        """Generate content using RAG context.
        
        Args:
            prompt: Generation prompt
            query: Optional query to retrieve context
            context_docs: Optional pre-retrieved context documents
            model: OpenAI model to use
            temperature: Generation temperature
            max_tokens: Maximum tokens to generate
            
        Returns:
            Generated content
        """
        context_text = ""
        
        if query and not context_docs:
            context_docs = self.retrieve_context(query, top_k=5)
        
        if context_docs:
            context_text = "\n\n".join([
                f"[{doc.get('metadata', {}).get('doc_name', 'Unknown')}]\n{doc.get('metadata', {}).get('text_preview', '')}"
                for doc in context_docs if 'metadata' in doc
            ])
        
        system_message = """Eres un abogado experto del bufete de abogados. 
Tu tarea es generar plantillas, correos y documentos legales profesionales.
Utiliza el contexto proporcionado para mantener consistencia con el estilo y la información del bufete.
Responde siempre en español y de manera profesional."""

        if context_text:
            system_message += f"\n\nContexto del bufete:\n{context_text}"
        
        response = self.openai_client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        return response.choices[0].message.content

    def generate_template(self, template_type: str, cliente: str = "", details: Dict = None) -> str:
        """Generate a legal template with RAG context.
        
        Args:
            template_type: Type of template (e.g., "aceptacion_pago", "demanda")
            cliente: Client name
            details: Additional details for the template
            
        Returns:
            Generated template
        """
        if details is None:
            details = {}
        
        query = f"plantilla {template_type} bufete abogados"
        
        prompt = f"""Genera una plantilla legal de tipo '{template_type}' para el cliente '{cliente}'.
        
Detalles adicionales:
{chr(10).join(f"- {k}: {v}" for k, v in details.items())}

La plantilla debe ser profesional, completa y lista para usar. 
Incluye espacios para rellenar información específica del caso cuando sea necesario."""

        return self.generate_with_context(
            prompt=prompt,
            query=query,
            temperature=0.5
        )

    def generate_email(self, email_type: str, recipient: str = "",
                      subject: str = "", body_details: Dict = None) -> Dict[str, str]:
        """Generate a professional email with RAG context.
        
        Args:
            email_type: Type of email (e.g., "seguimiento", "confirmacion")
            recipient: Email recipient
            subject: Email subject
            body_details: Details for email body
            
        Returns:
            Dictionary with 'subject' and 'body'
        """
        if body_details is None:
            body_details = {}
        
        query = f"ejemplo correo email {email_type} clientes"
        
        prompt = f"""Genera un correo profesional de tipo '{email_type}' para el destinatario '{recipient}'.

Asunto requerido: {subject or 'A definir según el contenido'}

Detalles del correo:
{chr(10).join(f"- {k}: {v}" for k, v in body_details.items())}

El correo debe ser profesional, empático y representar bien al bufete de abogados.
Incluye un cierre profesional con datos de contacto del bufete si es relevante."""

        body = self.generate_with_context(
            prompt=prompt,
            query=query,
            temperature=0.6
        )
        
        final_subject = subject or f"Re: Asunto del correo - {email_type}"
        
        return {
            "subject": final_subject,
            "body": body
        }

    def get_index_stats(self) -> Dict[str, Any]:
        """Get statistics about the RAG index.
        
        Returns:
            Index statistics
        """
        return self.pinecone.get_index_stats()
