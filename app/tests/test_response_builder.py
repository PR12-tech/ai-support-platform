from app.agent.response_generator import generate_response


def main():

    tests = [

        (
            "Where is my order?",
            "order_lookup",
            {
                "success": True,
                "order": {
                    "order_id": "ORD1001",
                    "customer": "Prasad",
                    "status": "Shipped",
                    "tracking_number": "TRK1001",
                    "estimated_delivery": "2026-06-30"
                }
            }
        ),

        (
            "Show my ticket",
            "ticket_lookup",
            {
                "success": True,
                "ticket": {
                    "ticket_id": "TKT1001",
                    "customer": "Prasad",
                    "status": "Open",
                    "priority": "High",
                    "assigned_to": "Support Team"
                }
            }
        ),

        (
            "How many shipped orders are there?",
            "sql_search",
            {
                "success": True,
                "rows": [
                    {
                        "total": 1
                    }
                ]
            }
        )

    ]

    for question, tool, result in tests:

        print("\n==============================")
        print(f"Tool: {tool}\n")

        response = generate_response(
            question,
            tool,
            result
        )

        print(response)

        print("==============================\n")


if __name__ == "__main__":
    main()