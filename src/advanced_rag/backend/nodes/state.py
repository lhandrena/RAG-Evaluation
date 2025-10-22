from typing import List, Optional, Any

from langchain_core.documents import Document
from pydantic import BaseModel, Field

from advanced_rag.backend.data_models.message import Message


class State(BaseModel):
    chat_history: list[Message]
    context: List[Document] = Field(default_factory=list)
    knowledge_graph_context: list[dict[str, Any]] = Field(default_factory=list)
    answer: Optional[str] = None

    def get_current_question(
            self,
    ) -> str:
        return self.chat_history[-1].content

    def get_current_chat_history(
            self,
    ) -> str:
        result = []

        for message in self.chat_history:
            entry = f"{message.sender.name}: {message.content}\n"
            result.append(entry)

        return '\n'.join(result).strip()
