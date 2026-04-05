""" Test the workflow graph. """

def test_full_graph_execution(agent_app):

    """
    Test the full execution of the workflow graph using `invoke`.

    The `invoke` method executes the LangGraph workflow with the given input
    and optional configuration, returning the final state.

    Args:
        agent_app: Compiled LangGraph application instance.

    Invoke Signature:
        invoke(
            input: InputT | Command | None,
            config: RunnableConfig | None = None,
            *,
            context: ContextT | None = None,
            stream_mode: StreamMode = "values",
            print_mode: StreamMode | Sequence[StreamMode] = (),
            output_keys: str | Sequence[str] | None = None,
        ) -> dict[str, Any] | Any

    Parameters:
        input: Input data for the graph (e.g., dict with query, documents, etc.).
        config: Configuration for execution.

            Example:
                {"configurable": {"thread_id": "test_1"}}

            The `thread_id` acts as a storage key that allows LangGraph to:
            - Persist conversation state
            - Retrieve it later for the same session
    """

    

    inputs = {
        "input": "Explain Scientific Management Theory.?",
        "documents": [],
        "iteration_count": 0
    }

    config = {"configurable": {"thread_id": "test_1"}}

    final_state = agent_app.invoke(input=inputs, config=config)

    # Assertions
    assert "generation" in final_state
    assert len(final_state["generation"]) > 0
    assert final_state["iteration_count"] >= 0