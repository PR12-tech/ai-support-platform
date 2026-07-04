from time import sleep

from app.agent.orchestrator import run_agent


tests = [
    (
        "Order Lookup",
        "Where is order ORD1001?"
    ),
    (
        "Ticket Lookup",
        "Show me ticket TKT1002."
    ),
    (
        "SQL Analytics",
        "How many shipped orders are there?"
    )
]


print("=" * 90)
print("AI CUSTOMER SUPPORT PLATFORM")
print("AGENT INTEGRATION TEST")
print("=" * 90)


for index, (title, question) in enumerate(tests, start=1):

    print(f"\nTEST {index}: {title}")
    print("-" * 90)

    print("\nQuestion:")
    print(question)

    response = run_agent(
        question=question,
        session_id=f"integration_test_{index}"
    )

    print("\nSelected Tool:")
    print(response.tool)

    print("\nTool Result:")
    print(response.result)

    print("\nFinal Answer:")
    print(response.answer)

    print("\n" + "-" * 90)

    if index != len(tests):

        print("\nWaiting 60 seconds to avoid Gemini rate limits...\n")

        sleep(60)


print("\n" + "=" * 90)
print("ALL AGENT TESTS COMPLETED")
print("=" * 90)