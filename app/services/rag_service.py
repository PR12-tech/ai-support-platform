from app.services.ai_service import generate_content
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
from app.services.query_rewriter import rewrite_query
from app.services.multi_query import generate_queries
from app.logger import logger

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

    rewritten_query = rewrite_query(
        question,
        history
    )

    knowledge = get_knowledge(
        rewritten_query
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

    response = generate_content(prompt)

    if response is None:
        return {
            "answer": "AI service temporarily unavailable.",
            "sources": sources
        }

    add_message(
        session_id,
        "assistant",
        response
    )

    return {
        "answer": response,
        "sources": sources
    }


def find_relevant_document(question: str):

    queries = generate_queries(
        question
    )

    chunks = retrieve_multi_query_chunks(
        queries
    )

    logger.debug(
        f"Retrieved {len(chunks)} chunks before reranking."
    )

    chunks = rerank_chunks(
        question,
        chunks
    )

    logger.debug(
        f"Top retrieved sources: {extract_sources(chunks)}"
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

    response = generate_content(prompt)

    if response is None:
        return "AI service temporarily unavailable."

    return response


def create_chunks(text: str):

    words = text.split()

    chunk_size = 350
    overlap = 50

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(
            words[start:end]
        )

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def load_documents():

    DOCUMENT_CHUNKS.clear()

    index_exists = load_index()

    knowledge_base_path = Path("knowledge_base")

    documents = list(knowledge_base_path.rglob("*.md"))
    documents.extend(
        knowledge_base_path.rglob("*.txt")
    )

    for file_path in documents:

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

                chunk_data = {
                    "document": str(
                        file_path.relative_to(
                            knowledge_base_path
                        )
                    ),
                    "content": chunk
                }

                if not index_exists:

                    chunk_data["embedding"] = (
                        embedding_model.encode(chunk)
                    )

                DOCUMENT_CHUNKS.append(
                    chunk_data
                )

    if not index_exists:

        embedding_dimension = len(
            DOCUMENT_CHUNKS[0]["embedding"]
        )

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

    bm25_documents = [
        chunk["content"]
        for chunk in DOCUMENT_CHUNKS
    ]

    create_bm25_index(
        bm25_documents
    )


def retrieve_chunks(question):

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


def retrieve_multi_query_chunks(
        queries: list[str]
):

    all_chunks = []

    for query in queries:

        chunks = retrieve_chunks(
            query
        )

        all_chunks.extend(
            chunks
        )

    seen = set()

    unique_chunks = []

    for chunk in all_chunks:

        if chunk["content"] not in seen:

            seen.add(
                chunk["content"]
            )

            unique_chunks.append(
                chunk
            )

    return unique_chunks


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





