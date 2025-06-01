import streamlit as st

def display_results(response_list):
    st.subheader("Analysis Results:")
    scrollable_container = """
        <div class=\"scrollable-container\">
            {content}
        </div>
    """
    combined = "<br>".join(response_list)
    st.markdown(scrollable_container.format(content=combined), unsafe_allow_html=True)