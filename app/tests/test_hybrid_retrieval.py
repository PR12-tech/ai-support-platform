from app.services.rag_service import answer_question

print(
    answer_question(
        "user1",
        "How long does refund processing take?"
    )
)