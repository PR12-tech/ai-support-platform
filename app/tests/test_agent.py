from app.agent.orchestrator import run_agent


def main():

    question = "How many shipped orders are there?"

    response = run_agent(question)

    print("\n========== FINAL RESPONSE ==========\n")
    print(response)
    print("\n====================================\n")


if __name__ == "__main__":
    main()