import json


with open(
        "data/tickets.json",
        "r"
) as file:

    TICKETS = json.load(
        file
    )


def lookup_ticket(
        ticket_id: str
):

    for ticket in TICKETS:

        if ticket["ticket_id"] == ticket_id:

            return {

                "success": True,

                "ticket": ticket
            }

    return {

        "success": False,

        "message": "Ticket Not Found."

    }