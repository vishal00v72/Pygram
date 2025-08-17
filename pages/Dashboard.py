import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide") # Important: Use this on all pages for consistency

st.title("📊 Data Profile Report")
st.write("Explore the dataset used for model training.")

file_path = r'C:\Users\uniqu\PYkalp\pages\churnA.html'


try:
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    components.v1.html(html_content, height=800, scrolling=True)

except FileNotFoundError:
    st.error("Error: 'churnA.html' not found.")
