import os

from langchain.retrievers import MultiQueryRetriever
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import PromptTemplate

from advanced_rag.backend.environment import Environment
from .base_node import BaseNode
from .prompt_templates.query_expansion_lc_prompt import QueryExpansionLcPrompt
from .state import State

RETRIEVED_NUMBER_OF_DOCUMENTS = int(os.getenv(Environment.RETRIEVED_NUMBER_OF_DOCUMENTS))


class QueryExpansionLcRetriever(BaseNode):

    def __init__(
            self,
            node_name: str,
            vector_store: Chroma,
            llm: BaseChatModel,

    ):
        super().__init__(node_name)
        self.vector_store = vector_store
        self.llm = llm

    def traverse(
            self,
            state: State,
    ) -> State:
        """Retrieve relevant documents based on the question"""
        retriever_from_llm = MultiQueryRetriever.from_llm(
            retriever=self.vector_store.as_retriever(),
            llm=self.llm,
            prompt=PromptTemplate(
                input_variables=QueryExpansionLcPrompt.get_input_variables(),
                template=QueryExpansionLcPrompt.get_prompt_template(),
            ),
        )
        retrieved_docs: list[Document] = retriever_from_llm.invoke(state.get_current_question())

        state.context = retrieved_docs
        return state
