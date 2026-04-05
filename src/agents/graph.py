from turtle import st

from langgraph.graph import StateGraph, START, END

from .state import AgentState
from .nodes import (
    retrieve_node,
    grade_documents_node, 
    generate_node,
    refine_query_node,
    tavily_tool_node,
    guardrail_node
)

# Initialize the Graph
workflow = StateGraph(AgentState)

# Define the nodes
workflow.add_node("guardrail", guardrail_node)
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("grade_documents", grade_documents_node)
workflow.add_node("generate", generate_node)
workflow.add_node("refine_query", refine_query_node)
workflow.add_node("tavily_tool", tavily_tool_node)

# Define the edges
workflow.add_edge(START, "guardrail")
workflow.add_edge("retrieve", "grade_documents")
workflow.add_edge("tavily_tool","generate")
workflow.add_edge("generate", END)


# Define conditional edge function for guardrail
def decide_to_process(state: AgentState):
    """
    Determines whether to proceed with processing or refuse based on guardrail evaluation.
    """

    if state.get("is_allowed", False):
        return "retrieve"
    
    return END

# Add the conditional edge for guardrail
workflow.add_conditional_edges(
    "guardrail",
    decide_to_process,
    {
        "retrieve": "retrieve",
        END: END
    }
)



# Define Conditional Edge
def decide_to_generate(state: AgentState):
    """
    Determines whether to move to generation or fallback to Tavily search.
    """

    # MAX Loops to prevent infinite cycles
    if state.get("iteration_count",0) >= 3:
        print("----------------Max iterations reached. Moving to generation.----------------")
        return "generate"
    
    if state["run_tavily"]:
        return "refine_query"
    
    # Doesn't need  to run tavily, move to generation
    return "generate"


# Add the conditional edge
workflow.add_conditional_edges(
    "grade_documents",
    decide_to_generate,
    {
        "refine_query": "refine_query",
        "generate": "generate"
    }
)

workflow.add_edge("refine_query", "tavily_tool")

app = workflow.compile()