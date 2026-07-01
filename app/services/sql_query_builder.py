def build_query(
        question: str
):

    question = question.lower()

    # Orders

    QUERY_PATTERNS = [

        (
            ["how many", "shipped"],
            """
            SELECT COUNT(*) AS total
            FROM orders
            WHERE status='Shipped';
            """
        ),

        (
            ["show", "shipped"],
            """
            SELECT *
            FROM orders
            WHERE status='Shipped';
            """
        ),

        (
            ["cancelled"],
            """
            SELECT *
            FROM orders
            WHERE status='Cancelled';
            """
        ),

        (
            ["high priority"],
            """
            SELECT *
            FROM support_tickets
            WHERE priority='High';
            """
        ),

        (
            ["open tickets"],
            """
            SELECT *
            FROM support_tickets
            WHERE status='Open';
            """
        )

    ]

    for keywords, query in QUERY_PATTERNS:

        if all(

            keyword in question

            for keyword in keywords

        ):

            return query

    return None
