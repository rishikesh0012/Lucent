# Lucent — Local Document AI (RAG System)

Lucent is a **privacy-first, local Document AI system** that enables users to query PDF documents using **Retrieval-Augmented Generation (RAG)** without relying on cloud-based LLMs.

---

## Problem Statement
Most document-based AI tools rely on cloud APIs, which raises concerns around:
- Data privacy
- Latency
- Cost
- Internet dependency

Organizations handling sensitive documents require an **offline, secure, and low-latency solution** for document question answering.

---

## Solution
Lucent solves this by implementing a **fully local RAG pipeline**:
- PDFs are ingested and chunked locally
- Semantic search is performed using vector embeddings
- Relevant context is retrieved using FAISS
- Answers are generated using a **locally hosted LLM (Mistral via Ollama)**

No data leaves the system.

---

## System Architecture
1. User uploads PDF documents  
2. Text is extracted and chunked  
3. Embeddings are generated and stored in FAISS  
4. User query is embedded and matched semantically  
5. Relevant chunks are passed to the LLM  
6. Context-aware response is generated and returned via API  

---

## AI / ML Details
- **Approach:** Retrieval-Augmented Generation (RAG)
- **Embeddings:** Sentence embeddings
- **Vector Store:** FAISS
- **LLM:** Mistral (served locally via Ollama)
- **Inference:** End-to-end local LLM inference pipeline

---

## Tech Stack
- Python
- FastAPI
- FAISS
- Ollama (Mistral)
- REST APIs

---

## Features
- Offline-first AI system
- Privacy-preserving document querying
- Low-latency semantic search
- REST API-based architecture
- Scalable to multiple documents

---

## ▶️ How to Run
```bash
# Clone the repository
git clone https://github.com/rishikesh0012/Lucent.git
cd Lucent

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn app.main:app --reload
