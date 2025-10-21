import streamlit as st
from PyPDF2 import PdfReader
from cohere_chat import chat_with_pdf

st.set_page_config(page_title="PDF Chatbot", page_icon="🤖")
st.title("📄 PDF Chatbot with Cohere")

# 1️⃣ Upload PDF
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file:
    # Read PDF content
    reader = PdfReader(uploaded_file)
    pdf_text = ""
    for page in reader.pages:
        pdf_text += page.extract_text() + "\n"

    st.success("PDF loaded successfully!")

    # 2️⃣ Input box for questions
    question = st.text_area("Ask a question about your PDF:")

    # 3️⃣ Button to submit question
    if st.button("Get Answer"):
        if question.strip() != "":
            with st.spinner("Generating answer..."):
                answer = chat_with_pdf(question, pdf_text)
            st.markdown("**Answer:**")
            st.write(answer)
        else:
            st.warning("Please type a question first.")
