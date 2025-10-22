import os

from langchain.retrievers import EnsembleRetriever
from langchain_chroma import Chroma
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import Neo4jVector
from langchain_core.documents import Document

from advanced_rag.backend.environment import Environment
from advanced_rag.backend.nodes.state import State
from .base_node import BaseNode

RETRIEVED_NUMBER_OF_DOCUMENTS = int(int(os.getenv(Environment.RETRIEVED_NUMBER_OF_DOCUMENTS)) / 2)


class HybridRetriever(BaseNode):

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
        ids: list[str] = self.vector_store.get()["ids"]
        documents: list[Document] = self.vector_store.get_by_ids(ids)

        bm25_retriever = BM25Retriever.from_documents(documents)
        bm25_retriever.k = RETRIEVED_NUMBER_OF_DOCUMENTS

        vector_store_retriever = self.vector_store.as_retriever(
            search_kwargs={
                "k": RETRIEVED_NUMBER_OF_DOCUMENTS
            },
        )

        ensemble_retriever = EnsembleRetriever(
            retrievers=[
                bm25_retriever,
                vector_store_retriever

            ],
            weights=[
                0.5,
                0.5
            ],
        )

        retrieved_docs = ensemble_retriever.invoke(state.get_current_question())
        state.context = retrieved_docs
        return state
