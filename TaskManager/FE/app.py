import streamlit as st
st.header("Agentic Git Documentation Assistant")

st.write(f"This application helps you with Git repository documentation using AI-powered agents. Provide the URL of your Git repository below to get started.")
repo_url = st.text_input("Enter Git Repository URL", key="repo_url",placeholder="Enter Git repo URL here...")

docs = st.Page("docs/view_docs.py", title="Documents", icon=":material/settings:")

st.logo("assets/img/holla_logo.png", icon_image="assets/img/holla_logo.png")