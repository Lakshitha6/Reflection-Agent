from abc import ABC, abstractmethod

class BaseEmbeddingService:
    @abstractmethod
    def get_embeddings(self):
        """Returns the LangChain compatible embedding object."""
        pass

    @abstractmethod
    def embed_query(self, text: str):
        """Embeds a single string (for searching)."""
        pass

    @abstractmethod
    def embed_documents(self, texts: list[str]):
        """Embeds a list of strings (for indexing)."""
        pass