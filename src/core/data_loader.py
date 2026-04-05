from langchain_community.document_loaders import PyMuPDFLoader
import os
from pathlib import Path

class DocumentLoader:

    """PDF Documents loader class"""

    def __init__(self, data_path):
        self.data_path = Path(data_path)
        if not self.data_path.exists():
            raise FileNotFoundError(f"Data path not found: {self.data_path}")
        
    def load_pdfs(self) -> list:
        """Finds all PDFs in the directory and loads them."""

        all_docs = []

        # Look for the all pdf files in the directory
        pdf_files = list(self.data_path.glob("*.pdf"))

        if not pdf_files:
            print(f"No PDF files found at {self.data_path}")
            return []
        
        for pdf_path in pdf_files:
            print("="*40)
            print(f"Loading {pdf_path.name}")
            print("="*40)
            loader = PyMuPDFLoader(file_path=str(pdf_path)) # .load() returns a list of Document objects (one per page)
            all_docs.extend(loader.load())

        print(f"Successfully loaded {len(all_docs)} pages from {len(pdf_files)} files.")
        return all_docs