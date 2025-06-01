import os
import time
from random import randint
from openai import OpenAI
from utils.retry import safe_api_call
import streamlit as st
from functools import wraps

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
HR_ASSISTANT_ID = os.getenv("HR_ASSISTANT_ID") 


@st.cache_resource
def get_openai_client():
    return openai_client    

@safe_api_call
def submit_message(assistant_id, thread, user_message, attachment_id):
    client = get_openai_client()
    client.beta.threads.messages.create(
        thread_id=thread.id, 
        role="user", 
        content=user_message, 
        attachments=[{"file_id": attachment_id, "tools": [{"type": "code_interpreter"}]}]
    )
    return client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )

@safe_api_call
def create_thread_and_run(user_input, attachment_id):
    """Create a thread and run with proper error handling."""
    try:
        # Create thread first
        thread = get_openai_client().beta.threads.create()
        
        # Then submit message with all required arguments
        run = submit_message(
            assistant_id=HR_ASSISTANT_ID,
            thread=thread,
            user_message=user_input,
            attachment_id=attachment_id
        )
        
        return thread, run
    except Exception as e:
        st.error(f"Failed to create thread and run: {str(e)}")
        raise

def wait_on_run(run, thread, timeout=300):  # 5 minutes timeout by default
    start_time = time.time()
    
    while run.status == "queued" or run.status == "in_progress":
        if time.time() - start_time > timeout:
            raise TimeoutError(f"Analysis timed out after {timeout} seconds")
            
        try:
            run = get_openai_client().beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id,
            )
        except Exception as e:
            st.error(f"Error while checking analysis status: {str(e)}")
            raise
            
        if run.status == "failed":
            st.error("Analysis failed. Please try again.")
            raise Exception("Run failed with status: " + run.status)
            
        time.sleep(min(5, 0.5 * randint(20, 30)))  # Sleep for a short time before checking again
    
    return run

@safe_api_call
def upload_file_to_assistant(file):
    return get_openai_client().files.create(
        file=file,
        purpose="assistants",
    )

@safe_api_call
def get_response(thread):
    messages = get_openai_client().beta.threads.messages.list(thread_id=thread.id, order="asc")
    return [message.content[0].text.value for message in messages if message.role == "assistant"]

