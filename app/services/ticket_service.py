from sqlalchemy import select

from app.database.db import SessionLocal
from app.models.ticket import Ticket


def lookup_ticket(
        ticket_id: str
):

    db = SessionLocal()

    try:

        ticket = db.execute(

            select(Ticket).where(
                Ticket.ticket_id == ticket_id
            )

        ).scalar_one_or_none()

        if ticket:

            return {

                "success": True,

                "ticket": {

                    "ticket_id": ticket.ticket_id,

                    "owner_id": ticket.owner_id,

                    "status": ticket.status,

                    "priority": ticket.priority,

                    "assigned_to": ticket.assigned_to

                }

            }

        return {

            "success": False,

            "message": "Ticket Not Found."

        }

    finally:

        db.close()