# Chat with Multiple PDFs

Chat with Multiple PDFs is a Streamlit application that enables users to interactively ask questions based on the content of multiple PDF files. It utilizes Google Gemini Pro to provide accurate answers to user queries.

## Features

- **PDF Upload**: Users can upload multiple PDF files containing the information they want to inquire about.

- **Question-Answering**: The application allows users to ask questions related to the content of the uploaded PDF files.

- **Efficient PDF Processing**: Automatically processes uploaded PDF files, extracts text, and creates a vector store for efficient querying using FAISS.

## How to Use

1. **Upload PDF Files**: Use the file uploader to upload one or more PDF files containing the information you want to inquire about.

2. **Submit & Process**: Click the "Submit & Process" button to initiate the processing of the uploaded PDF files. The application will extract text from the PDFs, create a vector store, and prepare for user queries.

3. **Ask Questions**: Once the processing is complete, you can ask questions related to the content of the PDF files in the text input field provided.

4. **View Answers**: The application will generate answers based on the provided context and questions from the PDF files.

## Technologies Used

1. Python
   
2. Streamlit
   
3. PyPDF2
  
4. LangChain
  
5. Google Gemini Pro
  
6. FAISS
