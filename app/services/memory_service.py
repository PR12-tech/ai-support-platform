from sqlalchemy.orm import Session
from uuid import uuid4

from app.database.db import SessionLocal
from app.models.conversations import Conversation
from app.models.messages import Message

def generate_conversation_title(content: str) -> str:

    words = content.strip().split()

    if not words:
        return "New Conversation"

    title = " ".join(words[:7])

    if len(title) > 50:
        title = title[:50].rsplit(" ", 1)[0]

    return title


def add_message(
        session_id: str,
        role: str,
        content: str
):

    db: Session = SessionLocal()

    try:

        conversation = db.query(
            Conversation
        ).filter(
            Conversation.session_id == session_id
        ).first()

        if not conversation:

            conversation = Conversation(
                session_id=session_id,
                title="New Conversation"
            )

            db.add(
                conversation
            )

            db.commit()

            db.refresh(
                conversation
            )


        if (
            role == "user"
            and conversation.title == "New Conversation"
        ):
            conversation.title = generate_conversation_title(
                content
            )


        message = Message(
            sender=role,
            content=content,
            conversation_id=conversation.id
        )

        db.add(
            message
        )

        db.commit()

    finally:

        db.close()


def create_conversation():

    db: Session = SessionLocal()

    try:

        conversation = Conversation(
            session_id=str(uuid4()),
            title="New Conversation"
        )

        db.add(
            conversation
        )

        db.commit()

        db.refresh(
            conversation
        )

        return {
            "session_id": conversation.session_id,
            "title": conversation.title,
            "created_at": conversation.created_at
        }

    finally:

        db.close()


def get_history(
        session_id: str
):

    db: Session = SessionLocal()

    try:

        conversation = db.query(
            Conversation
        ).filter(
            Conversation.session_id == session_id
        ).first()

        if not conversation:

            return []

        messages = db.query(
            Message
        ).filter(
            Message.conversation_id == conversation.id
        ).order_by(
            Message.created_at
        ).all()

        return [
            {
                "role": message.sender,
                "content": message.content,
                "created_at": message.created_at
            }
            for message in messages
        ]

    finally:

        db.close()


def clear_history(
        session_id: str
):

    db: Session = SessionLocal()

    try:

        conversation = db.query(
            Conversation
        ).filter(
            Conversation.session_id == session_id
        ).first()

        if not conversation:

            return None

        db.query(
            Message
        ).filter(
            Message.conversation_id == conversation.id
        ).delete()

        db.query(
            Message
        ).filter(
            Message.conversation_id == conversation.id
        ).delete()

        db.delete(
            conversation
        )

        db.commit()

    finally:

        db.close()


def get_conversations():

    db: Session = SessionLocal()

    try:

        conversations = db.query(
            Conversation
        ) .order_by(
            Conversation.created_at.desc()
        ).all()

        return [
            {
                "session_id": conversation.session_id,
                "title": conversation.title,
                "created_at": conversation.created_at
            }
            for conversation in conversations
        ]

    finally:

        db.close()