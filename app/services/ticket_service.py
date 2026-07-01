from sqlalchemy import select

from app.database.db import SessionLocal
from app.models.support_ticket import SupportTicket


def lookup_ticket(
        ticket_id: str
):

    db = SessionLocal()

    try:

        ticket = db.execute(

            select(SupportTicket).where(
                SupportTicket.ticket_id == ticket_id
            )

        ).scalar_one_or_none()

        if ticket:

            return {

                "success": True,

                "ticket": {

                    "ticket_id": ticket.ticket_id,

                    "customer": ticket.customer,

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