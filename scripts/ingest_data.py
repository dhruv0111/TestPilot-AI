from langchain_core.documents import Document
import json
import os

from app.rag.embeddings import get_embeddings
from app.rag.vector_store import create_vector_store


def load_bug_data():
    with open("data/bugs.json", "r") as f:
        bugs = json.load(f)

    docs = []
    for bug in bugs:
        content = f"""
        Bug ID: {bug['bug_id']}
        Description: {bug['description']}
        Severity: {bug['severity']}
        Module: {bug['module']}
        Resolution: {bug['resolution']}
        """
        docs.append(Document(page_content=content))

    return docs


def load_logs():
    with open("data/logs.txt", "r") as f:
        logs = f.readlines()

    return [Document(page_content=log) for log in logs]


def load_code():
    docs = []
    folder = "data/code_samples"

    for file in os.listdir(folder):
        with open(os.path.join(folder, file), "r") as f:
            code = f.read()

        docs.append(Document(page_content=code))

    return docs


def load_all_data():
    docs = []
    docs.extend(load_bug_data())
    docs.extend(load_logs())
    docs.extend(load_code())
    return docs


if __name__ == "__main__":
    docs = load_all_data()
    embeddings = get_embeddings()

    create_vector_store(docs, embeddings)

    print("✅ Real dataset ingested successfully!")