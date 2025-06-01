import os
from dotenv import load_dotenv
import streamlit as st

def validate_environment() -> None:
    """Validate required environment variables."""
    if not os.getenv("OPENAI_API_KEY"):
        st.error("OpenAI API key not found. Please set OPENAI_API_KEY environment variable.")
        st.stop()
    
    if not os.getenv("HR_ASSISTANT_ID"):
        st.error("HR Assistant ID not found. Please set HR_ASSISTANT_ID environment variable.")
        st.stop()


def initialize_app():
    load_dotenv()
    st.set_page_config(page_title="ATS-CV", page_icon="🕵️", layout="wide")
    validate_environment()