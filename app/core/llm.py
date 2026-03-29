from langchain_openai import ChatOpenAI
from app.core.config import OPENAI_API_KEY

def get_llm():
    return ChatOpenAI(
        temperature=0,
        api_key=OPENAI_API_KEY,
        model="gpt-3.5-turbo",  # 🔥 faster than gpt-4
        max_tokens=300
    )