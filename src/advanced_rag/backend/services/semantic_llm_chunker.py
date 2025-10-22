import logging
import os
from concurrent.futures import ThreadPoolExecutor
from itertools import chain

from langchain_core.documents import Document
from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSerializable
from langchain_text_splitters import MarkdownTextSplitter
from pydantic import BaseModel, Field

from advanced_rag.backend.environment import Environment
from advanced_rag.backend.nodes.prompt_templates.semantic_llm_chunking_prompt import SemanticLlmChunkingPrompt


class ChunkSplitIndices(BaseModel):
    split_after_segment: list[int] = Field(
        description="A sorted (ascending) list of chunk numbers (positive integers) after which to split.",
    )


class SemanticLLMChunker:

    def __init__(
            self,
            llm: BaseChatModel,
            chunk_size: int = 100,
    ):
        self.llm = llm
        self.chunk_size = chunk_size
        self.max_chunk_token = int(os.getenv(Environment.MAX_CHUNK_TOKEN, default=800))

        self.text_splitter = MarkdownTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=0,
        )

    def split_documents(
            self,
            documents: list[Document],
    ) -> list[Document]:
        logging.info("Splitting documents into semantic chunks")

        with ThreadPoolExecutor(max_workers=10) as executor:
            chunked_documents = list(
                chain.from_iterable(
                    executor.map(self._chunk_single_document, documents),
                ),
            )

        logging.info(f"number of documents: {len(chunked_documents)}")
        return chunked_documents

    def _chunk_single_document(
            self,
            document: Document,
    ) -> list[Document]:
        chunks_overall: list[Document] = []
        remaining_chunks: list[str] = self.text_splitter.split_text(document.page_content)

        logging.info(f"number of chunks: {len(remaining_chunks)}")
        current_chunks: list[str] = []
        current_tokens: int = 0

        while len(remaining_chunks) > 0:
            current_chunks.append(remaining_chunks.pop(0))
            current_tokens += self.llm.get_num_tokens(current_chunks[-1])

            if current_tokens >= self.max_chunk_token:
                merged_chunks = self.merge_chunks(chunks=current_chunks, metadata=document.metadata)

                if len(merged_chunks) > 1:
                    # keep the last chunk to be able to merge it with chunks after the max chunk limit
                    current_chunks = [
                        merged_chunks.pop(-1).page_content,
                    ]
                    current_tokens = self.llm.get_num_tokens(current_chunks[-1])
                else:
                    current_chunks = []
                    current_tokens = 0

                chunks_overall.extend(merged_chunks)

        if len(current_chunks) > 0:
            chunks_overall.extend(self.merge_chunks(chunks=current_chunks, metadata=document.metadata))

        return chunks_overall

    def merge_chunks(
            self,
            chunks: list[str],
            metadata: dict = None,
    ) -> list[Document]:
        merged_chunks: list[Document] = []
        last_index: int = 0

        chain = self._create_llm_chain()

        split_indices: BaseModel | ChunkSplitIndices = chain.invoke(
            {
                "chunked_input": chunks
            },
        )

        for split_index in split_indices.split_after_segment:
            document: Document = Document(page_content="".join(chunks[last_index:split_index]), metadata=metadata)
            merged_chunks.append(document)
            last_index = split_index

        document = Document(page_content="".join(chunks[last_index:]), metadata=metadata, )
        merged_chunks.append(document)

        return merged_chunks

    def _create_llm_chain(
            self,
    ) -> RunnableSerializable[dict, BaseModel]:

        output_parser = PydanticOutputParser(pydantic_object=ChunkSplitIndices)
        llm_with_structured_output = self.llm.with_structured_output(ChunkSplitIndices, method="json_mode")

        prompt = PromptTemplate(
            input_variables=SemanticLlmChunkingPrompt.get_input_variables(),
            template=SemanticLlmChunkingPrompt.get_prompt(),
            partial_variables=SemanticLlmChunkingPrompt.get_partial_variables(output_parser.get_format_instructions()),
        )

        return prompt | llm_with_structured_output
