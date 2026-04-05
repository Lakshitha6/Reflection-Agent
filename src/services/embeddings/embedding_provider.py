# Initialize embeddings services. 

from langchain_huggingface import HuggingFaceEndpointEmbeddings
from .embedding_base import BaseEmbeddingService

class HuggingFaceService(BaseEmbeddingService):

    def __init__(self, model_name: str, hf_token: str):
        if not hf_token:
            raise ValueError("HF_TOKEN is missing!")
        
        self._client = HuggingFaceEndpointEmbeddings(
            model=model_name,
            huggingfacehub_api_token=hf_token
        )

    def get_embeddings(self):
        return self._client
    
    def embed_query(self, text: str):
        return self._client.embed_query(text)
    
    def embed_documents(self, texts: list[str]):
        return self._client.embed_documents(texts)
    

# class OpenAISerivice should define as above if wants to use that