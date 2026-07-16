from app.models.schemas import ChatRequest, ChatResponse


class ChatService:

    @staticmethod
    def generate_response(message: ChatRequest) -> ChatResponse:
        return ChatResponse(
            reply=f"Hola {message.sender}, has dicho: {message.text}"
        )