from app.services.query_rewriter import rewrite_query

history = [
    {
        "role": "user",
        "content": "I want a refund."
    },
    {
        "role": "assistant",
        "content": "You can request a refund within 30 days."
    }
]

question = "How long does it take?"

rewritten_query = rewrite_query(
    question,
    history
)

print(rewritten_query)