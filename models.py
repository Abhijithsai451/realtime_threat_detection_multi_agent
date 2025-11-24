from transformers import ViTForImageClassification, ViTImageProcessor, Wav2Vec2ForCTC, Wav2Vec2Processor
import torch

# Global cache for models to avoid reloading
_VISION_MODEL = None
_VISION_PROCESSOR = None
_AUDIO_MODEL = None
_AUDIO_PROCESSOR = None

def get_vision_model():
    """Loads and returns the Vision Transformer model and processor."""
    global _VISION_MODEL, _VISION_PROCESSOR
    if _VISION_MODEL is None:
        print("Loading Vision Model (ViT)...")
        # In a real scenario, we would load 'google/vit-base-patch16-224'
        # For this prototype, we might want to mock it or load a tiny version if available.
        # Proceeding with standard loading but wrapped in try-except to handle missing internet/auth.
        try:
            _VISION_PROCESSOR = ViTImageProcessor.from_pretrained("google/vit-base-patch16-224")
            _VISION_MODEL = ViTForImageClassification.from_pretrained("google/vit-base-patch16-224")
        except Exception as e:
            print(f"Error loading Vision Model: {e}")
            return None, None
    return _VISION_MODEL, _VISION_PROCESSOR

def get_audio_model():
    """Loads and returns the Wav2Vec model and processor."""
    global _AUDIO_MODEL, _AUDIO_PROCESSOR
    if _AUDIO_MODEL is None:
        print("Loading Audio Model (Wav2Vec2)...")
        try:
            _AUDIO_PROCESSOR = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
            _AUDIO_MODEL = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
        except Exception as e:
            print(f"Error loading Audio Model: {e}")
            return None, None
    return _AUDIO_MODEL, _AUDIO_PROCESSOR
