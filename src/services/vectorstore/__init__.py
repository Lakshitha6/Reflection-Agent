from .vector_factory import VectorStoreFactory
from src.core import config
from src.services.embeddings import embeddings

vector_db = VectorStoreFactory.create(config=config, embedding_service= embeddings.get_embeddings())

__all__ = ["vector_db"]