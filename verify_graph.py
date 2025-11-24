from graph import build_graph
from state import AgentState

def test_graph():
    print("Building graph...")
    app = build_graph()
    
    print("Initializing state...")
    initial_state = AgentState(
        image_data=b"fake_image_bytes",
        audio_data=b"fake_audio_bytes",
        vision_analysis=None,
        audio_analysis=None,
        threat_assessment=None
    )
    
    print("Running graph...")
    try:
        result = app.invoke(initial_state)
        print("\n--- Execution Result ---")
        print(f"Vision Analysis: {result.get('vision_analysis')}")
        print(f"Audio Analysis: {result.get('audio_analysis')}")
        print(f"Threat Assessment: {result.get('threat_assessment')}")
        print(f"Action Log: {result.get('action_log')}")
        
        assessment = result.get('threat_assessment')
        if assessment:
            print(f"\nFinal Threat Level: {assessment.threat_level}")
            print(f"Reasoning: {assessment.reasoning}")
            
        action_log = result.get('action_log')
        if action_log:
            print("\nExecuted Actions:")
            for action in action_log:
                print(f" - {action}")
        else:
            print("\nNo actions executed.")
            
    except Exception as e:
        print(f"Graph execution failed: {e}")

if __name__ == "__main__":
    test_graph()
