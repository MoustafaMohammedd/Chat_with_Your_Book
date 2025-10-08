from langchain.embeddings import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv(".env")
import os


embedd_model_name=os.getenv("EMBEDD_MODEL_NAME")

model = HuggingFaceEmbeddings(model_name=embedd_model_name)




