import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.config import VECTOR_STORE_PATH
from src.retriever import get_retriever

def test_get_retriever(query):
    retriever = get_retriever(vector_store_path=VECTOR_STORE_PATH,search_type='score', n_k=3, nf_k=10)
    output_docs=retriever.invoke(query)
    return output_docs

if __name__ == "__main__":
    
    query="what is the main point of this document?"
    
    docs=test_get_retriever(query)
    for doc in docs:
        print(doc)