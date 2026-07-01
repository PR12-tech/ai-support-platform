from app.services.sql_service import execute_sql


def main():

    questions = [

        "How many shipped orders are there?",

        "Show shipped orders",

        "Show cancelled orders",

        "Show high priority tickets",

        "Show open tickets"

    ]

    for question in questions:

        print("\nQuestion:")

        print(question)

        print("\nResult:")

        print(
            execute_sql(question)
        )

        print(
            "\n============================="
        )


if __name__ == "__main__":

    main()