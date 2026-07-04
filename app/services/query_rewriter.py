from app.services.ai_service import generate_content

def rewrite_query(
        question: str,
        history: list
):

    prompt = f"""
    You are an AI assistant.

    Rewrite the user's latest question into a standalone search query.

    Use the conversation history only if needed.

    Do NOT answer the question.

    Conversation:

    {history}

    Latest Question:

    {question}

    Standalone Search Query:
    """

    response = generate_content(prompt)

    if response is None:
        return question

    return response

