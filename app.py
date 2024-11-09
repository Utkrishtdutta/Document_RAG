import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from utils import parse_pdf, text_to_docs, embed_docs

st.title("Document RAG")

embeddings = HuggingFaceEmbeddings()

model = ChatOllama(
    model="llama3.2",
    base_url = "http://localhost:11434"
)

prompt = ChatPromptTemplate.from_template(
    """ You are a Q/A expert and you just need to take refrence of given documents to structure 
     a response for the given question. If you don't find any relevent reference in documents 
     reqarding the question just return 'I don't know the answer as not sufficient information 
     provided in the PDF'?\n\n
     Document 1: {context1}\n
     Document 2: {context2}\n
     Question: {question}\n """
)

uploaded_files = st.file_uploader("Choose a PDF file", type='pdf')

if uploaded_files:
    text = parse_pdf(uploaded_files)
    docs = text_to_docs(text)
    faiss_index = embed_docs(text)
    input = st.chat_input("Enter the question")
    if input:
        docs_page = faiss_index.similarity_search(input, k = 2)
        st.write(docs_page)
        chain = prompt | model | StrOutputParser()
        output = chain.invoke({"context1" : docs_page[0].page_content,
                               "context2" : docs_page[1].page_content,
                                "question" : input})
        st.write(output)
