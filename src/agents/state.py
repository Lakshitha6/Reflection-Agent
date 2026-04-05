from typing import List, TypedDict, Annotated
import operator

class AgentState(TypedDict):
    

    """AgentState of the Reflection Agent
    
    Attributes:
        input (str): The original user query.
        documents (Annotated[List[str], operator.add]): List of retrieved documents from the vector database. 
        run_tavily (bool): Flag to indicate whether to run the TAVILY agent.
        generation (str): The generated final response.
        refined_query (str): The refined user query before sending to the TAVILY agent.
        iteration_count (int): Prevent infinite looping
        is_allowed (bool): Whether the question is allowed by the guardrail.
        
    Note:
        The `documents` attribute is annotated with `operator.add` to 
        indicate that it can be extended with additional documents as the agent retrieves more information during its iterations.

    """



    input: str
    documents: Annotated[List[str], operator.add]
    run_tavily: bool
    generation: str
    refined_query: str
    iteration_count: int
    is_allowed: bool