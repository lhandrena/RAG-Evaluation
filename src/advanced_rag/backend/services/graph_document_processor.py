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
    _SUMMARIZATION_LOG_INTERVAL = 10
    _GRAPH_CONVERSION_BATCH_SIZE_ENV = "GRAPH_CONVERSION_BATCH_SIZE"
    _DEFAULT_GRAPH_CONVERSION_BATCH_SIZE = 10

    def __init__(
            self,
            llm: BaseLanguageModel,
    ):
        self.llm = llm
        # Keep compatibility with older env naming used in the course docs.
        self.neo4j_url = os.getenv(Environment.NEO4J_URL) or os.getenv("NEO4J_URI")
        self.neo4j_username = os.getenv(Environment.NEO4J_USERNAME)
        self.neo4j_password = os.getenv(Environment.NEO4J_PASSWORD)
        self.file_service = FileProcessor()

        self.chunk_size: int = int(3000)
        self.chunk_overlap: int = int(500)

    def get_or_create(
            self,
    ) -> Neo4jGraph:
        logging.info("Connecting to Neo4j (%s)", self.neo4j_url or "default URL")
        graph = Neo4jGraph(
            refresh_schema=True,
            username=self.neo4j_username,
            password=self.neo4j_password,
            url=self.neo4j_url,
        )

        if self._database_is_empty(graph):
            logging.info("Neo4j database is empty. Starting knowledge graph creation.")
            return self._create_knowledge_graph(graph)

        logging.info("Neo4j already contains data. Reusing existing knowledge graph.")
        return graph

    def _create_knowledge_graph(
            self,
            graph: Neo4jGraph,
    ) -> Neo4jGraph:
        total_start_time = time.time()
        llm_transformer: LLMGraphTransformer = LLMGraphTransformer(
            llm=self.llm,
        )

        raw_documents: list[Document] = self.file_service.load_documents(DocumentSource.SHAKESPEARE)
        logging.info("Loaded %s raw documents for graph ingestion", len(raw_documents))

        chunked_documents: list[Document] = self.split_documents(raw_documents, self.chunk_size, self.chunk_overlap)
        summarized_documents: list[Document] = self._summarize_documents_with_progress(chunked_documents)

        graph_documents: List[GraphDocument] = self._convert_documents_to_graph_documents(
            llm_transformer=llm_transformer,
            documents=summarized_documents,
        )

        logging.info("Writing %s graph documents to Neo4j", len(graph_documents))
        graph.add_graph_documents(graph_documents, include_source=True)
        logging.info("Knowledge graph creation finished in %.2f seconds", time.time() - total_start_time)
        return graph

    def _database_is_empty(
            self,
            graph,
    ):
        node_count = graph.query("MATCH (n) RETURN count(n)")
        count = node_count[0]["count(n)"]
        logging.info("Neo4j currently has %s nodes", count)
        return count == 0

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
        logging.info("Splitting %s documents into chunks (size=%s, overlap=%s)", len(docs), size, overlap)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=size,
            chunk_overlap=overlap,
        )

        chunks = text_splitter.split_documents(docs)
        logging.info("number of chunks: %s", len(chunks))
        return chunks

    def _summarize_documents_with_progress(
            self,
            documents: list[Document],
    ) -> list[Document]:
        total_documents = len(documents)
        if total_documents == 0:
            logging.info("No chunks to summarize")
            return []

        logging.info("Starting summarization for %s chunks", total_documents)
        summarized_documents: list[Document] = []
        start_time = time.time()

        for index, document in enumerate(documents, start=1):
            try:
                summarized_documents.append(self.summarize_document(document))
            except Exception:
                logging.exception("Summarization failed at chunk %s/%s", index, total_documents)
                raise

            if index == 1 or index % self._SUMMARIZATION_LOG_INTERVAL == 0 or index == total_documents:
                elapsed = time.time() - start_time
                average_time_per_chunk = elapsed / index
                eta_seconds = average_time_per_chunk * (total_documents - index)
                logging.info(
                    "Summarization progress: %s/%s (%.1f%%, elapsed %.1fs, ETA %.1fs)",
                    index,
                    total_documents,
                    (index / total_documents) * 100,
                    elapsed,
                    eta_seconds,
                )

        return summarized_documents

    def _convert_documents_to_graph_documents(
            self,
            llm_transformer: LLMGraphTransformer,
            documents: list[Document],
    ) -> list[GraphDocument]:
        total_documents = len(documents)
        if total_documents == 0:
            logging.info("No summarized chunks to convert")
            return []

        batch_size = max(
            1,
            int(os.getenv(self._GRAPH_CONVERSION_BATCH_SIZE_ENV, self._DEFAULT_GRAPH_CONVERSION_BATCH_SIZE)),
        )
        total_batches = (total_documents + batch_size - 1) // batch_size
        logging.info(
            "Converting %s summarized chunks to graph documents (batch_size=%s, batches=%s)",
            total_documents,
            batch_size,
            total_batches,
        )

        graph_documents: list[GraphDocument] = []
        start_time = time.time()
        for batch_index, start in enumerate(range(0, total_documents, batch_size), start=1):
            batch = documents[start:start + batch_size]
            chunk_start = start + 1
            chunk_end = start + len(batch)

            try:
                batch_graph_documents = llm_transformer.convert_to_graph_documents(batch)
            except Exception:
                logging.exception(
                    "Graph conversion failed for batch %s/%s (chunks %s-%s)",
                    batch_index,
                    total_batches,
                    chunk_start,
                    chunk_end,
                )
                raise

            graph_documents.extend(batch_graph_documents)
            elapsed = time.time() - start_time
            average_time_per_batch = elapsed / batch_index
            eta_seconds = average_time_per_batch * (total_batches - batch_index)
            logging.info(
                "Graph conversion progress: batch %s/%s (chunks %s-%s), total graph docs=%s (elapsed %.1fs, ETA %.1fs)",
                batch_index,
                total_batches,
                chunk_start,
                chunk_end,
                len(graph_documents),
                elapsed,
                eta_seconds,
            )

        logging.info("Graph conversion completed in %.2f seconds", time.time() - start_time)
        return graph_documents

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
