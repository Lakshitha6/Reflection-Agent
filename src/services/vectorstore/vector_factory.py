from .vector_provider import QdrantProvider
from src.core import config

import os
from dotenv import load_dotenv
load_dotenv()

class VectorStoreFactory:

    @staticmethod
    def create(config: dict, embedding_service):
        active_vector_provider = config["vectorstore"]["active_provider"]
        spec = config["vectorstore"]["providers"][active_vector_provider]

        if active_vector_provider == "qdrant":

            url = os.getenv("QDRANT_URL")
            api_key = os.getenv("QDRANT_API_KEY")

            # Validation: Fail with a clear message if env is not set

            if not url or not api_key:
                raise ValueError(
                    "Missing QDRANT_URL or QDRANT_API_KEY in environment variables. "
                )

            return QdrantProvider(
            embedding_service=embedding_service,
            url=url,
            api_key=api_key,
            collection_name=spec["collection_name"],
            )

        else:
            raise ValueError(f"Vector Store provider {active_vector_provider} not supported.")