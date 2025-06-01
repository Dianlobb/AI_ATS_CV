import streamlit as st

def render_header():
    # Cargar estilos desde assets/styles.css
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    st.markdown(
        '<div class="main-header"><h3>AI 🕵️- ATS Resume Scanner</h3></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="description">'
        '📄 Upload your resume and let AI analyze its ATS compatibility.<br>'
        '🎯 Get insights on your resume\'s match with job requirements.<br>'
        '⚡ Receive actionable feedback to improve your chances of getting shortlisted.'
        '</div>',
        unsafe_allow_html=True
    )