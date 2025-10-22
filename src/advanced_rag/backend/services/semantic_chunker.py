import logging
import os
import re
from concurrent.futures import ThreadPoolExecutor
from itertools import chain
from typing import Any

import numpy as np
import tiktoken
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from numpy import bool_
from sklearn.metrics.pairwise import cosine_similarity
from tiktoken import Encoding

from advanced_rag.backend.environment import Environment


class SemanticChunker:

    def __init__(
            self,
    ):
        self.avg_chunk_size: int = int(os.getenv(Environment.AVG_CHUNK_SIZE, default=300))
        self.breakpoint_percentile_threshold: int = int(
            os.getenv(Environment.BREAKPOINT_PERCENTILE_THRESHOLD, default=95),
        )
        self.buffer_size: int = int(os.getenv(Environment.BUFFER_SIZE, default=1))
        self.binary_search: bool = eval(os.getenv(Environment.BINARY_SEARCH, default=False))
        self.encoding: Encoding = tiktoken.encoding_for_model("gpt-4")

    def split_documents(
            self,
            documents: list[Document],
            embedding: OpenAIEmbeddings,
    ) -> list[Document]:
        logging.info("Splitting documents into semantic chunks")

        # TODO IMPROVEMENT: Check if embedding is thread-safe, if not, create a new instance for each thread
        with ThreadPoolExecutor(max_workers=20) as executor:
            chunked_documents = list(
                chain.from_iterable(
                    executor.map(
                        lambda
                            doc: self._create_chunks(doc, embedding),
                        documents,
                    ),
                ),
            )
        return chunked_documents

    def _create_chunks(
            self,
            document: Document,
            embedding: OpenAIEmbeddings,
    ) -> list[Document]:
        """Chop document into semantic chunks using embeddings and cosine distance."""
        sentences: list[dict] = self._split_into_sentences(document.page_content)
        self._combine_sentences(sentences)
        self._add_embeddings(sentences, embedding)

        distances, sentences = self._calculate_cosine_distances(sentences)

        threshold: float = self._determine_distance_threshold(distances, sentences)

        indices_above_thresh = [index for index, distance in enumerate(distances) if distance > threshold]

        chunks: list[str] = self.extract_chunks(indices_above_thresh, sentences)

        return [Document(page_content=chunk, metadata=document.metadata) for chunk in chunks]

    def _split_into_sentences(
            self,
            text: str,
    ) -> list[dict]:
        sentences: list[str | Any] = re.split(r'(?<=[.?!])\s+', text)
        logging.info(f"{len(sentences)} sentences were found")
        return [{
            'sentence': s,
            'index':    i
        } for i, s in enumerate(sentences)]

    def _add_embeddings(
            self,
            sentences: list[dict],
            embedding: OpenAIEmbeddings,
    ) -> None:
        combined = [dic['combined_sentence'] for dic in sentences]
        embeddings = embedding.embed_documents(combined)
        for dic, emb in zip(sentences, embeddings):
            dic["combined_sentence_embedding"] = emb

    def _combine_sentences(
            self,
            sentences: list[dict],
    ) -> None:
        for index in range(len(sentences)):
            start = max(0, index - self.buffer_size)
            end = min(len(sentences), index + self.buffer_size + 1)
            combined = ' '.join(sent['sentence'] for sent in sentences[start:end])
            sentences[index]['combined_sentence'] = combined

    def _calculate_cosine_distances(
            self,
            sentences: list[dict],
    ) -> tuple[list[float], list[dict]]:
        """Return list of cosine distances between each pair of consecutive combined_sentence embeddings."""

        distances = []
        for index in range(len(sentences) - 1):
            embedding_current: list[float] = sentences[index]['combined_sentence_embedding']
            embedding_next: list[float] = sentences[index + 1]['combined_sentence_embedding']

            similarity: float = cosine_similarity([embedding_current], [embedding_next])[0][0]

            distance: float = 1 - similarity

            distances.append(distance)

            sentences[index]['distance_to_next'] = distance

        # handle the last sentence
        sentences[-1]['distance_to_next'] = 0

        return distances, sentences

    def extract_chunks(
            self,
            indices_above_thresh: list[int],
            sentences: list[dict],
    ) -> list[str]:
        """Slice sentences into chunks using the break_indices."""

        chunks: list[str] = []
        start_index: int = 0
        for break_idx in indices_above_thresh:
            chunk: str = ' '.join(sent['sentence'] for sent in sentences[start_index:break_idx + 1])
            chunks.append(chunk)

            start_index = break_idx + 1

        # The last group, if any sentences remain
        if start_index < len(sentences):
            combined_text: str = ' '.join([d['sentence'] for d in sentences[start_index:]])
            chunks.append(combined_text)

        return chunks

    def _determine_distance_threshold(
            self,
            distances: list[float],
            sentences: list[dict],
    ) -> float:
        """Determine the distance threshold that separates the sentences into chunks."""

        if self.binary_search:
            total_tokens: float = sum(self._openai_token_count(sentence['sentence']) for sentence in sentences)
            number_of_cuts: float = total_tokens // self.avg_chunk_size

            lower_limit: float = 0.0
            upper_limit: float = 1.0

            distances_np = np.array(distances)

            # TODO IMPROVEMENT: make stopping condition variable?
            while upper_limit - lower_limit > 1e-6:
                threshold: float = (upper_limit + lower_limit) / 2.0
                num_points_above_threshold: bool_ = np.sum(distances_np > threshold)

                if num_points_above_threshold > number_of_cuts:
                    lower_limit = threshold
                else:
                    upper_limit = threshold
            return threshold

        return float(
            np.percentile(
                distances,
                self.breakpoint_percentile_threshold,
            ),
        )

    def _openai_token_count(
            self,
            content: str,
    ) -> int:
        """Returns the number of tokens in a text string."""
        return len(self.encoding.encode(content, disallowed_special=()))
