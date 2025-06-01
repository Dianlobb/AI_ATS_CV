import streamlit as st
from config import initialize_app
from ui.header_ui import render_header
from ui.sidebar_ui import render_sidebar
from services.analysis_service import process_resume
from utils.logging_setup import logger

# Inicializar configuración y entorno
initialize_app()

# Renderizar UI
render_header()
upload_file, job_role, job_description, analyze_button = render_sidebar()

if upload_file and analyze_button:
    try:
        with st.spinner('🔄 Processing your resume... Please wait.'):
            response = process_resume(upload_file, job_role, job_description)
            
        with st.spinner('📊 Displaying results...'):
            from ui.result_ui import display_results
            display_results(response)
            
    except Exception as e:
        logger.error(f"Error en procesamiento: {str(e)}")
        st.error("Ocurrió un error durante el análisis. Por favor, inténtalo de nuevo.")