from .embedding_factory import EmbeddingFactory
from src.core import config

embeddings = EmbeddingFactory().create(config=config)

__all__ = ["embeddings"]