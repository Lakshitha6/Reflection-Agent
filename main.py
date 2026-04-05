def main():

    

# ======================================================================================================
    #  Uncomment these at first run to make and store the vectorstore

    
    # from src.core import DocumentLoader, TextSplitter, config
    # from src.services.vectorstore import vector_db

    # # 1. Get the path from our global config
    # data_path = config["data"]["raw_path"]

    # # 2. Initialize and load
    # loader = DocumentLoader(data_path)
    # loaded_pdfs = loader.load_pdfs()

    # chunks_maker = TextSplitter(
    #     chunk_size=config["processing"]["chunk_size"],
    #     chunk_overlap=config["processing"]["chunk_overlap"]
    #     )
    
    # chunked_pdfs = chunks_maker.split_documents(loaded_pdfs)
    
    # # Make vector store and save at "data/vector_db"
    # vector_db.add_documents(chunked_pdfs)

# ======================================================================================================


    # Test by retrieving documents from vectordb

    # from src.services.vectorstore import vector_db

    # results = vector_db.similarity_search("What is recruitment selection?")
    # print(f"Found {len(results)} relevant chunks.")
    # print(f"Top result: {results[0].page_content[:200]}...")

# ======================================================================================================


# Test The Agent

    from src.agents.graph import app

    def run_agent(query: str):
        inputs = {
            "input": query,
            "iteration_count": 0,
            "documents": []
        }


        final_generation = None

        for output in app.stream(inputs):
            for key, value in output.items():
                print(f"Finished Node: {key}")

                if key == "generate":
                    final_generation = value["generation"]

        print("\n-------------------Final Output-------------------")
        print(final_generation)

    test_query = "What is the meaning ofScientific management theory ?"
    run_agent(test_query)

if __name__ == "__main__":
    main()