from src.agents.nodes import grade_documents_node


def test_grader_node_relevant():
    # 1. Setup a "perfect" state
    state = {
        "input": "What is recruitment?",
        "documents": ["Recruitment is the process of finding and hiring candidates."],
        "iteration_count": 0
    }

    result = grade_documents_node(state=state)

    assert result["run_tavily"] is False


def test_grader_node_irrelevant():
    # 1. Setup a "non perfect" state
    state = {
        "input": "How to bake a cake?",
        "documents": ["The stock market is volatile and can be influenced by various factors."],
        "iteration_count": 0
    }

    result = grade_documents_node(state=state)

    assert result["run_tavily"] is True