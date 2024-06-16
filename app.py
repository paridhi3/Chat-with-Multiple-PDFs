import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context. Make sure to 
    provide all the details. If the answer is not in the provided context just say, 
    "Answer is not available in the context.". Do not provide the wrong answer.\n\n

    Context:\n {context}?\n
    Question: \n{question}\n

    Answer: """

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()
    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    # Extract the output text from the response
    answer = response["output_text"]

    st.subheader("Answer: ")
    st.write(answer)

    # Append user input and response to chat history
    st.session_state['chat_history'].append(("You", user_question))
    st.session_state['chat_history'].append(("BOT", answer))

def main():
    st.set_page_config("Chat with PDF")
    st.header("Chat with Multiple PDFs")

    # Initialize session state for chat history if it doesn't exist
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Initialize session state for chat history visibility if it doesn't exist
    if 'show_chat_history' not in st.session_state:
        st.session_state['show_chat_history'] = False

    user_question = st.text_input("Ask a question from the PDF files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF files and click on Submit & Process", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done! Feel free to ask your questions now.")

    # Button to toggle chat history visibility
    if st.button("Show Chat History"):
        if not st.session_state['chat_history']:
            st.write("No chat history yet.")
        else:
            st.session_state['show_chat_history'] = not st.session_state['show_chat_history']

    # Only display chat history if the button has been toggled to show
    if st.session_state['show_chat_history'] and st.session_state['chat_history']:
        st.subheader("Chat History:")
        for role, text in st.session_state['chat_history']:
            st.write(f"{role}: {text}")

if __name__ == "__main__":
    main()
