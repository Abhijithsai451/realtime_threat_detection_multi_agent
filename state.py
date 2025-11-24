from typing import TypedDict, List, Optional, Any
from schemas import VisionEvent, AudioEvent, ThreatAssessment

class AgentState(TypedDict):
    image_data: Optional[Any] # Placeholder for actual image data (e.g., numpy array or bytes)
    audio_data: Optional[Any] # Placeholder for actual audio data
    vision_analysis: Optional[VisionEvent]
    audio_analysis: Optional[AudioEvent]
    threat_assessment: Optional[ThreatAssessment]
    action_log: Optional[List[str]]
