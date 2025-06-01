from functools import wraps
import time
import streamlit as st

def safe_api_call(func):
    """Decorator to handle API calls with retries and error handling.
    
    Args:
        func: The function to wrap
        
    Returns:
        The wrapped function with retry logic
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        max_retries = 3
        retry_delay = 1
        
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == max_retries - 1:
                    st.error(f"API call failed after {max_retries} attempts: {str(e)}")
                    raise
                time.sleep(retry_delay * (attempt + 1))
    return wrapper