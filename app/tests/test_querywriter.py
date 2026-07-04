from app.services.query_rewriter import rewrite_query

history = [
    {
        "role": "user",
        "content": "Where is my order?"
    },
    {
        "role": "assistant",
        "content": "Can you provide your order ID?"
    }
]

result = rewrite_query(
    "What about the delivery date?",
    history
)

print(result)