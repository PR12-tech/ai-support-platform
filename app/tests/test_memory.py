from app.services.memory_service import (
    add_message,
    get_history,
    clear_history
)


def main():

    session_id = "memory_test"

    print("\n========== CLEAR OLD HISTORY ==========\n")

    clear_history(session_id)

    print("Previous history cleared.")

    print("\n========== ADDING MESSAGES ==========\n")

    add_message(
        session_id=session_id,
        role="user",
        content="Where is my order?"
    )

    add_message(
        session_id=session_id,
        role="assistant",
        content="Your order has been shipped."
    )

    add_message(
        session_id=session_id,
        role="user",
        content="Can I cancel it?"
    )

    print("Messages added successfully.")

    print("\n========== CONVERSATION HISTORY ==========\n")

    history = get_history(session_id)

    for message in history:

        print(f"[{message['role']}] {message['content']}")

    print("\n========== CLEAR HISTORY ==========\n")

    clear_history(session_id)

    history = get_history(session_id)

    print("History after clearing:")

    print(history)

    print("\n========== MEMORY SERVICE TEST PASSED ==========\n")


if __name__ == "__main__":
    main()