import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from embedder import model
from config import FILE_PATH, VECTOR_STORE_PATH
from langchain_community.vectorstores import FAISS



def load_vector_store(output_path):
    reviews_vector_db = FAISS.load_local(
        output_path, model,allow_dangerous_deserialization=True)
    
    return reviews_vector_db


def get_retriever(vector_store_path=VECTOR_STORE_PATH,search_type='mmr', n_k=3, nf_k=10):
    
    reviews_vector_db=load_vector_store(output_path=vector_store_path)

    if search_type == 'mmr':
        retriever = reviews_vector_db.as_retriever(search_type = 'mmr', 
                                            search_kwargs = {'k': n_k, 'fetch_k': nf_k})
    else:
        retriever = reviews_vector_db.as_retriever(search_type = 'similarity', 
                                            search_kwargs = {'k': n_k})
        
    return retriever


