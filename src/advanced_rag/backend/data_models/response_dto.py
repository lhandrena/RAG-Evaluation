from langchain_core.documents import Document
from pydantic import BaseModel


class ResponseDTO(BaseModel):
    reply: str
    context: list[Document]
