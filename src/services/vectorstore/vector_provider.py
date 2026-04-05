from qdrant_client.grpc import Distance, VectorParams

from .vector_base import BaseVectorStore
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from langchain_core.documents import Document

class QdrantProvider(BaseVectorStore):

    def __init__(self, embedding_service, url: str, api_key: str, collection_name: str):

        self.client = QdrantClient(
            url=url,
            api_key=api_key,
        )

        if not self.client.collection_exists(collection_name=collection_name):
            print(f"Creating Qdrant collection '{collection_name}'...")

            self.client.create_collection(
                    collection_name=collection_name,
                    vectors_config=VectorParams(
                    size= 768,
                    distance=Distance.COSINE
                    )          
            )

        # The PDF Knowledge Base
        self._db = QdrantVectorStore(
            client=self.client,
            embedding=embedding_service,
            collection_name=collection_name,
        )
        

    # Knowledge Base Methods(PDF)
    def add_documents(self, documents: list[Document]):
        print(f"Adding {len(documents)} documents to Qdrant...")
        
        self._db.add_documents(documents=documents)

    def similarity_search(self, query: str, k: int = 3) -> list[Document]:
        return self._db.similarity_search(query=query, k=k)