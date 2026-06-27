from app.services.ai_service import model


def generate_response(
        question: str,
        tool_name: str,
        tool_result: dict
):

    prompt = f"""
    You are a helpful AI customer support assistant.

    The user's question:

    {question}

    The selected tool:

    {tool_name}

    Tool result:

    {tool_result}

    Using ONLY the tool result, answer the user's question naturally.

    If the tool returned an error, explain it politely.
    """

    response = model.generate_content(
        prompt
    )

    return response.text