import os
from functools import wraps
import time

# Mock Langfuse client if not available
class MockLangfuse:
    def trace(self, name, **kwargs):
        print(f"[Langfuse] Tracing: {name}")
        return self

    def span(self, name, **kwargs):
        print(f"[Langfuse] Span: {name}")
        return self
    
    def event(self, name, **kwargs):
        print(f"[Langfuse] Event: {name}")
        return self
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

try:
    from langfuse import Langfuse
    # langfuse = Langfuse() # Commented out to avoid auth errors during demo
    langfuse = MockLangfuse()
except ImportError:
    langfuse = MockLangfuse()

def trace_execution(func):
    """
    Decorator to trace function execution with Langfuse.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            duration = time.time() - start_time
            langfuse.event(
                name=func.__name__,
                metadata={"duration": duration, "success": True}
            )
            return result
        except Exception as e:
            duration = time.time() - start_time
            langfuse.event(
                name=func.__name__,
                metadata={"duration": duration, "success": False, "error": str(e)}
            )
            raise e
    return wrapper
