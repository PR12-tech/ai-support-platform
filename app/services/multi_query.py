from app.services.ai_service import model


def generate_queries(
        query: str
):

    prompt = f"""
    Generate 4 different search queries for the following question.

Return ONLY the queries.

One query per line.

Question:

{query}
"""

    try:

        response = model.generate_content(
            prompt
        )

        queries = response.text.split("\n")

        return [
            query.strip("-•")
            for query in queries
            if query.strip()
        ]

    except Exception:

        return [query]