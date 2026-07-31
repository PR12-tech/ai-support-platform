from pydantic import BaseModel

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