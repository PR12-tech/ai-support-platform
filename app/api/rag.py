from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.agent.orchestrator import run_agent
from app.auth.dependencies import get_current_user
from app.models.conversations import Conversation
from app.models.user import User
from app.models.ticket import Ticket
from app.models.messages import Message
from app.schemas.rag import (
    QuestionRequest,
    AskResponse,
    SuggestReplyResponse,
    ConversationResponse,
    ConversationHistoryResponse,
    ClearHistoryResponse,
    ConversationListResponse,
)

from app.services.rag_service import (
    suggest_reply,
    get_knowledge
)

from app.services.memory_service import (
    get_history,
    clear_history,
    get_conversations,
    create_conversation,
)

router = APIRouter()

@router.post(
    "/ask",
    response_model=AskResponse
)

def ask_question(
        request: QuestionRequest,
        current_user: User = Depends(get_current_user)
):

    agent_response = run_agent(
        session_id=request.session_id,
        question=request.question,
        user_id=current_user.id
    )

    return {
        "session_id": request.session_id,
        "question": request.question,
        "tools_used": agent_response.tools_used,
        "answer": agent_response.answer
    }

@router.post(
    "/tickets/{ticket_id}/suggest-reply",
    response_model=SuggestReplyResponse
)

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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket not found."
        )

    messages = db.query(Message).filter(
        Message.ticket_id == ticket_id
    ).all()

    conversation = (
        f"Title: {ticket.title}\n"
        f"Description: {ticket.description}"
    )

    if messages:
        conversation += "\n\nConversation:\n"
        conversation += "\n".join(
            message.content
            for message in messages
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
        "retrieved_chunk": knowledge["knowledge"],
        "reply": reply
    }

@router.post(
        "/conversations",
        response_model=ConversationResponse
)

def create_new_conversation(
    current_user: User = Depends(get_current_user)
):

    conversation = create_conversation(
        user_id=current_user.id
    )

    return conversation

@router.get(
    "/history/{session_id}",
    response_model=ConversationHistoryResponse
)

def get_conversation_history(
        session_id: str,
        current_user: User = Depends(get_current_user)
):

    history = get_history(
        session_id=session_id,
        user_id=current_user.id
    )

    return{
        "session_id": session_id,
        "history": history
    }

@router.delete(
    "/history/{session_id}",
    response_model=ClearHistoryResponse
)

def delete_conversation_history(
        session_id: str,
        current_user: User = Depends(get_current_user)
):

    result = clear_history(
        session_id=session_id,
        user_id=current_user.id
    )
    
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found.                       "
        )

    return {
        "message": "Conversation history cleared.",
        "session_id": session_id
    }

@router.get(
    "/conversations",
    response_model=ConversationListResponse
)
def list_conversations(
    current_user: User = Depends(get_current_user)
):

    conversations = get_conversations(
        user_id=current_user.id
    )

    return {
        "conversations": conversations
    }