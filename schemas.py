from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class MultimodalEvent(BaseModel):
    timestamp: float
    source: str

class VisionEvent(MultimodalEvent):
    detected_objects: List[str]
    anomalies: List[str]
    frame_id: int

class AudioEvent(MultimodalEvent):
    detected_sounds: List[str]
    decibel_level: float
    chunk_id: int

class ThreatAssessment(BaseModel):
    threat_level: str
    reasoning: str
    actions: List[str]
    confidence: float
