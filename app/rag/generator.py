from app.core.llm import get_llm

llm = get_llm()

def generate_answer(query, docs):
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are an expert AI debugging assistant.

    Context:
    {context}

    Question:
    {query}

    Answer with:
    - Root cause
    - Risk level
    - Suggested test cases
    """

    response = llm.invoke(prompt)
    return response.content