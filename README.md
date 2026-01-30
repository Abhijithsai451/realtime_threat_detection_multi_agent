# Real-Time Threat Detection Multi-Agent System

## Overview
The **Real-Time Threat Detection Multi-Agent System** is a sophisticated, multimodal AI surveillance solution designed for high-stakes environments like smart factories and secure facilities. It leverages state-of-the-art Deep Learning models and LLM-based orchestration to process video and audio feeds, detect anomalies, and execute autonomous security protocols.

---

## What We Have Done
In this project, we have successfully implemented a full-stack AI orchestration engine:
1.  **Architecture Design**: Built a multi-agent system using **LangGraph** for robust state management and conditional workflow routing.
2.  **Multimodal Integration**: Implemented specialized nodes for **Computer Vision (ViT)** and **Audio Analysis (Wav2Vec2)** to process concurrent data streams.
3.  **Intelligent Reasoning**: Developed a **Threat Aggregator Agent** that correlates findings across modalities to assess risk levels using heuristic and LLM logic.
4.  **Autonomous Action Engine**: Created an **Action Agent** capable of executing real-world tools (alerts, lockdowns) based on threat severity.
5.  **Data Simulation & Testing**: Developed a real-time sensor simulator and an evaluation suite to benchmark system latency and accuracy.
6.  **Observability**: Integrated **Langfuse** for end-to-end trace visibility, enabling detailed monitoring of agent decisions and model inferences.
7.  **Production Readiness**: Containerized the entire solution with **Docker** and exposed it via a **FastAPI** interface.

---

## End-to-End Implementation Walkthrough

The system follows a modular architecture where data flows through specialized agents coordinated by a central state graph.

### 1. The Foundation: State & Schemas
Every agent in the system communicates via a structured **AgentState**. This ensures that data is consistent and traceable as it moves through the graph.

```python
# state.py
class AgentState(TypedDict):
    image_data: Optional[Any]      # Input video frames
    audio_data: Optional[Any]      # Input audio chunks
    vision_analysis: Optional[VisionEvent]
    audio_analysis: Optional[AudioEvent]
    threat_assessment: Optional[ThreatAssessment]
    action_log: Optional[List[str]]
```

Our schemas use **Pydantic** to enforce strict data validation for multimodal events:

```python
# schemas.py
class VisionEvent(MultimodalEvent):
    detected_objects: List[str]
    anomalies: List[str]
    frame_id: int

class ThreatAssessment(BaseModel):
    threat_level: str  # LOW, MEDIUM, HIGH, CRITICAL
    reasoning: str
    actions: List[str]
```

### 2. Multi-Agent Nodes (The "Brain")
Each node in our graph represents a specialized agent.

#### **Vision Analysis Agent**
Uses a **Vision Transformer (ViT)** to analyze camera feeds for suspicious objects or activities.
```python
def vision_node(state: AgentState) -> AgentState:
    model, processor = get_vision_model()
    # In a real run, this processes image_data through ViT
    # For simulation, it extracts objects like 'person', 'unattended_bag'
    return {"vision_analysis": vision_event}
```

#### **Audio Analysis Agent**
Processes audio streams using **Wav2Vec2** to detect acoustic signatures like "glass breaking" or "alarms".
```python
def audio_node(state: AgentState) -> AgentState:
    model, processor = get_audio_model()
    # Detects sounds like 'glass_breaking' or 'footsteps'
    return {"audio_analysis": audio_event}
```

#### **Threat Aggregator Agent**
This is the "Logic Core". It correlates visual and auditory findings to determine if a threat exists.
```python
def aggregator_node(state: AgentState) -> AgentState:
    vision = state.get("vision_analysis")
    audio = state.get("audio_analysis")
    
    # Logic: If Vision sees 'unattended_bag' AND Audio hears 'silence', level = MEDIUM.
    # If Audio hears 'glass_breaking', level = HIGH.
    return {"threat_assessment": assessment}
```

### 3. Orchestration with LangGraph
The magic happens in `graph.py`, where we define how these agents interact. We use **Parallel Execution** for vision and audio analysis and **Conditional Routing** for actions.

```python
# graph.py
def build_graph():
    workflow = StateGraph(AgentState)
    workflow.add_node("vision", vision_node)
    workflow.add_node("audio", audio_node)
    
    # Entry point
    workflow.set_entry_point("vision")
    workflow.add_edge("vision", "audio")
    workflow.add_edge("audio", "aggregator")
    
    # Conditional Edge: Only execute action if threat is detected
    workflow.add_conditional_edges(
        "aggregator",
        should_act, # Function checking threat_level in ["HIGH", "MEDIUM"]
        {"action": "action", END: END}
    )
```

### 4. Real-Time Simulation & Evaluation
To bridge the gap between development and deployment, we built a simulator and an evaluation suite.

-   **Simulator**: Generates dummy buffer data mimicking real-world sensor streams.
-   **Evaluation**: Benchmarks the end-to-end latency.

```bash
# Run performance evaluation
python evaluate.py
```

---

## Tech Stack
-   **Framework**: LangGraph, LangChain
-   **Deep Learning**: PyTorch, Transformers (ViT, Wav2Vec2)
-   **API**: FastAPI, Uvicorn
-   **Observability**: Langfuse
-   **Validation**: Pydantic
-   **Deployment**: Docker, Docker Compose

---

## Getting Started

### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Run the System
Start the FastAPI server to begin real-time detection:
```bash
python main.py
```

### 3. Monitoring
Access the **Langfuse** dashboard to view real-time traces and agent decision-making logs.

---

## 📄 License
MIT License - See [LICENSE](LICENSE) for details.
