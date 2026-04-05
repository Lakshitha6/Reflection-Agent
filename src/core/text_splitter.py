from langchain_text_splitters import RecursiveCharacterTextSplitter

class TextSplitter:

    def __init__(self, chunk_size: int, chunk_overlap: int):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n","\n"," ",""]
        )

    def split_documents(self, documents: list):
        """
        Takes a list of LangChain Document objects from the Loader
        and returns a list of smaller chunked Documents.
        """

        if not documents:
            return []
        
        chunks = self.splitter.split_documents(documents)

        print(f"Split {len(documents)} pages into {len(chunks)} chunks.")
        return chunks