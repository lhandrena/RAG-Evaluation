from enum import Enum

from pydantic import BaseModel


class SenderType(str, Enum):  # Inherit from str for JSON compatibility
    user = "user"
    bot = "bot"


class Message(BaseModel):
    id: str
    content: str
    sender: SenderType
