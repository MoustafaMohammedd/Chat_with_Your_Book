import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from pydantic import BaseModel
from generator import ask_your_book
from ingest import create_vector_store_of_chunkes
from config import FILE_PATH, VECTOR_STORE_PATH
from embedder import model

from retriever import get_retriever



app = FastAPI()

class QueryRequest(BaseModel):
    question: str = "What is the main point of this document?"
    vector_store_path: str = VECTOR_STORE_PATH
    
    
class IngestRequest(BaseModel):
    input_file_path: str = FILE_PATH
    output_vector_store_path: str = VECTOR_STORE_PATH
    
class SetRetrieverRequest(BaseModel):
    
    query: str = "What is the main point of this document?"
    vector_store_path: str = VECTOR_STORE_PATH
    search_type: str = 'score'
    n_k: int = 3
    nf_k: int = 10
    

@app.get("/")
def read_root():
    return {"message": "Welcome to the Chat_with_Your_Book Query API!"}

@app.post("/ingest")
def ingest_book(request: IngestRequest):
    create_vector_store_of_chunkes(file_path=request.input_file_path, model=model, output_path=request.output_vector_store_path)
    return {"message": f"Document ingested and vector store created at {request.output_vector_store_path}"}

@app.post("/retriever_output")
def retriever_output(request: SetRetrieverRequest):
    retriever = get_retriever(vector_store_path=request.vector_store_path, search_type=request.search_type, n_k=request.n_k, nf_k=request.nf_k)
    output_docs = retriever.invoke(request.query)
    return {"documents": [doc.page_content for doc in output_docs]}


@app.post("/ask_your_book")
def ask_book(request: QueryRequest):
    answer = ask_your_book(question=request.question, vector_store_path=request.vector_store_path)
    return {"answer": answer}


  





   
    
    
    