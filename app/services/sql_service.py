from sqlalchemy import text

from app.database.db import SessionLocal

from app.logger import logger

from app.services.sql_query_builder import (
    build_query
)


def execute_sql(
        question: str
):

    """
        Executes a predefined SQL query built from a
        supported natural language question.

        Returns:
            A standardized SQL tool response.
    """

    query = build_query(
        question
    )

    if query is None:

        return {

            "success": False,

            "type": "sql",

            "data": None,

            "message": (
                "Unsupported SQL query. "
                "This question is not supported by the SQL tool."
            )

        }

    db = SessionLocal()

    try:

        logger.info(
            f"Executing SQL query:\n{query}"
        )

        result = db.execute(
            text(query)
        )

        rows = result.mappings().all()

        logger.info(
            f"SQL query returned {len(rows)} rows."
        )

        return {

            "success": True,

            "type": "sql",

            "data": [

                dict(row)

                for row in rows
            ]

        }

    finally:

        db.close()