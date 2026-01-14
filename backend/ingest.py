import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS

DOCS_PATH = "docs"
VECTORSTORE_PATH = "vectorstore"

def ingest_documents():
    documents = []

    for file in os.listdir(DOCS_PATH):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DOCS_PATH, file))
            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    embeddings = OllamaEmbeddings(model="mistral")
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(VECTORSTORE_PATH)

    print("✅ Documents indexed successfully")

if __name__ == "__main__":
    ingest_documents()
