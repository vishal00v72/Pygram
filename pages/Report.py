import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide", page_title="Report|Churn prediction MLWA", page_icon="🎰") 

st.title("📊 Data Profile Report")
st.write("Explore the dataset used for model training.")


file_path = 'pages/churnA.html' 


if os.path.exists(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        components.html(html_content, height=800, scrolling=True)

    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")
else:
    st.error(f"Error: The file '{file_path}' was not found.")
    st.info("Please verify the file path and directory structure are correct.")
