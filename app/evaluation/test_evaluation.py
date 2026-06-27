from app.evaluation.evaluator import evaluate

results = evaluate()

print("\n====================")

print(
    f"Hit Rate: {results['hit_rate']:.2%}"
)

print(
    f"Average Precision@K: {results['precision']:.2%}"
)

print(
    f"MRR: {results['mrr']:.2f}"
)