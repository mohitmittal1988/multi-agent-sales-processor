import streamlit as st
import requests

st.title("Multi-Agent Sales Query")

st.markdown("Ask questions about sales data using our AI-powered system.")

query = st.text_input("Enter your question:", placeholder="e.g., What were total sales in Q1?")

if st.button("Ask"):
    if query:
        with st.spinner("Processing your query..."):
            try:
                response = requests.post("http://mcp:9000/process", json={"query": query}, timeout=30)
                response.raise_for_status()
                result = response.json()
                st.success("Response:")
                st.write(result.get("result", "No result"))
            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")

st.markdown("---")
st.markdown("**Note:** This app queries a RAG system with vector database and LLM.")