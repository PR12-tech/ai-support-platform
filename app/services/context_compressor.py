from app.services.ai_service import generate_content


def compress_context(
        question: str,
        context: str
):

    prompt = f"""
Extract all information that may help answer the user's question.

Do not answer the question.

Keep only relevant facts.

Remove unrelated information.

Question:

{question}

Context:

{context}

Relevant Context:
"""

    response = generate_content(prompt)

    if response is None:
        return context

    lines = []

    for line in response.split("\n"):

        cleaned = line.strip("*•- ")

        if cleaned:
            lines.append(cleaned)

    return "\n".join(lines)