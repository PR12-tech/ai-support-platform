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


def is_greeting_only(content: str) -> bool:

    normalized = content.strip().lower()

    for char in [".", ",", "?", "!", ";", ":", "-", "_"]:
        normalized = normalized.replace(char, "")

    normalized = " ".join(normalized.split())

    greetings = {
        "hello", "hi", "hey",
        "good morning", "good afternoon", "good evening",
        "hi there", "hello there", "hey there", "greetings",
        "goodmorning", "goodafternoon", "goodevening",
        "yo", "howdy", "sup"
    }

    return normalized in greetings


def add_message(
        session_id: str,
        role: str,
        content: str,
        user_id: int
):

    db: Session = SessionLocal()

    try:

        conversation = db.query(
            Conversation
        ).filter(
            Conversation.session_id == session_id,
            Conversation.user_id == user_id
        ).first()

        if not conversation:

            return None

        if (
            role == "user"
            and conversation.title == "New Conversation"
            and not is_greeting_only(content)
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
        
        return True

    finally:

        db.close()


def create_conversation(user_id: int):

    db: Session = SessionLocal()

    try:

        conversation = Conversation(
            session_id=str(uuid4()),
            title="New Conversation",
            user_id=user_id
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
        session_id: str,
        user_id: int
):
    import time
    from app.logger import logger

    t_total_start = time.perf_counter()

    t_session_start = time.perf_counter()
    db: Session = SessionLocal()
    t_session_end = time.perf_counter()

    try:
        t_conv_start = time.perf_counter()
        conversation = db.query(
            Conversation
        ).filter(
            Conversation.session_id == session_id,
            Conversation.user_id == user_id
        ).first()
        t_conv_end = time.perf_counter()

        if not conversation:
            t_total_elapsed = (time.perf_counter() - t_total_start) * 1000.0
            logger.info(f"HISTORY_TIMING total={t_total_elapsed:.2f}ms")
            return []

        t_msg_start = time.perf_counter()
        messages = db.query(
            Message
        ).filter(
            Message.conversation_id == conversation.id
        ).order_by(
            Message.created_at
        ).all()
        t_msg_end = time.perf_counter()

        t_build_start = time.perf_counter()
        result = [
            {
                "role": message.sender,
                "content": message.content,
                "created_at": message.created_at
            }
            for message in messages
        ]
        t_build_end = time.perf_counter()

        elapsed_session = (t_session_end - t_session_start) * 1000.0
        elapsed_conv = (t_conv_end - t_conv_start) * 1000.0
        elapsed_msg = (t_msg_end - t_msg_start) * 1000.0
        elapsed_build = (t_build_end - t_build_start) * 1000.0
        elapsed_total = (time.perf_counter() - t_total_start) * 1000.0

        logger.info(
            f"HISTORY_DB session_acquire={elapsed_session:.2f}ms "
            f"conversation_query={elapsed_conv:.2f}ms "
            f"message_query={elapsed_msg:.2f}ms "
            f"response_build={elapsed_build:.2f}ms "
            f"total={elapsed_total:.2f}ms"
        )
        logger.info(f"HISTORY_TIMING total={elapsed_total:.2f}ms")

        return result

    finally:

        db.close()


def clear_history(
        session_id: str,
        user_id: int
):

    db: Session = SessionLocal()

    try:

        conversation = db.query(
            Conversation
        ).filter(
            Conversation.session_id == session_id,
            Conversation.user_id == user_id
        ).first()

        if not conversation:
            return None

        db.query(
            Message
        ).filter(
            Message.conversation_id == conversation.id,
        ).delete()

        db.delete(
            conversation
        )

        db.commit()
        
        return True

    finally:

        db.close()


def get_conversations(user_id: int):

    db: Session = SessionLocal()

    try:

        conversations = db.query(
            Conversation
        ).filter(
            Conversation.user_id == user_id
        ).order_by(
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