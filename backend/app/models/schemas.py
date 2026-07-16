from pydantic import BaseModel


class ChatRequest(BaseModel):
    sender: str
    text: str


class ChatResponse(BaseModel):
    reply: str