from app.services.bm25_service import (
    create_bm25_index,
    search_bm25
)

documents = [
    "Refund processing takes 5-7 business days.",
    "Customers may request a refund within 30 days.",
    "Orders delayed beyond 7 days may qualify for compensation.",
    "Customers can permanently delete their account.",
    "Gift cards cannot be exchanged for cash."
]

create_bm25_index(
    documents
)

results = search_bm25(
    "refund processing"
)

for document, score in results:
    print(f"{score:.2f} -> {document}")