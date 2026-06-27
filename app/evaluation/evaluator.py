from app.services.rag_service import get_knowledge

from app.evaluation.metrics import (
    hit_rate,
    precision,
    mrr
)

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


def evaluate():

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

            total_mrr += 1 / rank

        relevant = sum(
            1
            for source in retrieved
            if source in expected
        )

        precision_score = relevant / len(retrieved)

        total_precision += precision_score

        if any(
            source in retrieved
            for source in expected
        ):
            hits += 1

    return {

        "hit_rate": hit_rate(
            hits,
            len(TEST_CASES)
        ),

        "precision": precision(
            total_precision,
            len(TEST_CASES)
        ),

        "mrr": mrr(
            total_mrr,
            len(TEST_CASES)
        )

    }