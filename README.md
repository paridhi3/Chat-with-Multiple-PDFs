# [Chat with Multiple PDFs](https://paridhi3-chat-with-multiple-pdfs-app-oseph5.streamlit.app/)

Chat with Multiple PDFs is a Streamlit application that enables users to interactively ask questions based on the content of multiple PDF files. It utilizes various natural language processing and generative AI techniques to provide accurate answers to user queries.

## Features

1. **PDF Upload**: Users can upload multiple PDF files containing the information they want to inquire about.

2. **Question-Answering**: The application allows users to ask questions related to the content of the uploaded PDF files.

3. **Conversational AI**: Utilizes conversational AI powered by Google GenerativeAI to generate responses to user queries based on the provided PDF context.

4. **Efficient PDF Processing**: Automatically processes uploaded PDF files, extracts text, and creates a vector store for efficient querying.

5. **Chat History**: The application keeps a record of the conversation between the user and the AI model, allowing users to review previous interactions.

## How to Use

1. **Upload PDF Files**: Use the file uploader to upload one or more PDF files containing the information you want to inquire about.

2. **Submit & Process**: Click the "Submit & Process" button to initiate the processing of the uploaded PDF files. The application will extract text from the PDFs, create a vector store, and prepare for user queries.

3. **Ask Questions**: Once the processing is complete, you can ask questions related to the content of the PDF files in the text input field provided.

4. **View Answers**: The application will generate answers based on the provided context and questions from the PDF files.

5. **Show Chat History**: Click the "Show Chat History" button to show or hide the chat history. The chat history records all interactions between the user and the AI model.

## Technologies Used

1. Python

2. Streamlit

3. PyPDF2

4. LangChain

5. Google Gemini Pro

6. FAISS (Facebook AI Similarity Search)

