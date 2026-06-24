from app.services.ai_service import model
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path
from app.services.embedding_service import model as embedding_model

DOCUMENT_CHUNKS = []


def get_knowledge(question: str):

        return find_relevant_document(
            question
        )


def answer_question(question: str):

    knowledge = get_knowledge(question)

    prompt = f"""
    Answer using ONLY the information below.
    
    Knowledge Base:
    
    {knowledge}
    
    Question:
    
    {question}
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return (
            f"AI service temporarily unavailable: {e}"
        )


def find_relevant_document(question: str):

    question_embedding = embedding_model.encode(
        question
    )

    best_chunk = None

    best_score = -1

    for chunk in DOCUMENT_CHUNKS:

        chunk_embedding = chunk["embedding"]

        score = cosine_similarity(
            [question_embedding],
            [chunk_embedding]
        )[0][0]

        if score > best_score:

            best_score = score

            best_chunk = chunk["content"]

    return best_chunk


def suggest_reply(
        conversation: str,
        knowledge: str
):
    prompt = f"""
        You are a professional customer support agent.

        Use the knowledge below to help the customer.

        Knowledge:
        {knowledge}

        Customer Conversation:
        {conversation}

        Write a helpful support response.
        """

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return (
            f"AI service temporarily unavailable: {e}"
        )


def create_chunks(text: str):

    chunks = text.split("\n\n")

    return [
        chunk.strip()
        for chunk in chunks
        if chunk.strip()
    ]


def load_documents():

    DOCUMENT_CHUNKS.clear()

    documents = [
        "refund_policy.txt",
        "shipping_policy.txt",
        "faq.txt"
    ]

    for document in documents:

        file_path = (
            Path("knowledge_base")
            / document
        )

        with open(
            file_path,
            "r",
            encoding= "utf-8"
        ) as file:

            content = file.read()

            chunks = create_chunks(
                content
            )

            for chunk in chunks:

                embedding = embedding_model.encode(
                    chunk
                )

                DOCUMENT_CHUNKS.append(
                    {
                        "document": document,
                        "content": chunk,
                        "embedding": embedding
                    }
                )

load_documents()



