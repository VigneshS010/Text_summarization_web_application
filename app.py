import streamlit as st
from newspaper import Article
import PyPDF2
from transformers import pipeline, T5Tokenizer

# Load the summarization pipeline and tokenizer (T5)
@st.cache_resource
def load_summarizer():
    summarizer = pipeline('summarization', model='google/long-t5-tglobal-base')
    tokenizer = T5Tokenizer.from_pretrained('google/long-t5-tglobal-base')
    return summarizer, tokenizer

summarizer, tokenizer = load_summarizer()

st.title("Text Summarization App")

source = st.radio("Select Text Source", ("URL", "PDF", "Manual Text Input"))

if source == "URL":
    url = st.text_input("Enter URL")
    if st.button("Summarize"):
        try:
            article = Article(url)
            article.download()
            article.parse()
            text = article.text

            tokens = tokenizer.encode(text, return_tensors='pt')
            max_length = 1024
            if tokens.shape[1] > max_length:
                tokens = tokens[:, :max_length]
                text = tokenizer.decode(tokens[0], skip_special_tokens=True)

            summary = summarizer(text, max_length=250, min_length=50, do_sample=False)
            st.write("Summary:")
            st.write(summary[0]['summary_text'])

        except Exception as e:
            st.error(f"An error occurred: {e}")

elif source == "PDF":
    uploaded_file = st.file_uploader("Upload PDF file", type="pdf")
    if st.button("Summarize") and uploaded_file is not None:
        try:
            def extract_text(pdf_file):
                text = ''
                reader = PyPDF2.PdfReader(pdf_file)
                for page in reader.pages:
                    text += page.extract_text()
                return text

            pdf_text = extract_text(uploaded_file)

            tokens = tokenizer.encode(pdf_text, return_tensors='pt')
            max_length = 1024
            if tokens.shape[1] > max_length:
                tokens = tokens[:, :max_length]
                pdf_text = tokenizer.decode(tokens[0], skip_special_tokens=True)

            summary = summarizer(pdf_text, max_length=250, min_length=50, do_sample=False)
            st.write("Summary:")
            st.write(summary[0]['summary_text'])

        except Exception as e:
            st.error(f"An error occurred: {e}")

elif source == "Manual Text Input":
    text = st.text_area("Enter Text")
    if st.button("Summarize"):
        try:

            tokens = tokenizer.encode(text, return_tensors='pt')
            max_length = 1024
            if tokens.shape[1] > max_length:
                tokens = tokens[:, :max_length]
                text = tokenizer.decode(tokens[0], skip_special_tokens=True)

            summary = summarizer(text, max_length=250, min_length=50, do_sample=False)
            st.write("Summary:")
            st.write(summary[0]['summary_text'])

        except Exception as e:
            st.error(f"An error occurred: {e}")