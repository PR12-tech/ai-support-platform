def build_query(
        question: str
):

    question = question.lower()

    # Orders

    QUERY_PATTERNS = [

        (
            ["each status"],
            """
            SELECT status, COUNT(*) AS count
            FROM orders
            GROUP BY status;
            """
        ),

        (
            ["by status"],
            """
            SELECT status, COUNT(*) AS count
            FROM orders
            GROUP BY status;
            """
        ),

        (
            ["how many", "shipped"],
            """
            SELECT COUNT(*) AS total
            FROM orders
            WHERE LOWER(status)='shipped';
            """
        ),

        (
            ["show", "shipped"],
            """
            SELECT *
            FROM orders
            WHERE LOWER(status)='shipped';
            """
        ),

        (
            ["cancelled"],
            """
            SELECT *
            FROM orders
            WHERE LOWER(status)='cancelled';
            """
        ),

        (
            ["high priority"],
            """
            SELECT *
            FROM tickets
            WHERE LOWER(priority)='high';
            """
        ),

        (
            ["open tickets"],
            """
            SELECT *
            FROM tickets
            WHERE LOWER(status)='open';
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
