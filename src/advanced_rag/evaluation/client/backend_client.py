from typing import Any

import aiohttp
from langchain_core.documents import Document
from langfuse._client.datasets import DatasetItemClient


class BackendClient:
    def __init__(
            self,
            port: int,
    ):
        self._url: str = f'http://127.0.0.1:{port}/chat-completion'
        self._session: aiohttp.ClientSession | None = None

    async def __aenter__(self):
        connector = aiohttp.TCPConnector(
            limit=10,
            limit_per_host=10,
            force_close=False,
            enable_cleanup_closed=True
        )
        timeout = aiohttp.ClientTimeout(total=300, connect=60, sock_read=60)
        self._session = aiohttp.ClientSession(
            connector=connector,
            timeout=timeout
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._session:
            await self._session.close()

    async def get_chat_completion_with_context(
            self,
            item: DatasetItemClient,
    ) -> tuple[str, list[Document]]:
        payload: dict[str, list[dict[str, str]]] = self._create_payload_from(item)
        
        if not self._session:
            connector = aiohttp.TCPConnector(
                limit=10,
                limit_per_host=10,
                force_close=False,
                enable_cleanup_closed=True
            )
            timeout = aiohttp.ClientTimeout(total=300, connect=60, sock_read=60)
            self._session = aiohttp.ClientSession(
                connector=connector,
                timeout=timeout
            )
        
        async with self._session.post(self._url, json=payload) as response:
            content_type = response.headers.get('Content-Type', '')
            
            if response.status != 200:
                text = await response.text()
                raise Exception(f"Backend returned status {response.status}: {text[:500]}")
            
            if 'application/json' not in content_type:
                text = await response.text()
                raise Exception(
                    f"Backend returned HTML instead of JSON (status {response.status}).\n"
                    f"Content-Type: {content_type}\n"
                    f"Response preview: {text[:1000]}\n"
                    f"This usually means the Flask backend has an error or the endpoint doesn't exist."
                )
            
            json_data = await response.json()
            return self._extract_reply_and_documents_from(json_data)

    @staticmethod
    def _create_payload_from(
            item: DatasetItemClient,
    ) -> dict[str, list[dict[str, str]]]:
        # Extract text from item.input if it's a dict, otherwise use as-is
        content = item.input.get('text') if isinstance(item.input, dict) else item.input
        return {
            "chat_history": [
                {
                    "id":      item.id,
                    "content": content,
                    "sender":  "user"
                }
            ]
        }

    @staticmethod
    def _extract_reply_and_documents_from(
            json_data: dict[str, Any],
    ) -> tuple[str, list[Document]]:
        llm_reply: str = json_data['reply']
        dict_documents: list[dict[str, Any]] = json_data["context"]
        documents: list[Document] = [Document(**dict_document) for dict_document in dict_documents]

        return llm_reply, documents
