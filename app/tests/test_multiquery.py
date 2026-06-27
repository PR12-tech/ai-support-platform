from app.services.multi_query import generate_queries

queries = generate_queries(
    "Can I get my money back?"
)

for query in queries:
    print(query)