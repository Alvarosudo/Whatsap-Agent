from fastapi import APIRouter

from app.models.schemas import ChatRequest
from app.services.chat import ChatService

router = APIRouter()


@router.get("/")
def root():
    return {"status": "ok"}


@router.post("/chat")
def chat(message: ChatRequest):
    return ChatService.generate_response(message)