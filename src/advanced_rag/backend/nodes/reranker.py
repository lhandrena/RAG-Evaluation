import logging
import os

from langchain_core.documents import Document

from advanced_rag.backend.environment import Environment
from .base_node import BaseNode
from .state import State

CONTEXT_SIZE_AFTER_RERANKING = int(os.getenv(Environment.CONTEXT_SIZE_AFTER_RERANKING))


class Reranker(BaseNode):
    def __init__(
            self,
            node_name: str,
    ):
        super().__init__(node_name)
        self._cross_encoder = None
    
    @property
    def cross_encoder(self):
        if self._cross_encoder is None:
            logging.info("Loading Cross-Encoder model for reranking...")
            from sentence_transformers import CrossEncoder
            self._cross_encoder = CrossEncoder(os.getenv(Environment.CROSS_ENCODER), max_length=512)
            logging.info("Cross-Encoder model loaded successfully")
        return self._cross_encoder

    def traverse(
            self,
            state: State,
    ) -> State:
        if os.getenv(Environment.USE_RERANKING, default="false").lower() == "true":
            documents: list[Document] = state.context
            state.context = self._rerank_documents(documents, state.get_current_question())
            return state
        else:
            return state

    def _rerank_documents(
            self,
            documents: list[Document],
            question: str,
    ) -> list[Document]:
        query_context_pairs: list[tuple[str, str]] = []
        for document in documents:
            query_context_pairs.append(
                (
                    question,
                    document.page_content
                ),
            )
        scores: list[float] = self.cross_encoder.predict(sentences=query_context_pairs).tolist()
        for index, score in enumerate(scores):
            documents[index].metadata['score'] = score
        reranked_documents: list[Document] = sorted(
            documents,
            key=lambda
                document: document.metadata['score'],
            reverse=True,
        )
        reranked_documents = reranked_documents[:min(len(reranked_documents), CONTEXT_SIZE_AFTER_RERANKING)]

        return reranked_documents
