import re
import os
from langchain_community.document_loaders import  PyMuPDFLoader,Docx2txtLoader
from config import FILE_PATH

def clean_text(text):
    
    text = re.sub(r'(\d+)([a-zA-Z])', r'\1 \2', text)
    text = re.sub(r'([a-zA-Z])(\d+)', r'\1 \2', text)

    text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)

    text = re.sub(r'http\S+', ' ', text)

    text = re.sub(r'\S+@\S+', ' ', text)
  
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def load_file(file_path):
    file_extension = os.path.splitext(file_path)[1]
    
    if file_extension.lower() == '.docx' or file_extension.lower() == '.doc':
        loader = Docx2txtLoader(file_path)
        
    elif file_extension.lower() == '.pdf':
        loader = PyMuPDFLoader(file_path)
        
    else:
        raise ValueError("Unsupported file format. Please provide a .pdf or .docx file.")
    
    documents = loader.load()
 
    
    return documents


prompt = """
    You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question.
    If you don't know the answer, just say that you don't know.
    Answer in bullet points. Make sure your answer is relevant to the question and it is answered from the context only.
    Question: {question} 
    Context: {context} 
    Answer:
"""



if __name__ == "__main__":

    documents = load_file(FILE_PATH)
    
    all_text = "\n".join([doc.page_content for doc in documents])
    
    all_text = clean_text(all_text)
    
    print(all_text)