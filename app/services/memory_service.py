from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.models.conversations import Conversation
from app.models.messages import Message

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
                session_id=session_id
            )

            db.add(
                conversation
            )

            db.commit()

            db.refresh(
                conversation
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

        db.delete(
            conversation
        )

        db.commit()

    finally:

        db.close()