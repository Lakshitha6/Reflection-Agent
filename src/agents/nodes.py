from src.services.llm import llm_service
from .state import AgentState
from src.services.search_tool import tavily_search
from src.services.vectorstore import vector_db
import json
from .prompts import GRADER_PROMPT, GENERATOR_PROMPT, REFINER_PROMPT, GUARDRAIL_PROMPT

# Vector store retrieving node
def retrieve_node(state: AgentState):
    """
    Fetches documents from vector store based on the user's input

    """

    print("---------- Retrieving from vectorstore ----------")

    question = state["input"]
    results = vector_db.similarity_search(query=question)

    docs = [doc.page_content for doc in results]

    # Initialize iteration_count if it doesn't exist
    return {
        "documents": docs,
        "iteration_count": 0
    }


# Evaluating retrieved content node
def grade_documents_node(state: AgentState):
    """
    Determines if the retrieved documents are relevant to the question.
    """

    print("---------- Evaluating retrieved contents ----------")

    user_message = f"User Question: {state['input']}\nRetrieved Documents: {state['documents']}"

    if not state['documents']:
        return {
            "run_tavily": True
        }
    
    else:
        response_text = llm_service.generate(
            user_query=user_message,
            system_prompt=GRADER_PROMPT
        )

        try:
            score = json.loads(response_text).get("score", "no")
        
        except:
            score = "no"

        return {
            "run_tavily": (score == "no")
        }
    

# Final answer generation node
def generate_node(state: AgentState):
    """
    Generates the final answer using all accumulated documents.
    """

    print("---------- Generating final answer ----------")

    context_str = "\n\n".join(state['documents'])
    user_query = f"Question: {state['input']}\n\nContext:\n{context_str}"

    response = llm_service.generate(
        user_query=user_query,
        system_prompt=GENERATOR_PROMPT
    )

    return {
        "generation": response
    }


# Refine node to refine the user query for better retrieval from the tavily
def refine_query_node(state: AgentState):
    """
    Optimizes the user's question for a web search engine (Tavily).
    """

    print("---------- Refining query for Tavily ----------")

    user_query = f"Original Question: {state['input']}"

    optimized_query = llm_service.generate(
        user_query=user_query,
        system_prompt=REFINER_PROMPT
    )


    # Strip whitespace and remove quotes from the optimized query , llm might added
    clean_query = optimized_query.strip().replace('"', '')

    return {
        "refined_query": clean_query,
        "iteration_count": state.get("iteration_count",0) + 1
    }


# Tavily search node
def tavily_tool_node(state: AgentState):
    """
    Performs a web search using the refined query and appends to documents.
    """

    print(f"---------- Performing Web search for {state['refined_query']} ----------")

    search_result = tavily_search(state['refined_query'])

    # search results will automatically append to the documents because of Annotated[str] in the AgentState definition
    return {
        "documents": [search_result]
    }



# Guardrail node to filter out irrelevant questions
def guardrail_node(state: AgentState):
    """
    Determines if the user's question is relevant to the agent's domain That's HR, Finance , Business ,Marketing.
    """

    print("---------- Guardrail check for relevance ----------")

    user_query = f"User Question: {state['input']}"

    response = llm_service.generate(
        user_query=user_query,
        system_prompt=GUARDRAIL_PROMPT
    )

    decision = response.strip().lower()

    if "allow" in decision:
        return {"is_allowed": True}
    else:
        return {"is_allowed": False}