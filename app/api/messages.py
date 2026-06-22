from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.auth.dependencies import get_current_user
from app.models.user import User
from app.models.ticket import Ticket
from app.models.messages import Message
from app.schemas.message import MessageCreate
from app.services.ai_service import summarize_text, classify_ticket, analyze_ticket


router = APIRouter()


@router.post("/tickets/{ticket_id}/messages")
def create_message(
        ticket_id: int,
        message: MessageCreate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):

    ticket = db.query(Ticket).filter(
Ticket.id == ticket_id,
         Ticket.owner_id == current_user.id
    ).first()

    if not ticket:
        return {
            "message": "Ticket not found"
        }

    new_message = Message(
        content = message.content,
        sender = current_user.username,
        ticket_id = ticket_id
    )

    db.add(new_message)

    db.commit()

    db.refresh(new_message)

    return {
        "message": "Message added"
    }


@router.get("/tickets/{ticket_id}/messages")
def get_messages(
        ticket_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):

    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id,
        Ticket.owner_id == current_user.id
    ).first()

    if not ticket:
        return{
            "message": "Ticket not found"
        }

    messages = db.query(Message).filter(
        Message.ticket_id == ticket_id,
    ).all()

    return messages


@router.post("/tickets/{ticket_id}/summarize")
def summarize_ticket(
        ticket_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):

    ticket = db.query(Ticket).filter(
Ticket.id == ticket_id,
         Ticket.owner_id == current_user.id
    ).first()

    if not ticket:
        return {
            "message": "Ticket not found"
        }

    messages = db.query(Message).filter(
        Message.ticket_id == ticket_id
    ).all()

    conversation = "\n".join(
        [message.content for message in messages]
    )

    summary = summarize_text(conversation)

    return {
        "ticket_id": ticket_id,
        "conversation": conversation,
        "summary": summary
    }

@router.post("/tickets/{ticket_id}/classify")
def classify_ticket_endpoint(
        ticket_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id,
        Ticket.owner_id == current_user.id
    ).first()

    if not ticket:
        return {
            "message": "Ticket not found"
        }

    messages = db.query(Message).filter(
        Message.ticket_id == ticket_id
    ).all()

    conversation = "\n".join(
        [message.content for message in messages]
    )

    category = classify_ticket(conversation)

    return {
        "ticket_id": ticket_id,
        "category": category
    }

@router.post("/tickets/{ticket_id}/analyze")
def analyze_ticket_endpoint(
        ticket_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):

    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id,
        Ticket.owner_id == current_user.id
    ).first()

    if not ticket:
        return {
            "message": "Ticket not found"
        }

    messages = db.query(Message).filter(
        Message.ticket_id == ticket_id
    ).all()

    conversation = "\n".join(
        [message.content for message in messages]
    )

    analysis = analyze_ticket(conversation)

    return analysis