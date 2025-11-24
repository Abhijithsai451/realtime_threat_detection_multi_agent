from fastapi import FastAPI, BackgroundTasks
from graph import build_graph
from state import AgentState
from simulator import generate_mock_event
import asyncio

app = FastAPI(title="Real-time Threat Detection Agent")
graph_app = build_graph()

@app.get("/")
async def root():
    return {"message": "System Operational"}

@app.post("/process_event")
async def process_event():
    """
    Triggers a single analysis cycle.
    In a real system, this might be triggered by a webhook or a timer.
    """
    # 1. Fetch data from Simulator
    # Note: simulator.generate_mock_event returns a dict, but our state needs specific keys.
    # Let's assume we extract raw data from it or just pass it as is if it matches.
    # For now, we'll create a fresh state with mock bytes.
    
    print("Received event trigger.")
    initial_state = AgentState(
        image_data=b"mock_image_stream",
        audio_data=b"mock_audio_stream",
        vision_analysis=None,
        audio_analysis=None,
        threat_assessment=None,
        action_log=[]
    )
    
    # 2. Invoke Graph
    result = await graph_app.ainvoke(initial_state)
    
    # 3. Return Result
    assessment = result.get("threat_assessment")
    actions = result.get("action_log")
    
    return {
        "status": "processed",
        "threat_level": assessment.threat_level if assessment else "UNKNOWN",
        "actions_taken": actions
    }

async def run_continuous_cycle():
    """
    Simulates a continuous loop of processing.
    """
    while True:
        print("\n--- Starting Cycle ---")
        await process_event()
        await asyncio.sleep(5) # Wait 5 seconds between cycles

# To run the continuous cycle, we would typically use a background task or a separate worker.
# For this demo, we can expose an endpoint to start it.

@app.post("/start_simulation")
async def start_simulation(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_continuous_cycle)
    return {"message": "Simulation started in background."}
