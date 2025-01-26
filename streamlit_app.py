import streamlit as st
from openai import OpenAI
import base64

# Show title and description.
st.title("Police Incident Report Drafter")
st.write(
    "Upload an audio file below, and a police report will be generated! "
)

# Let the user upload a file via `st.file_uploader`.
uploaded_file = st.file_uploader(
    "Upload a document (.mp3 or .wav)", type=("mp3", "wav")
)
uploaded_filed = st.file_uploader("Upload a PDF file", type="pdf")


if uploaded_file and uploaded_filed:
   if uploaded_file and uploaded_filed is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_filed.getbuffer())
    # Embed the PDF using an iframe
    pdf_display = f"""
    <iframe src="/workspaces/document-qa/temp.pdf" width="700" height="1000" type="application/pdf"></iframe>
    """
    st.components.v1.html(pdf_display, height=1000, scrolling=True)
