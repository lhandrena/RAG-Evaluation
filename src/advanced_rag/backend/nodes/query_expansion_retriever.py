import os
from typing import Sequence

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSerializable
from pydantic import BaseModel, Field

from advanced_rag.backend.environment import Environment
from advanced_rag.backend.nodes.prompt_templates.query_expansion_prompt import QueryExpansionPrompt
from advanced_rag.backend.nodes.state import State
from .base_node import BaseNode

RETRIEVED_NUMBER_OF_DOCUMENTS = int(os.getenv(Environment.RETRIEVED_NUMBER_OF_DOCUMENTS))


class RephrasedQueries(BaseModel):
    queries: set[str] = Field(description="The rephrased questions as text")


class QueryExpansionRetriever(BaseNode):
    def __init__(
            self,
            node_name: str,
            llm: BaseChatModel,
            vector_store: Chroma,
    ):
        super().__init__(node_name)
        self.llm = llm
        self.vector_store = vector_store

    def traverse(
            self,
            state: State,
    ) -> State:
        expanded_queries: BaseModel = self._expand_queries(state.get_current_question())
        retrieved_documents = self.retrieve_documents_from(expanded_queries)

        state.context = retrieved_documents
        return state

    def _expand_queries(
            self,
            original_query: str,
    ) -> BaseModel | RephrasedQueries:
        chain = self._create_llm_chain()
        rephrased_queries: BaseModel = chain.invoke(
            {
                "original_query": original_query
            },
        )

        return rephrased_queries

    def _create_llm_chain(
            self,
    ) -> RunnableSerializable[dict, BaseModel]:
        output_parser = PydanticOutputParser(pydantic_object=RephrasedQueries)
        llm_with_structured_output = self.llm.with_structured_output(RephrasedQueries, method="json_mode")
        prompt: PromptTemplate = PromptTemplate(
            template=QueryExpansionPrompt.get_prompt_template(),
            input_variables=QueryExpansionPrompt.get_input_variables(),
            partial_variables=QueryExpansionPrompt.get_partial_variables(output_parser.get_format_instructions()),
        )
        return prompt | llm_with_structured_output

    def retrieve_documents_from(
            self,
            expanded_queries: RephrasedQueries | BaseModel,
    ) -> list[Document]:
        documents: list[Document] = []
        for query in expanded_queries.queries:
            documents.extend(self.vector_store.similarity_search(query, k=RETRIEVED_NUMBER_OF_DOCUMENTS))
        return self._unique_documents(documents)

    def _unique_documents(
            self,
            documents: Sequence[Document],
    ) -> list[Document]:
        return [doc for index, doc in enumerate(documents) if doc not in documents[:index]]
