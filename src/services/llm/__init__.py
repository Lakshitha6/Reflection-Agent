from .llm_factory import LLMFactory
from src.core import config

llm_service = LLMFactory.create(config=config)

__all__ = ["llm_service"]