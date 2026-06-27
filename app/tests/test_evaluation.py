from app.services.rag_service import get_knowledge


TEST_CASES = [

    {
        "question": "Can I get a refund?",
        "expected": [
            "refund_policy.txt"
        ]
    },

    {
        "question": "How can I track my order?",
        "expected": [
            "order_tracking.txt"
        ]
    },

    {
        "question": "Can I cancel my order?",
        "expected": [
            "cancellations.txt"
        ]
    },

    {
        "question": "How long does express delivery take?",
        "expected": [
            "shipping_policy.txt"
        ]
    },

    {
        "question": "Can I change my password?",
        "expected": [
            "account_management.txt"
        ]
    }

]

hits = 0

total_precision = 0

total_mrr = 0

for test in TEST_CASES:

    result = get_knowledge(
        test["question"]
    )

    expected = test["expected"]

    retrieved = result["sources"]

    rank = 0

    for index, source in enumerate(retrieved):

        if source in expected:

            rank = index + 1

            break

    if rank:

        total_mrr += 1/rank


    relevant = sum(
        1
        for source in retrieved
        if source in expected
    )

    precision = relevant / len(retrieved)

    total_precision += precision

    print(f"Precision: {precision:.2f}")
    print()

    print(f"Question : {test['question']}")
    print(f"Expected : {expected}")
    print(f"Retrieved: {retrieved}")

    if any(source in retrieved for source in expected):
        hits += 1

hit_rate = hits / len(TEST_CASES)

print("\n====================")
print(f"Hit Rate: {hit_rate:.2%}")

average_precision = total_precision / len(TEST_CASES)

print(f"Average Precision@K: {average_precision:.2%}")

mrr = total_mrr / len(TEST_CASES)

print(f"MRR: {mrr:.2f}")