from app.services.ai_service import model

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


    try:

        response = model.generate_content(
            prompt
        )

        return response.text.strip()

    except Exception:

        return question

