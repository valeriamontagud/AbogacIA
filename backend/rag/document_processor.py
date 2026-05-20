"""Document processing and chunking for RAG."""

import os
import re
from typing import List, Dict, Any, Optional
from pathlib import Path


class DocumentProcessor:
    """Processes documents for RAG ingestion."""

    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """Initialize document processor.
        
        Args:
            chunk_size: Size of text chunks in characters
            chunk_overlap: Overlap between chunks in characters
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def load_text_file(self, file_path: str) -> str:
        """Load text from a file.
        
        Args:
            file_path: Path to text file
            
        Returns:
            File content
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

    def chunk_text(self, text: str, metadata: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """Split text into overlapping chunks.
        
        Args:
            text: Text to chunk
            metadata: Additional metadata for chunks
            
        Returns:
            List of chunks with metadata
        """
        if metadata is None:
            metadata = {}

        chunks = []
        start = 0

        while start < len(text):
            end = min(start + self.chunk_size, len(text))
            chunk_text = text[start:end].strip()
            
            if chunk_text:
                chunk_data = {
                    "text": chunk_text,
                    "chunk_start": start,
                    "chunk_end": end,
                    **metadata
                }
                chunks.append(chunk_data)
            
            start += self.chunk_size - self.chunk_overlap

        return chunks

    def process_document(self, file_path: str, doc_type: str = "general",
                        doc_name: str = None) -> List[Dict[str, Any]]:
        """Process a single document into chunks.
        
        Args:
            file_path: Path to document
            doc_type: Type of document (e.g., "template", "email", "info")
            doc_name: Name of document for metadata
            
        Returns:
            List of processed chunks
        """
        text = self.load_text_file(file_path)
        
        if not doc_name:
            doc_name = Path(file_path).stem
        
        metadata = {
            "doc_type": doc_type,
            "doc_name": doc_name,
            "source_file": file_path
        }
        
        return self.chunk_text(text, metadata)

    def process_directory(self, directory_path: str, doc_type: str = "general") -> List[Dict[str, Any]]:
        """Process all text files in a directory.
        
        Args:
            directory_path: Path to directory containing text files
            doc_type: Type of documents
            
        Returns:
            List of all processed chunks
        """
        all_chunks = []
        path = Path(directory_path)
        
        for file_path in path.glob("*.txt"):
            try:
                chunks = self.process_document(str(file_path), doc_type)
                all_chunks.extend(chunks)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
        
        return all_chunks

    def clean_text(self, text: str) -> str:
        """Clean text by removing extra whitespace and special chars.
        
        Args:
            text: Text to clean
            
        Returns:
            Cleaned text
        """
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F]', '', text)
        return text.strip()

    def extract_sections(self, text: str, section_pattern: str = r"^#{1,3}\s+") -> List[Dict[str, str]]:
        """Extract sections from markdown-formatted text.
        
        Args:
            text: Text with markdown headers
            section_pattern: Regex pattern for section headers
            
        Returns:
            List of sections with title and content
        """
        lines = text.split('\n')
        sections = []
        current_section = None
        current_content = []

        for line in lines:
            if re.match(section_pattern, line):
                if current_section:
                    sections.append({
                        "title": current_section,
                        "content": '\n'.join(current_content).strip()
                    })
                current_section = line.strip()
                current_content = []
            else:
                current_content.append(line)

        if current_section:
            sections.append({
                "title": current_section,
                "content": '\n'.join(current_content).strip()
            })

        return sections
