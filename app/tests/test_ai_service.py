from unittest.mock import patch

from app.services.ai_service import (
    classify_ticket,
    analyze_ticket,
)


print("=" * 60)
print("Testing classify_ticket() - Success")
print("=" * 60)

with patch(
    "app.services.ai_service.generate_content",
    return_value="Payment Issue"
) as mock_generate:

    result = classify_ticket("I was charged twice.")

    print("Result:", result)

    assert result == "Payment Issue"
    mock_generate.assert_called_once()

print("✅ Passed")


print("\n" + "=" * 60)
print("Testing classify_ticket() - AI Failure")
print("=" * 60)

with patch(
    "app.services.ai_service.generate_content",
    return_value=None
) as mock_generate:

    result = classify_ticket("I was charged twice.")

    print("Result:", result)

    assert result == "Other"
    mock_generate.assert_called_once()

print("✅ Passed")


print("\n" + "=" * 60)
print("Testing analyze_ticket() - Success")
print("=" * 60)

fake_json = """
{
    "summary": "Customer was charged twice.",
    "category": "Payment Issue",
    "sentiment": "Negative",
    "priority": "High"
}
"""

with patch(
    "app.services.ai_service.generate_content",
    return_value=fake_json
) as mock_generate:

    result = analyze_ticket("I was charged twice.")

    print(result)

    assert result["summary"] == "Customer was charged twice."
    assert result["category"] == "Payment Issue"
    assert result["sentiment"] == "Negative"
    assert result["priority"] == "High"

    mock_generate.assert_called_once()

print("✅ Passed")


print("\n" + "=" * 60)
print("Testing analyze_ticket() - AI Failure")
print("=" * 60)

with patch(
    "app.services.ai_service.generate_content",
    return_value=None
) as mock_generate:

    result = analyze_ticket("I was charged twice.")

    print(result)

    assert result["summary"] == "AI service temporarily unavailable."
    assert result["category"] == "Other"
    assert result["sentiment"] == "Neutral"
    assert result["priority"] == "Low"

    mock_generate.assert_called_once()

print("✅ Passed")


print("\n" + "=" * 60)
print("🎉 ALL TESTS PASSED")
print("=" * 60)