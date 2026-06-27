from app.services.ai_service import model


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

    try:

        response = model.generate_content(
            prompt
        )

        compressed = response.text

        lines = []

        for line in compressed.split("\n"):

            cleaned = line.strip("*•- ")

            if cleaned:

                lines.append(cleaned)

        return "\n".join(lines)


    except Exception:

        return context