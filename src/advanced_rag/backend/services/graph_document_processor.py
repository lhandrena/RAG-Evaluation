import logging
import os
import time
from typing import List

from langchain_core.documents import Document
from langchain_core.language_models import BaseLanguageModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_neo4j import Neo4jGraph
from langchain_neo4j.graphs.graph_document import GraphDocument
from langchain_text_splitters import RecursiveCharacterTextSplitter

from advanced_rag.backend.environment import Environment
from advanced_rag.backend.nodes.prompt_templates.graph_context_summarization_prompt import GraphContextSummarizationPrompt
from advanced_rag.backend.services.document_source import DocumentSource
from advanced_rag.backend.services.file_processor import FileProcessor


class GraphDocumentProcessor:
    def __init__(
            self,
            llm: BaseLanguageModel,
    ):
        self.llm = llm
        self.neo4j_url = os.getenv(Environment.NEO4J_URL)
        self.neo4j_username = os.getenv(Environment.NEO4J_USERNAME)
        self.neo4j_password = os.getenv(Environment.NEO4J_PASSWORD)
        self.file_service = FileProcessor()

        self.chunk_size: int = int(os.getenv(Environment.CHUNK_SIZE))
        self.chunk_overlap: int = int(os.getenv(Environment.CHUNK_OVERLAP))

    def get_or_create(
            self,
    ) -> Neo4jGraph:
        graph = Neo4jGraph(
            refresh_schema=True,
            username=self.neo4j_username,
            password=self.neo4j_password,
            url=self.neo4j_url,
        )

        if self._database_is_empty(graph):
            return self._create_knowledge_graph(graph)

        return graph

    def _create_knowledge_graph(
            self,
            graph: Neo4jGraph,
    ) -> Neo4jGraph:
        llm_transformer: LLMGraphTransformer = LLMGraphTransformer(
            llm=self.llm,
        )

        documents: list[Document] = self.file_service.load_documents(DocumentSource.SHAKESPEARE)
        documents: list[Document] = self.split_documents(documents, self.chunk_size, self.chunk_overlap)
        documents: list[Document] = [self.summarize_document(document) for document in documents]

        logging.info(f"number of chunks: {len(documents)}")
        start_time = time.time()
        print("Converting to graph documents")
        graph_documents: List[GraphDocument] = llm_transformer.convert_to_graph_documents(documents)
        end_time = time.time()
        print(f"Time taken to convert to graph documents: {end_time - start_time} seconds")

        graph.add_graph_documents(graph_documents, include_source=True)
        return graph

    def _database_is_empty(
            self,
            graph,
    ):
        node_count = graph.query("MATCH (n) RETURN count(n)")
        return node_count[0]["count(n)"] == 0

    def split_documents(
            self,
            docs: List[Document],
            size,
            overlap,
    ) -> List[Document]:
        """Split documents into chunks
        :param docs:
        :param size:
        :param overlap:
        """
        logging.info("Splitting documents into chunks")

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=size,
            chunk_overlap=overlap,
        )

        return text_splitter.split_documents(docs)

    def summarize_document(
            self,
            document: Document,
    ) -> Document:
        generation_prompt = PromptTemplate(
            input_variables=[
                "context",
            ],
            template=GraphContextSummarizationPrompt.get_prompt(),
        )
        chain = self._create_llm_chain(generation_prompt)

        response = chain.invoke(
            {
                "context": document.page_content
            },
        )
        return Document(page_content=response)

    def _create_llm_chain(
            self,
            prompt: PromptTemplate,
    ):
        chain = prompt | self.llm | StrOutputParser()
        return chain
