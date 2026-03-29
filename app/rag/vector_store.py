from langchain_community.vectorstores import FAISS
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DB_PATH = os.path.join(BASE_DIR, "vector_db")

# ------------------- CREATE VECTOR DB -------------------
def create_vector_store(docs, embeddings):
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(DB_PATH)
    return db


# ------------------- LOAD VECTOR DB -------------------
def load_vector_store(embeddings):
    if not os.path.exists(DB_PATH):
        print("⚠️ Vector DB not found. Creating...")

        from scripts.ingest_data import create_vector_db
        create_vector_db()

    return FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )