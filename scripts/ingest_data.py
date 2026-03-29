from langchain_core.documents import Document
import json
import os

from app.rag.embeddings import get_embeddings
from app.rag.vector_store import create_vector_store


# ------------------- BASE PATH FIX -------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
BUG_FILE = os.path.join(DATA_DIR, "bugs.json")
LOG_FILE = os.path.join(DATA_DIR, "logs.txt")
CODE_DIR = os.path.join(DATA_DIR, "code_samples")


# ------------------- LOAD BUG DATA -------------------
def load_bug_data():
    docs = []

    if not os.path.exists(BUG_FILE):
        print("⚠️ bugs.json not found")
        return docs

    with open(BUG_FILE, "r") as f:
        bugs = json.load(f)

    for bug in bugs:
        content = f"""
        Bug ID: {bug.get('bug_id', '')}
        Description: {bug.get('description', '')}
        Severity: {bug.get('severity', '')}
        Module: {bug.get('module', '')}
        Resolution: {bug.get('resolution', '')}
        """
        docs.append(Document(page_content=content))

    return docs


# ------------------- LOAD LOGS -------------------
def load_logs():
    docs = []

    if not os.path.exists(LOG_FILE):
        print("⚠️ logs.txt not found")
        return docs

    with open(LOG_FILE, "r") as f:
        logs = f.readlines()

    return [Document(page_content=log) for log in logs]


# ------------------- LOAD CODE -------------------
def load_code():
    docs = []

    if not os.path.exists(CODE_DIR):
        print("⚠️ code_samples folder not found")
        return docs

    for file in os.listdir(CODE_DIR):
        file_path = os.path.join(CODE_DIR, file)

        try:
            with open(file_path, "r") as f:
                code = f.read()

            docs.append(Document(page_content=code))

        except Exception as e:
            print(f"Error reading file {file}: {e}")

    return docs


# ------------------- LOAD ALL DATA -------------------
def load_all_data():
    docs = []
    docs.extend(load_bug_data())
    docs.extend(load_logs())
    docs.extend(load_code())

    print(f"📊 Total documents loaded: {len(docs)}")
    return docs


# ------------------- CREATE VECTOR DB (IMPORTANT) -------------------
def create_vector_db():
    docs = load_all_data()

    if len(docs) == 0:
        print("❌ No data found. Skipping vector DB creation.")
        return

    embeddings = get_embeddings()
    create_vector_store(docs, embeddings)

    print("✅ Vector DB created successfully!")


# ------------------- MAIN -------------------
if __name__ == "__main__":
    create_vector_db()