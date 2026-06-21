from fastapi import APIRouter, Depends
from sqlalchemy.orm  import Session

from app.database.db import get_db
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate
from app.auth.dependencies import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/tickets")
def create_ticket(
        ticket: TicketCreate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):

    new_ticket = Ticket(
        title = ticket.title,
        description = ticket.description,
        owner_id = current_user.id
    )

    db.add(new_ticket)

    db.commit()

    db.refresh(new_ticket)

    return {
        "message": "Ticket Created Successfully"
    }

@router.get("/tickets")
def get_tickets(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):

    tickets = db.query(Ticket).filter(
        Ticket.owner_id == current_user.id
    ).all()

    return tickets