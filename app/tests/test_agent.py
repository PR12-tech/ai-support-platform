from app.agent.orchestrator import run_agent


def main():

    question = "My order ORD1001 is delayed. Can I get a refund??"

    response = run_agent(question)

    print("\n========== FINAL RESPONSE ==========\n")
    print(response)
    print("\n====================================\n")


if __name__ == "__main__":
    main()