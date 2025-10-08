# 📚 Chat with Your Book

**Chat with Your Book** is an AI-powered **Retrieval-Augmented Generation (RAG)** system built using **FastAPI** and **LangChain**.  
It allows you to upload any book or report (PDF/DOCX), create vector embeddings using a transformer model, and then **ask natural language questions** — with accurate, context-based answers retrieved directly from your book.

---

## 🚀 Key Features

- 📘 **Upload any book/document** (PDF or DOCX)
- 🧩 **Automatic text cleaning and chunking**
- 🧠 **Embedding generation** using Sentence Transformers
- 🔍 **Semantic retrieval** with FAISS vector database
- 💬 **RAG pipeline** combining retriever + LLM (via OpenRouter or OpenAI)
- ⚡ **FastAPI backend** — lightweight, modular, and production-ready
- 🧪 Includes **test scripts** for retriever and generator

---

## 🏗️ Project Structure

```

Chat_with_Your_Book/
│
├── data/
│   ├── raw/                         # Original input files (PDF, DOCX)
│   ├── processed/                   # Cleaned and chunked text
│   └── embeddings/                  # Stored FAISS vector database
│
├── notebooks/
│   └── exploration.ipynb            # Optional notebook for testing embeddings
│
├── src/
│   ├── **init**.py
│   ├── config.py                    # Global constants and file paths
│   ├── embedder.py                  # Embedding model initialization
│   ├── generator.py                 # RAG pipeline logic
│   ├── ingest.py                    # Ingests, cleans, chunks, and embeds documents
│   ├── retriever.py                 # Loads and queries FAISS vector store
│   ├── utils.py                     # Cleaning, file loading, and QA prompt template
│   └── main.py                      # FastAPI server with all endpoints
│
├── tests/
│   ├── test_generator.py            # Unit test for RAG generator
│   └── test_retriever.py            # Unit test for retriever
│
├── .env.example                     # Example environment variables
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/MoustafaMohammedd/Chat_with_Your_Book.git
cd Chat_with_Your_Book
````

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set up your environment variables

Copy `.env.example` → `.env` and add your keys:

```bash
API_KEY="your_api_key_here"
BASE_URL="https://openrouter.ai/api/v1"
MODEL_NAME="openai/gpt-oss-20b:free"
EMBEDD_MODEL_NAME="sentence-transformers/all-MiniLM-L6-v2"
```

> You can use [OpenRouter](https://openrouter.ai) or OpenAI API.

---
Start the FastAPI app:

```bash
uvicorn src.main:app --reload
```

Access the **interactive API docs** at:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧠 Workflow Overview

1. **Ingest**: Upload and process your document.
   → Cleans text, splits into chunks, and creates embeddings.
2. **Retrieve**: Find the most relevant document chunks for a given query.
3. **Generate**: The retriever context + user question are sent to an LLM to produce an accurate answer.

---


## ⚡ FastAPI Endpoints

### **1️⃣ Root Endpoint**

`GET /`

```json
{
  "message": "Welcome to the Chat_with_Your_Book Query API!"
}
```

---

### **2️⃣ Ingest Document**

`POST /ingest`

```json
{
  "input_file_path": "data/raw/economic-and-investment-monitor-Q4-2022-english.pdf",
  "output_vector_store_path": "data/embeddings/vector_store"
}
```

✅ **Creates and saves FAISS embeddings** for your document.

---

### **3️⃣ Retrieve Chunks**

`POST /retriever_output`

```json
{
  "query": "What is the main point of this document?",
  "vector_store_path": "data/embeddings/vector_store",
  "search_type": "score",
  "n_k": 3,
  "nf_k": 10
}
```

✅ Returns relevant document chunks for your query.

---

### **4️⃣ Ask Your Book**

`POST /ask_your_book`

```json
{
  "question": "What are the key economic insights in Q4 2022?",
  "vector_store_path": "data/embeddings/vector_store"
}
```

✅ Returns an **LLM-generated answer** using retrieved context.

---

## 🧪 Running the API

Start the FastAPI app:

```bash
uvicorn src.main:app --reload
```

Access the **interactive API docs** at:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧠 Example Query Flow

1. Run `/ingest` once to build the vector store.
2. Use `/ask_your_book` for any number of questions.
3. The API fetches top relevant chunks + LLM answer.

---

## 🧪 Tests

### Run tests manually:

```bash
python tests/test_retriever.py
python tests/test_generator.py
```

### Example output:

```
Answer: The main point of this document is...
```

---


## 📚 Example File Used

Located in `data/raw/`:

```
economic-and-investment-monitor-Q4-2022-english.pdf
```

---

## 🔮 Future Enhancements

* 🧩 Add conversation memory (multi-turn RAG)
* 🔐 Add authentication and user management
* 🌐 Add **UI** for easy upload and visualization

---
