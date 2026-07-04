from app.services.rag_service import answer_question

print("=" * 70)
print("Testing Complete RAG Pipeline")
print("=" * 70)

session_id = "integration_test"

question = "What is your refund policy?"

result = answer_question(
    session_id=session_id,
    question=question
)

print("\nAnswer:")
print(result["answer"])

print("\nSources:")
print(result.get("sources", []))

assert isinstance(result, dict)
assert "answer" in result
assert "sources" in result

assert isinstance(result["answer"], str)
assert isinstance(result["sources"], list)

assert len(result["answer"].strip()) > 0

print("\n✅ RAG Pipeline Test Passed")