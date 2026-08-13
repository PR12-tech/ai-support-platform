from pydantic import BaseModel
from datetime import datetime

class QuestionRequest(BaseModel):
    session_id: str
    question: str

class ToolExecution(BaseModel):
    tool: str
    arguments: dict
    result: dict

class AskResponse(BaseModel):
    session_id: str
    question: str
    tools_used: list[ToolExecution]
    answer: str

class SuggestReplyResponse(BaseModel):
    ticket_id: int
    retrieved_chunk: str
    reply: str

class ConversationHistoryResponse(BaseModel):
    session_id: str
    history: list

class ClearHistoryResponse(BaseModel):
    message: str
    session_id: str

class ConversationResponse(BaseModel):
    session_id: str
    title: str
    created_at: datetime

class ConversationListResponse(BaseModel):
    conversations: list[ConversationResponse]