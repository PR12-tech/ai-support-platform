from app.services.ai_service import generate_content


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

    response = generate_content(prompt)

    if response is None:
        return [query]

    queries = response.split("\n")

    return [
        query.strip("-• ")
        for query in queries
        if query.strip()
    ]