import logging
import os
from typing import Any

from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel
from langchain_core.runnables import RunnableConfig
from langchain_neo4j import Neo4jGraph
from langgraph.constants import START
from langgraph.graph import StateGraph

from advanced_rag.backend.data_models.message import Message
from advanced_rag.backend.data_models.response_dto import ResponseDTO
from advanced_rag.backend.environment import Environment
from advanced_rag.backend.nodes.graph_answer_generator import GraphAnswerGenerator
from advanced_rag.backend.nodes.knowledge_graph_retriever import KnowledgeGraphRetriever
from advanced_rag.backend.nodes.state import State
from advanced_rag.backend.services.graph_document_processor import GraphDocumentProcessor


class GraphApplication:

    def __init__(
            self,
            tracing_callback_handler,
    ):
        model: str = os.getenv(Environment.CHAT_MODEL)
        self.llm: BaseChatModel = init_chat_model(model, model_provider="openai")
        self.knowledge_graph: Neo4jGraph = GraphDocumentProcessor(llm=self.llm).get_or_create()
        self.tracing_callback_handler = tracing_callback_handler
        self._graph = self.build_graph()

    def ask(
            self,
            chat_history: list[Message],
    ) -> ResponseDTO:
        response: dict[str, Any] = self._graph.invoke(
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
        retriever = KnowledgeGraphRetriever("knowledge_graph_retriever", llm=self.llm, graph=self.knowledge_graph)
        generator: GraphAnswerGenerator = GraphAnswerGenerator(node_name="generator", llm=self.llm)
        logging.info("Building processing graph")
        graph_builder = StateGraph(State).add_sequence(
            [
                (
                    retriever.node_name,
                    retriever.traverse
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
