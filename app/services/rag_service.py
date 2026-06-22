from app.services.ai_service import model

from pathlib import Path

def get_knowledge(question: str):

    document = find_relevant_document(
        question
    )

    file_path = (
        Path("knowledge_base")
        / document
    )

    with open(
        file_path,
        "r",
        encoding = "utf-8"
    ) as file:

        return file.read()


def answer_question(question: str):

    knowledge = get_knowledge(question)

    prompt = f"""
    Answer using ONLY the information below.
    
    Knowledge Base:
    
    {knowledge}
    
    Question:
    
    {question}
"""

    response = model.generate_content(
        prompt
    )

    return response.text

def find_relevant_document(question: str):

    question = question.lower()

    if ("refund" in question
        or "money back" in question
        or "return" in question
    ):
        return "refund_policy.txt"

    if ("shipping" in question
        or "delivery" in question
        or "express" in question
    ):
        return "shipping_policy.txt"

    return "faq.txt"