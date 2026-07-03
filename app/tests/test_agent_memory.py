from app.agent.orchestrator import run_agent


SESSION = "demo_session"


def ask(question):

    response = run_agent(

        question=question,

        session_id=SESSION

    )

    print("\nUSER:")

    print(question)

    print("\nASSISTANT:")

    print(response.answer)

    print("\n----------------------")


def main():

    ask("Where is order ORD1001?")

    ask("Can I cancel it?")


if __name__ == "__main__":

    main()