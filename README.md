#  Lucent

ocused intelligence from your documents

A local-first Document AI system that lets you upload PDFs and chat with them using Retrieval-Augmented Generation (RAG).

Private • Local • Explainable • Fast

## 📁 Project Structure

```text
lucent/
├── frontend/              # Next.js frontend (UI)
├── backend/               # FastAPI backend (RAG pipeline)
├── images/                # Screenshots & demo images
└── README.md

frontend/
├── app/
│   ├── page.tsx           # Main chat interface (Lucent UI)
│   ├── layout.tsx         # Global layout & metadata
│   └── globals.css        # Global styles
│
├── components/
│   ├── ChatInput.tsx      # Chat input field
│   ├── Message.tsx        # Chat message renderer (Markdown + streaming)
│   ├── UploadBox.tsx      # PDF upload component
│   └── PromptCards.tsx    # Suggested prompt cards
│
├── lib/
│   └── api.ts             # Backend API calls (streaming support)
│
├── package.json           # Frontend dependencies
└── tsconfig.json


backend/
├── main.py                # FastAPI app & API routes
├── rag.py                 # Retrieval-Augmented Generation logic
├── ingest.py              # PDF ingestion & vector store creation
├── requirements.txt       # Python dependencies
│
├── docs/                  # Uploaded PDF files
└── vectorstore/           # FAISS vector index storage

What is Lucent?

Lucent is a privacy-focused Document Question-Answering application that runs completely on your local machine.

Unlike cloud-based AI tools, Lucent:
	•	Keeps your documents private
	•	Uses Retrieval-Augmented Generation (RAG) to reduce hallucinations
	•	Streams responses in real time
	•	Answers questions using only your uploaded documents

Lucent is ideal for:
	•	Research papers
	•	Technical documentation
	•	Resumes & reports
	•	Learning modern RAG systems

⸻

 Features
	•	📄 Upload PDF documents
	•	💬 Chat with documents using natural language
	•	🧠 RAG pipeline with FAISS vector search
	•	⚡ Streaming responses (ChatGPT-style typing)
	•	🧾 Markdown & code block rendering
	•	🎨 Clean, minimalist UI
	•	🔒 Fully local — no cloud APIs

⸻

How It Works (RAG Flow)

PDF Upload
   ↓
Text Extraction (PyPDF)
   ↓
Chunking + Embeddings (Ollama)
   ↓
FAISS Vector Store
   ↓
User Question
   ↓
Relevant Chunks Retrieved
   ↓
LLM Generates Grounded Answer (Streaming)


Lucent ensures responses are grounded in document content, not hallucinated.

⸻

Tech Stack

Frontend
	•	Next.js (App Router)
	•	TypeScript
	•	Tailwind CSS
	•	React Markdown

Backend
	•	FastAPI
	•	LangChain
	•	FAISS
	•	Ollama (Mistral)

⸻

⚙️ Prerequisites

Install the following before running Lucent:
	•	Node.js (v18+)
	•	Python (3.10+ recommended)
	•	Ollama

Install Ollama: https://ollama.com
Pull model - ollama pull mistral

Backend Setup
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
http://localhost:8000
http://localhost:8000/docs

Frontend Setup
cd frontend
npm install
npm run dev
http://localhost:3000

How to Use
	1.	Start Ollama
	2.	Run the backend
	3.	Run the frontend
	4.	Upload a PDF using the UI
	5.	Ask questions such as:
	•	Summarize this document
	•	Explain section 2
	•	Provide examples mentioned in the PDF

Responses stream live as they are generated.

BY RISHIKESH K G