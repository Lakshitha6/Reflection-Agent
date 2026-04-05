import os
from dotenv import load_dotenv

from .embedding_provider import HuggingFaceService  #  Import OpenAISerivice if its defined at the embedding_provider

load_dotenv()

class EmbeddingFactory:

    @staticmethod
    def create(config: dict):

        # look at the active provider in the settings.yaml file
        active_provider = config["embeddings"]["active_provider"]
        spec = config["embeddings"]["providers"][active_provider]

        if active_provider == "hf":
            token = os.getenv("HF_TOKEN")

            return HuggingFaceService(model_name=spec["model"], hf_token=token)
        
        # add -- if active_provider == "openai" -- if its defined.
        else:
            raise ValueError(f"Embedding provider {active_provider} not supported.")
