from abc import ABC, abstractmethod
from langchain_core.documents import Document

class BaseVectorStore(ABC):

    @abstractmethod
    def add_documents(self, documents: list[Document]):
        """Uploads chunked documents to the database"""
        pass

    @abstractmethod
    def similarity_search(self, query: str, k: int = 3) -> list[Document]:
        """Finds the most relevant chunks for a given question"""
        pass
