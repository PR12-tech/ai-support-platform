from app.services.sql_query_builder import build_query


def main():

    questions = [

        "How many shipped orders are there?",

        "Show shipped orders",

        "Show cancelled orders",

        "Show high priority tickets",

        "Show open tickets"

    ]

    for question in questions:

        print()

        print(question)

        print(build_query(question))


if __name__ == "__main__":

    main()