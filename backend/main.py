import os
import shutil
import time
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from ingest import ingest_documents
from rag import load_db, get_context, llm

app = FastAPI(title="DocuMind Backend")

# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Models
# -----------------------------
class ChatRequest(BaseModel):
    question: str

# -----------------------------
# Health
# -----------------------------
@app.get("/")
def health():
    return {"status": "running"}

# -----------------------------
# STREAMING CHAT (ChatGPT-style)
# -----------------------------
@app.post("/chat-stream")
def chat_stream(req: ChatRequest):
    context = get_context(req.question)

    prompt = f"""
You are a document-based assistant.
Answer ONLY using the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{req.question}
"""

    def token_generator():
        for token in llm.stream(prompt):
            yield token
            time.sleep(0.02)

    return StreamingResponse(token_generator(), media_type="text/plain")

# -----------------------------
# UPLOAD PDF (single-doc mode)
# -----------------------------
@app.post("/upload")
def upload_document(file: UploadFile = File(...)):
    os.makedirs("docs", exist_ok=True)

    # Remove old PDFs
    for f in os.listdir("docs"):
        if f.endswith(".pdf"):
            os.remove(os.path.join("docs", f))

    path = f"docs/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Remove old vectorstore
    if os.path.exists("vectorstore"):
        for f in os.listdir("vectorstore"):
            os.remove(os.path.join("vectorstore", f))

    ingest_documents()
    load_db()

    return {"status": "uploaded", "file": file.filename}