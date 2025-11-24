import numpy as np
import time

def simulate_video_frame(height=720, width=1280, channels=3):
    """Simulates a video frame as a random numpy array."""
    return np.random.randint(0, 256, (height, width, channels), dtype=np.uint8)

def simulate_audio_chunk(duration_sec=1, sample_rate=16000):
    """Simulates an audio chunk as a random numpy array."""
    return np.random.uniform(-1.0, 1.0, int(duration_sec * sample_rate))
