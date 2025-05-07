import streamlit as st
import config.gemini_config
from utils.summarizer import summarize_text

st.set_page_config(page_title="AI-Powered Text Summarizer", layout="wide")
st.title("AI-Powered Text Summarizer")
st.write("Paste your text below and click **Summarize**.")

user_input = st.text_area("Input Text", height=300)

if st.button("Summarize"):
    if not user_input.strip():
        st.error("Please enter some text to summarize.")
    else:
        with st.spinner("Generating summary…"):
            summary = summarize_text(user_input)
        if summary.startswith("Error:"):
            st.error(summary)
        else:
            st.subheader("Summary")
            st.write(summary)
