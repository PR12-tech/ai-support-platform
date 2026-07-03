from app.agent.orchestrator import run_agent


def ask(question: str):

    print("\n================================")
    print(f"Question: {question}")

    response = run_agent(
        question=question,
        session_id="optimization_test"
    )

    print("\nAnswer:")
    print(response.answer)
    print("================================\n")


def main():

    ask("Where is order ORD1001?")

    ask("Show high priority tickets")

    ask("How many shipped orders are there?")


if __name__ == "__main__":
    main()