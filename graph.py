from langgraph.graph import StateGraph, END
from state import AgentState
from nodes import vision_node, audio_node, aggregator_node, action_node

def build_graph():
    """
    Constructs the Real-Time Threat Detection Graph.
    """
    workflow = StateGraph(AgentState)

    # Add nodes
    workflow.add_node("vision", vision_node)
    workflow.add_node("audio", audio_node)
    workflow.add_node("aggregator", aggregator_node)
    workflow.add_node("action", action_node)

    # Define edges
    # Start -> Vision & Audio (Parallel) -> Aggregator -> Action -> End
    
    workflow.set_entry_point("vision")
    workflow.add_edge("vision", "audio")
    workflow.add_edge("audio", "aggregator")
    
    # Conditional Routing: Only go to 'action' if threat is detected.
    def should_act(state: AgentState):
        assessment = state.get("threat_assessment")
        if assessment and assessment.threat_level in ["HIGH", "MEDIUM"]:
            return "action"
        return END

    workflow.add_conditional_edges(
        "aggregator",
        should_act,
        {
            "action": "action",
            END: END
        }
    )
    
    workflow.add_edge("action", END)

    return workflow.compile()

if __name__ == "__main__":
    app = build_graph()
    print("Graph built successfully.")
