import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from config import FILE_PATH, VECTOR_STORE_PATH
from utils import prompt
from retriever import get_retriever
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough 
from langchain_core.prompts import ChatPromptTemplate


from dotenv import load_dotenv
load_dotenv(".env")

api_key=os.getenv("API_KEY")
base_url=os.getenv("BASE_URL")
model_name=os.getenv("MODEL_NAME")

llm=ChatOpenAI(api_key=api_key,model=model_name,base_url=base_url)

def format_docs(docs):
    return '\n\n'.join([doc.page_content for doc in docs])




def ask_your_book(question, vector_store_path=VECTOR_STORE_PATH, prompt=prompt):
    
    retriever=get_retriever(vector_store_path=vector_store_path,search_type='score', n_k=3, nf_k=10)

    prompt_t = ChatPromptTemplate.from_template(prompt)

    rag_chain = (
    {"context": retriever|format_docs, "question": RunnablePassthrough()}
    | prompt_t
    | llm
    | StrOutputParser()
                )
    
    return rag_chain.invoke(question)


if __name__ == "__main__":
    question = "What is the main point of this document?"
    answer = ask_your_book(question)
    print("Answer:", answer)