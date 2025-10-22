from pydantic import BaseModel

from advanced_rag.backend.data_models.message import Message


class ConversationState(BaseModel):
    chat_history: list[Message]
