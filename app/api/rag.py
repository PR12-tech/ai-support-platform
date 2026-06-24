from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.auth.dependencies import get_current_user
from app.models.user import User
from app.models.ticket import Ticket
from app.models.messages import Message
from app.schemas.rag import QuestionRequest

from app.services.rag_service import (
    answer_question,
    suggest_reply,
    get_knowledge
)

router = APIRouter()

@router.post("/ask")
def ask_question(
        request: QuestionRequest
):

    answer = answer_question(
        request.question
    )

    return {
        "question": request.question,
        "answer": answer
    }

@router.post("/tickets/{ticket_id}/suggest-reply")
def generate_reply(
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

    knowledge = get_knowledge(
        conversation
    )

    reply = suggest_reply(
        conversation,
        knowledge
    )

    return {
        "ticket_id": ticket_id,
        "retrieved_chunk": document,
        "reply": reply
    }


