from alembic.command import history
from torch import unique

from app.services.ai_service import model
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path
from app.services.embedding_service import model as embedding_model
from app.services.memory_service import get_history, add_message
from app.services.reranker_service import model as reranker_model
from app.services.vector_store import (
    create_index,
    add_embedding,
    search,
    save_index,
    load_index
)
from app.services.bm25_service import (
    create_bm25_index,
    search_bm25
)

DOCUMENT_CHUNKS = []

SIMILARITY_THRESHOLD = 0.60


def get_knowledge(question: str):

        return find_relevant_document(
            question
        )


def answer_question(
        session_id: str,
        question: str
):
    add_message(
        session_id,
        "user",
        question
    )

    history = get_history(
        session_id
    )

    knowledge = get_knowledge(
        question
    )

    knowledge_text = knowledge["knowledge"]

    sources = knowledge["sources"]

    prompt = f"""
    Answer using ONLY the information below.
    
    Conversation History:
    
    {history}
    
    Knowledge Base:
    
    {knowledge_text}
    
    Question:
    
    {question}
    
"""

    try:

        response = model.generate_content(
            prompt
        )

        add_message(
            session_id,
            "assistant",
            response.text
        )

        return {
            "answer": response.text,
            "sources": sources
        }

    except Exception as e:

        return (
            f"AI service temporarily unavailable: {e}"
        )


def find_relevant_document(question: str):

    chunks = retrieve_chunks(
        question
    )

    chunks = rerank_chunks(
        question,
        chunks
    )

    if not chunks:
        return {
            "knowledge": "No relevant information found in the knowledge base.",
            "chunks": []
        }

    sources = extract_sources(
        chunks
    )

    return {
        "knowledge": "\n\n".join(
            chunk["content"]
            for chunk in chunks
        ),
        "chunks": chunks,
        "sources": sources
    }


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
         "faq.txt",
        "warranty_policy.txt",
        "return_policy.txt",
        "payment_policy.txt",
        "order_tracking.txt",
        "account_management.txt",
        "delivery_delays.txt",
        "cancellations.txt",
        "international_shipping.txt",
        "gift_cards.txt"
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

    embedding_dimension = len(
        DOCUMENT_CHUNKS[0]["embedding"]
    )

    if not load_index():

        create_index(
            embedding_dimension
        )

        embeddings = [
            chunk["embedding"]
            for chunk in DOCUMENT_CHUNKS
        ]

        add_embedding(
            embeddings
        )

        save_index()

    documents = [
        chunk["content"]
        for chunk in DOCUMENT_CHUNKS
    ]

    create_bm25_index(
        documents
    )


def retrieve_chunks(question: str):

    question_embedding = embedding_model.encode(
        question
    )

    scores, indices = search(
        question_embedding,
        k=10
    )

    faiss_chunks = []

    for i, index in enumerate(indices[0]):

        if index == -1:
            continue

        chunk = DOCUMENT_CHUNKS[index]

        faiss_chunks.append(
            {
                "content": chunk["content"],
                "source_document": chunk["document"],
                "score": float(scores[0][i])
            }
        )


    faiss_chunks = [
        chunk
        for chunk in faiss_chunks
        if chunk["score"] >= SIMILARITY_THRESHOLD
    ]

    bm25_results = search_bm25(
        question,
        k=10
    )

    bm25_chunks = []

    for content, score in bm25_results:

        for chunk in DOCUMENT_CHUNKS:

            if chunk["content"] == content:

                bm25_chunks.append(
                    {
                        "content": chunk["content"],
                        "source_document": chunk["document"],
                        "score": float(score)
                    }
                )

                break

    all_chunks = (
        faiss_chunks
        + bm25_chunks
    )

    unique_chunks = {}

    for chunk in all_chunks:

        unique_chunks[
            chunk["content"]
        ] = chunk

    retrieved_chunks = list(
        unique_chunks.values()
    )

    return retrieved_chunks


def rerank_chunks(
        question: str,
        chunks: list
):

    pairs = [
        (
            question,
            chunk["content"]
        )
        for chunk in chunks
    ]

    scores = reranker_model.predict(
        pairs
    )

    for chunk, score in zip(
        chunks,
        scores
    ):
        chunk["rerank_score"] = float(score)

    chunks.sort(
        key=lambda chunk: chunk["rerank_score"],
        reverse=True
    )

    return chunks[:3]

def extract_sources(
        chunks: list
):

    sources = []

    for chunk in chunks:

        if chunk["source_document"] not in sources:

            sources.append(
                chunk["source_document"]
            )

    return sources

load_documents()



