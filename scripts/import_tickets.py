import json

from app.database.db import SessionLocal
from app.models.support_ticket import SupportTicket


def main():

    db = SessionLocal()

    with open(
        "data/tickets.json",
        "r",
        encoding="utf-8"
    ) as file:

        tickets = json.load(file)

    for ticket in tickets:

        db.add(

            SupportTicket(

                ticket_id=ticket["ticket_id"],

                customer=ticket["customer"],

                status=ticket["status"],

                priority=ticket["priority"],

                assigned_to=ticket["assigned_to"]

            )

        )

    db.commit()

    db.close()

    print("Tickets imported successfully.")


if __name__ == "__main__":

    main()