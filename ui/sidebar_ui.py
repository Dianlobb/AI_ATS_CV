import streamlit as st


def render_sidebar():
    st.sidebar.markdown("""
        ### 📌 How it works
        1. Upload your resume (PDF format)
        2. Enter the target job details
        3. Get instant ATS compatibility analysis
    """)
    st.sidebar.markdown("#### 📤 Upload Resume")
    upload_file = st.sidebar.file_uploader("Upload your CV (PDF format)", type=["pdf"])
    job_role = st.sidebar.text_input("Target Job Position", placeholder="e.g., Senior Software Engineer")
    job_description = st.sidebar.text_area(
        "Job Description",
        placeholder="Paste the job description here...", height=150
    )
    analyze_button = st.sidebar.button("Analyze Resume")
    return upload_file, job_role, job_description, analyze_button