from app.services.rag_service import answer_question

print(
    answer_question(
        "user1",
        "Can I get a refund?"
    )
)

print(
    answer_question(
        "user1",
        "How long will it take?"
    )
)