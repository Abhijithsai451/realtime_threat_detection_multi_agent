import pytest
from schemas import VisionEvent, AudioEvent
from simulator import simulate_video_frame, simulate_audio_chunk
import time
import sys
import os

# Add current directory to path so imports work
sys.path.append(os.getcwd())

def test_imports():
    import torch
    import fastapi
    import pydantic
    assert True

def test_schemas():
    ve = VisionEvent(
        timestamp=time.time(),
        source="camera_01",
        detected_objects=["person"],
        anomalies=[],
        frame_id=1
    )
    assert ve.source == "camera_01"

    ae = AudioEvent(
        timestamp=time.time(),
        source="mic_01",
        detected_sounds=["glass_break"],
        decibel_level=85.5,
        chunk_id=1
    )
    assert ae.decibel_level == 85.5

def test_simulator():
    frame = simulate_video_frame()
    assert frame.shape == (720, 1280, 3)
    
    audio = simulate_audio_chunk()
    assert len(audio) == 16000
