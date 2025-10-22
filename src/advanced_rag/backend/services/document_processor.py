import logging
import os
import time

from langchain_chroma import Chroma
from langchain_community.utilities.pebblo import generate_size_based_batches
from langchain_community.vectorstores.utils import filter_complex_metadata
from langchain_core.documents import Document
from langchain_core.language_models import BaseChatModel
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from advanced_rag.backend.environment import Environment
from advanced_rag.backend.services.chunking_strategy import ChunkingStrategy
from advanced_rag.backend.services.document_source import DocumentSource
from advanced_rag.backend.services.semantic_chunker import SemanticChunker
from advanced_rag.backend.services.semantic_llm_chunker import SemanticLLMChunker
from advanced_rag.backend.services.file_processor import FileProcessor


class DocumentProcessor:

    def create_vector_store(
            self,
            llm: BaseChatModel,
    ) -> Chroma:
        model: str = os.getenv(Environment.EMBEDDING_MODEL)
        chunk_size: int = int(os.getenv(Environment.CHUNK_SIZE))
        chunk_overlap: int = int(os.getenv(Environment.CHUNK_OVERLAP))
        embedding = OpenAIEmbeddings(model=model, show_progress_bar=True)
        document_source: DocumentSource = DocumentSource(os.getenv(Environment.DOCUMENT_SOURCE))
        chunking_strategy = ChunkingStrategy(os.getenv(Environment.CHUNKING_STRATEGY))
        semantic_chunker: SemanticChunker = SemanticChunker()
        semantic_llm_chunker: SemanticLLMChunker = SemanticLLMChunker(
            llm=llm,
            chunk_size=chunk_size,
        )

        vectorstore = Chroma(
            collection_name=f'{document_source}_{chunking_strategy}',
            embedding_function=embedding,
            persist_directory=f"./chroma_langchain_db_{chunk_size}_{chunk_overlap}",
        )

        file_processor: FileProcessor = FileProcessor()
        start_time = time.time()
        documents: list[Document] = file_processor.load_documents(document_source)
        documents: list[Document] = filter_complex_metadata(documents)
        documents: list[Document] = self._filter_existing_documents(documents, vectorstore)

        match chunking_strategy:
            case ChunkingStrategy.RECURSIVE:
                documents = self.split_documents(documents, chunk_size, chunk_overlap)
            case ChunkingStrategy.SEMANTIC:
                documents = semantic_chunker.split_documents(documents, embedding)
            case ChunkingStrategy.SEMANTIC_LLM:
                documents = semantic_llm_chunker.split_documents(documents)
            case _:
                raise ValueError(f"Unknown chunking type: {chunking_strategy}")

        for batch in generate_size_based_batches(documents):

            if batch:
                vectorstore.add_documents(batch)
        end_time = time.time()
        print(f"Time taken to load and index documents: {end_time - start_time} seconds")
        return vectorstore

    def split_documents(
            self,
            docs: list[Document],
            size,
            overlap,
    ) -> list[Document]:
        logging.info("Splitting documents into chunks")

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=size,
            chunk_overlap=overlap,
        )

        return text_splitter.split_documents(docs)

    def _filter_existing_documents(
            self,
            documents: list[Document],
            vectorstore,
    ) -> list[Document]:
        """Filter out documents that already exist in the vectorstore.

        Uses a combination of source file paths and content hashing to detect duplicates.
        This is more robust than simple metadata comparison.
        """
        # Get existing documents data
        existing_data = vectorstore.get()

        # Build a set of existing source files to avoid re-indexing entire files
        existing_sources = {
            metadata.get("source")
            for metadata in existing_data.get("metadatas", [])
            if metadata.get("source")
        }

        # Build a set of existing content hashes to detect duplicate content
        # even if it comes from different sources
        existing_content_hashes = {
            hash(content)
            for content in existing_data.get("documents", [])
            if content
        }

        new_documents = []
        for doc in documents:
            source = doc.metadata.get("source", "unknown")
            content_hash = hash(doc.page_content)

            # Skip if:
            # 1. The source file was already processed, OR
            # 2. This exact content already exists (duplicate content)
            if source not in existing_sources and content_hash not in existing_content_hashes:
                new_documents.append(doc)

        filtered_count = len(documents) - len(new_documents)
        if filtered_count > 0:
            logging.info(f"Filtered {filtered_count} existing documents out of {len(documents)} total")
        else:
            logging.info(f"All {len(documents)} documents are new")

        return new_documents
