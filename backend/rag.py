from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama

VECTORSTORE_PATH = "vectorstore"

embeddings = OllamaEmbeddings(model="mistral")
llm = Ollama(model="mistral")

db = None

def load_db():
    global db
    db = FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

load_db()

def get_context(question: str):
    docs = db.similarity_search(question, k=3)
    return "\n\n".join(d.page_content for d in docs)