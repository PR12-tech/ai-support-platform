from fastapi import APIRouter

from app.schemas.rag import QuestionRequest
from app.services.rag_service import answer_question

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