import logging
import os
from typing import Any

from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel
from langchain_core.runnables import RunnableConfig
from langgraph.constants import START
from langgraph.graph import StateGraph

from advanced_rag.backend.core.retrieval_type import RetrievalType
from advanced_rag.backend.data_models.message import Message
from advanced_rag.backend.data_models.response_dto import ResponseDTO
from advanced_rag.backend.environment import Environment
from advanced_rag.backend.nodes.base_node import BaseNode
from advanced_rag.backend.nodes.generator import Generator
from advanced_rag.backend.nodes.hybrid_retriever import HybridRetriever
from advanced_rag.backend.nodes.query_expansion_lc_retriever import QueryExpansionLcRetriever
from advanced_rag.backend.nodes.query_expansion_retriever import QueryExpansionRetriever
from advanced_rag.backend.nodes.reranker import Reranker
from advanced_rag.backend.nodes.similarity_retriever import SimilarityRetriever
from advanced_rag.backend.nodes.state import State
from advanced_rag.backend.services.document_processor import DocumentProcessor


class Application:

    def __init__(
            self,
            tracing_callback_handler,
    ):
        model: str = os.getenv(Environment.CHAT_MODEL)
        self.llm: BaseChatModel = init_chat_model(model, model_provider="openai")
        self._vector_store = None  # Lazy initialization
        self.tracing_callback_handler = tracing_callback_handler
        self._graph = None  # Lazy initialization

    @property
    def vector_store(self):
        """Lazy load vector store only when first accessed"""
        if self._vector_store is None:
            logging.info("Initializing vector store (first access)...")
            self._vector_store = DocumentProcessor().create_vector_store(llm=self.llm)
        return self._vector_store

    @property
    def graph(self):
        """Lazy load graph only when first accessed"""
        if self._graph is None:
            logging.info("Building processing graph (first access)...")
            self._graph = self.build_graph()
        return self._graph

    def ask(
            self,
            chat_history: list[Message],
    ) -> ResponseDTO:
        response: dict[str, Any] = self.graph.invoke(
            State(chat_history=chat_history),
            config=RunnableConfig(
                callbacks=[
                    self.tracing_callback_handler
                ],
            ),
        )

        return ResponseDTO(reply=response["answer"], context=response["context"])

    def build_graph(
            self,
    ):
        retriever: BaseNode

        retriever = self.create_retriever()

        reranker: Reranker = Reranker(node_name="reranker")
        generator: Generator = Generator(node_name="generator", llm=self.llm)
        logging.info("Building processing graph")
        graph_builder = StateGraph(State).add_sequence(
            [
                (
                    retriever.node_name,
                    retriever.traverse
                ),
                (
                    reranker.node_name,
                    reranker.traverse
                ),
                (
                    generator.node_name,
                    generator.traverse
                )
            ],
        )
        graph_builder.add_edge(START, retriever.node_name)
        graph = graph_builder.compile()
        return graph

    def create_retriever(
            self,
    ) -> BaseNode:
        retrieval_type: RetrievalType = RetrievalType(os.getenv(Environment.RETRIEVER_TYPE))

        match retrieval_type:
            case RetrievalType.SIMILARITY_SEARCH:
                return SimilarityRetriever(
                    node_name="similarity_retriever",
                    vector_store=self.vector_store,
                )
            case RetrievalType.HYBRID_SEARCH:
                return HybridRetriever(
                    node_name="hybrid_retriever",
                    vector_store=self.vector_store,
                )
            case RetrievalType.QUERY_EXPANSION:
                return QueryExpansionRetriever(
                    "query_expansion",
                    self.llm,
                    self.vector_store,
                )
            case RetrievalType.QUERY_EXPANSION_LC:
                return QueryExpansionLcRetriever(
                    "query_expansion_retriever",
                    self.vector_store,
                    self.llm,
                )
            case _:
                raise ValueError(f"Unknown retriever type: {retrieval_type}")
