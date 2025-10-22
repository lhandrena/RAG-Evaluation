import os

from langchain_chroma import Chroma
from langchain_community.vectorstores import Neo4jVector

from advanced_rag.backend.environment import Environment
from .base_node import BaseNode
from .state import State

RETRIEVED_NUMBER_OF_DOCUMENTS = int(os.getenv(Environment.RETRIEVED_NUMBER_OF_DOCUMENTS))


class SimilarityRetriever(BaseNode):

    def __init__(
            self,
            node_name: str,
            vector_store: Chroma | Neo4jVector,

    ):
        super().__init__(node_name)
        self.vector_store = vector_store

    def traverse(
            self,
            state: State,
    ) -> State:
        """Retrieve relevant documents based on the question"""
        retrieved_docs = self.vector_store.similarity_search(
            state.get_current_question(),
            k=RETRIEVED_NUMBER_OF_DOCUMENTS,
        )
        state.context = retrieved_docs
        return state
