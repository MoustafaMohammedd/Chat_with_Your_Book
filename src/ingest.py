from embedder import model
from config import FILE_PATH, VECTOR_STORE_PATH
from utils import load_file, clean_text
from langchain_text_splitters import  RecursiveCharacterTextSplitter
import faiss
from langchain_community.vectorstores import FAISS 
from langchain.schema import Document
  


def create_vector_store_of_chunkes(file_path, model, output_path):
    
    documents = load_file(file_path)
    all_text = "\n".join([doc.page_content for doc in documents])
    
    cleaned_text = clean_text(all_text)

    with open("data/processed/cleaned_text.txt", "w", encoding="utf-8") as f:
        f.write(cleaned_text)
        
    cleaned_documents = [
    Document(page_content=clean_text(doc.page_content), metadata=doc.metadata)
    for doc in documents
                        ]
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(cleaned_documents)
    reviews_vector_db = FAISS.from_documents(chunks, model)
    reviews_vector_db.save_local(output_path)
    
    print(f"Vector store created and saved to {output_path}")
  
  
if __name__ == "__main__":
    
    create_vector_store_of_chunkes(file_path=FILE_PATH, model=model, output_path=VECTOR_STORE_PATH)