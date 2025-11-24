from state import AgentState
from models import get_vision_model, get_audio_model
from schemas import VisionEvent, AudioEvent, ThreatAssessment
import torch
import random

def vision_node(state: AgentState) -> AgentState:
    """
    Analyzes image data using the Vision Transformer.
    """
    print("--- Vision Node ---")
    image_data = state.get("image_data")
    
    model, processor = get_vision_model()
    
    # Mocking inference if model loading failed or for prototype speed
    if model is None or image_data is None:
        print("Vision model not available or no data, returning mock event.")
        vision_event = VisionEvent(
            timestamp=0.0,
            source="camera_01",
            detected_objects=["person", "backpack"] if random.random() > 0.5 else ["empty_hallway"],
            anomalies=["unattended_bag"] if random.random() > 0.8 else [],
            frame_id=101
        )
    else:
        # TODO: Implement actual inference logic
        # inputs = processor(images=image_data, return_tensors="pt")
        # outputs = model(**inputs)
        # logits = outputs.logits
        # predicted_class_idx = logits.argmax(-1).item()
        # ... map to labels ...
        print("Running actual inference (placeholder logic)")
        vision_event = VisionEvent(
            timestamp=0.0,
            source="camera_01",
            detected_objects=["person"],
            anomalies=[],
            frame_id=101
        )

    return {"vision_analysis": vision_event}

def audio_node(state: AgentState) -> AgentState:
    """
    Analyzes audio data using Wav2Vec.
    """
    print("--- Audio Node ---")
    audio_data = state.get("audio_data")
    
    model, processor = get_audio_model()
    
    if model is None or audio_data is None:
        print("Audio model not available or no data, returning mock event.")
        audio_event = AudioEvent(
            timestamp=0.0,
            source="mic_01",
            detected_sounds=["footsteps"] if random.random() > 0.5 else ["silence"],
            decibel_level=45.0,
            chunk_id=202
        )
    else:
        # TODO: Implement actual inference logic
        print("Running actual inference (placeholder logic)")
        audio_event = AudioEvent(
            timestamp=0.0,
            source="mic_01",
            detected_sounds=["glass_breaking"],
            decibel_level=80.0,
            chunk_id=202
        )

    return {"audio_analysis": audio_event}

def aggregator_node(state: AgentState) -> AgentState:
    """
    Aggregates findings and assesses threat level using an LLM (mocked for now).
    """
    print("--- Aggregator Node ---")
    vision = state.get("vision_analysis")
    audio = state.get("audio_analysis")
    
    # Simple heuristic logic to simulate LLM reasoning
    threat_level = "LOW"
    reasoning = "Normal activity detected."
    actions = []
    confidence = 0.9

    if vision and "unattended_bag" in vision.anomalies:
        threat_level = "MEDIUM"
        reasoning = "Unattended bag detected in visual feed."
        actions = ["alert_security", "monitor_camera"]
    
    if audio and "glass_breaking" in audio.detected_sounds:
        threat_level = "HIGH"
        reasoning = "Glass breaking sound detected."
        actions = ["trigger_alarm", "lockdown_zone"]
        
    if vision and audio:
        if "person" in vision.detected_objects and "footsteps" in audio.detected_sounds:
             reasoning += " Person walking detected."

    assessment = ThreatAssessment(
        threat_level=threat_level,
        reasoning=reasoning,
        actions=actions,
        confidence=confidence
    )
    
    return {"threat_assessment": assessment}

def action_node(state: AgentState) -> AgentState:
    """
    Executes actions based on the threat assessment.
    """
    print("--- Action Node ---")
    assessment = state.get("threat_assessment")
    action_log = []
    
    if assessment and assessment.actions:
        print(f"Executing actions for threat level: {assessment.threat_level}")
        for action in assessment.actions:
            # Simulate action execution
            print(f" >> EXECUTING: {action}")
            action_log.append(f"Executed: {action}")
    else:
        print("No actions to execute.")
        
    return {"action_log": action_log}
