import asyncio
import os

from tqdm import tqdm
from langchain_core.documents import Document
from langfuse._client.client import Langfuse

from advanced_rag.evaluation.client.backend_client import BackendClient
from advanced_rag.backend.environment import Environment
from advanced_rag.backend.nodes.prompt_templates.augmented_generation_prompt import AugmentedGenerationPrompt
from advanced_rag.evaluation.metrics.custom_metrics import calculate_context_sources_precision_and_recall, calculate_context_sources_f1, \
    upload_context_metrics
from advanced_rag.evaluation.metrics.llm_judge_metric import evaluate_with_llm_judge, upload_llm_judge_metric
from advanced_rag.evaluation.metrics.ragas_metrics import score_with_ragas, upload_ragas_metrics
from advanced_rag.evaluation.metrics.wordiness_metric import calculate_wordiness_score, upload_wordiness_metric


class LangfuseFacade:
    def __init__(
            self,
            backend_client: BackendClient,
            num_parallel_questions: int,
            metrics_config,
    ):
        self._langfuse = Langfuse(
            public_key=os.getenv(Environment.LANGFUSE_PUBLIC_KEY),
            secret_key=os.getenv(Environment.LANGFUSE_SECRET_KEY),
            host=os.getenv(Environment.LANGFUSE_HOST),
        )
        self.client: BackendClient = backend_client
        self._num_parallel_questions = num_parallel_questions
        self._metrics_config = metrics_config

    async def evaluate_dataset(
            self,
            dataset_name,
            experiment_name,
    ):
        dataset = self._langfuse.get_dataset(dataset_name)
        
        self._run_metadata = {
            "chat_model": os.getenv(Environment.CHAT_MODEL),
            "embedding_model": os.getenv(Environment.EMBEDDING_MODEL),
            "generation_prompt": AugmentedGenerationPrompt.get_prompt(),
            "chunk_size": os.getenv(Environment.CHUNK_SIZE),
            "chunk_overlap": os.getenv(Environment.CHUNK_OVERLAP),
            "retriever_type": os.getenv(Environment.RETRIEVER_TYPE),
            "use_reranking": os.getenv(Environment.USE_RERANKING),
            "retrieved_docs": os.getenv(Environment.RETRIEVED_NUMBER_OF_DOCUMENTS),
            "context_size_after_reranking": os.getenv(Environment.CONTEXT_SIZE_AFTER_RERANKING),
            "chunking_strategy": os.getenv(Environment.CHUNKING_STRATEGY),
        }
        
        async with self.client:
            await self._process_chunks(dataset, experiment_name)

    async def _process_chunks(
            self,
            dataset,
            experiment_name,
    ):
        items = dataset.items
        number_of_items = len(items)

        print(f"\n🚀 Starting evaluation of {number_of_items} items from dataset")
        print(f"📊 Processing up to {self._num_parallel_questions} questions in parallel")
        print(f"🔬 Experiment: {experiment_name}\n")

        semaphore = asyncio.Semaphore(self._num_parallel_questions)
        
        async def process_with_semaphore(item):
            async with semaphore:
                try:
                    return await self._process_item(item, experiment_name)
                except Exception as e:
                    print(f"\n❌ Error processing item {item.id}: {str(e)}")
                    raise
        
        tasks = [process_with_semaphore(item) for item in items]
        
        completed = 0
        failed = 0
        with tqdm(total=number_of_items, desc="Evaluating dataset", unit="item") as pbar:
            for coro in asyncio.as_completed(tasks):
                try:
                    await coro
                    completed += 1
                except Exception:
                    failed += 1
                pbar.update(1)
        
        print(f"\n✅ Evaluation complete! Processed {completed} items successfully, {failed} failed")

    async def _process_item(
            self,
            item,
            experiment_name,
    ):
        user_input_text = self._extract_text(item.input)
        expected_output_text = self._extract_text(item.expected_output)
        
        description = f"Chat: {os.getenv(Environment.CHAT_MODEL)} | Embedding: {os.getenv(Environment.EMBEDDING_MODEL)}"
        
        with item.run(
            run_name=experiment_name,
            run_metadata=self._run_metadata,
            run_description=description
        ) as root_span:
            with self._langfuse.start_as_current_generation(
                    name="llm-call",
                    model=os.getenv(Environment.CHAT_MODEL),
                    input=item.input,
            ) as generation:
                llm_reply, documents = await self.client.get_chat_completion_with_context(item)
                context: list[str] = self._extract_context_from(documents)

                generation.update(output=llm_reply)
                root_span.update_trace(
                    input=item.input,
                    output=llm_reply,
                )

                if any([
                    self._metrics_config.use_context_sources_recall,
                    self._metrics_config.use_context_sources_precision,
                    self._metrics_config.use_context_sources_f1,
                ]):
                    context_recall, context_precision = calculate_context_sources_precision_and_recall(
                        documents,
                        item.metadata,
                    )
                    context_f1 = calculate_context_sources_f1(documents, item.metadata)
                    upload_context_metrics(
                        root_span,
                        context_recall,
                        context_precision,
                        context_f1,
                        self._metrics_config,
                    )

                if any([
                    self._metrics_config.use_faithfulness,
                    self._metrics_config.use_context_precision,
                    self._metrics_config.use_context_recall,
                    self._metrics_config.use_factual_correctness,
                    self._metrics_config.use_semantic_similarity,
                ]):
                    ragas_scores: dict[str, float] = await score_with_ragas(
                        user_input=user_input_text,
                        retrieved_context=context,
                        answer_reference=expected_output_text,
                        llm_reply=llm_reply,
                    )

                    upload_ragas_metrics(ragas_scores, root_span)

                if self._metrics_config.use_wordiness:
                    wordiness_score = calculate_wordiness_score(llm_reply)
                    upload_wordiness_metric(root_span, wordiness_score, self._metrics_config)

                if self._metrics_config.use_llm_judge:
                    llm_score = evaluate_with_llm_judge(llm_reply)
                    upload_llm_judge_metric(root_span,llm_score,self._metrics_config)
            self._langfuse.flush()

    @staticmethod
    def _extract_text(value):
        """Extract text from either a string or a dict with 'text' key."""
        if isinstance(value, dict):
            return value.get('text', str(value))
        return value
    
    @staticmethod
    def _extract_context_from(
            documents: list[Document],
    ) -> list[str]:
        return [document.page_content for document in documents]
