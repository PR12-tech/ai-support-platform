import re
from fastapi import APIRouter, Depends
from sqlalchemy.orm  import Session

from app.database.db import get_db
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketCreateResponse, TicketResponse
from app.auth.dependencies import get_current_user
from app.models.user import User

router = APIRouter()


@router.post(
    "/tickets",
    response_model=TicketCreateResponse
)

def create_ticket(
        ticket: TicketCreate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):

    # Generate sequential unique ticket_id (e.g., TKT1001, TKT1002, ...)
    last_ticket = db.query(Ticket).order_by(Ticket.id.desc()).first()
    next_num = 1001
    if last_ticket and last_ticket.ticket_id:
        match = re.search(r'\d+', last_ticket.ticket_id)
        if match:
            next_num = int(match.group()) + 1
        else:
            next_num = last_ticket.id + 1001

    while True:
        ticket_id = f"TKT{next_num}"
        exists = db.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()
        if not exists:
            break
        next_num += 1

    new_ticket = Ticket(
        ticket_id = ticket_id,
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

@router.get(
    "/tickets",
    response_model=list[TicketResponse]
)

def get_tickets(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):

    tickets = db.query(Ticket).filter(
        Ticket.owner_id == current_user.id
    ).all()

    return tickets