# Real-Time Threat Detection Multi-Agent System

## Overview
This project implements a sophisticated real-time surveillance agent designed for environments such as smart factories or home security systems. It combines deep learning models for computer vision and audio analysis with Large Language Models (LLMs) to detect anomalies, assess threats, and execute appropriate actions in real-time.

## Key Features
- **Multimodal AI Integration**: Synergizes outputs from Vision (CNN/Transformer) and Audio (Spectrogram CNN) models for comprehensive situational awareness.
- **Intelligent Threat Assessment**: Utilizes an LLM-based agent to correlate multimodal events and reason about potential threats.
- **Autonomous Action**: Features an Action Agent that triggers specific protocols (e.g., alerts, system shutdowns) based on the severity of the assessment.
- **Robust Orchestration**: Built on **LangGraph** to manage complex agent workflows and state transitions.
- **Observability & Monitoring**: Integrated with **Langfuse** for full trace visibility and latency tracking.
- **Production Ready**: Fully containerized with **Docker** and exposed via a **FastAPI** interface.

## System Architecture
The system is composed of four main nodes orchestrated by a state graph:

1.  **Vision Analysis Node**: Processes video frames to identify objects, unsafe acts, or visual anomalies.
2.  **Audio Analysis Node**: Analyzes audio streams to detect specific sounds like machinery faults or breaking glass.
3.  **Threat Assessment Agent**: Receives structured data from both vision and audio nodes. It uses complex reasoning to determine the threat level (e.g., correlating a "fall" detected by vision with a "crash" detected by audio).
4.  **Action Agent**: Executes tool calls based on the final threat assessment (Low, Medium, High, Critical).

## Project Structure
- `nodes.py`: Defines the core logic for Vision, Audio, Threat Assessment, and Action nodes.
- `graph.py`: Sets up the LangGraph state machine and orchestration logic.
- `models.py`: Handles loading of deep learning models (simulated or real).
- `simulator.py`: Provides simulated real-time video and audio data for testing.
- `schemas.py`: Defines Pydantic models for structured data exchange.
- `main.py`: FastAPI entry point for the application.
- `observability.py`: Configuration for Langfuse integration.
- `evaluate.py`: Evaluation suite for benchmarking system performance.

## Getting Started

### Prerequisites
- Python 3.10+
- Docker (optional, for containerized deployment)

### Installation

1.  **Clone the repository**
    ```bash
    git clone <repository-url>
    cd realtime_threat_detection_multi_agent
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Setup**
    Ensure you have the necessary API keys (e.g., OpenAI, Langfuse) set in your environment variables or a `.env` file.

### Running the Application

**Local Execution:**
To run the system locally with simulated data:
```bash
python main.py
```

**Using Docker:**
To build and run the containerized application:
```bash
docker-compose up --build
```

## Usage
Once running, the system will start processing simulated sensor data. You can interact with the API (default at `http://localhost:8000`) to trigger specific scenarios or view the current state.

## Evaluation
To run the evaluation suite and benchmark the agents:
```bash
python evaluate.py
```

## License
[MIT License](LICENSE)
