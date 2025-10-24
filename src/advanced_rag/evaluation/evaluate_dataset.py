import asyncio
import datetime
import os
import time
import warnings
from dataclasses import dataclass
from typing import Optional

os.environ['RAGAS_DO_NOT_TRACK'] = 'true'
warnings.filterwarnings('ignore')

from advanced_rag.evaluation.client.backend_client import BackendClient
from advanced_rag.evaluation.client.langfuse_facade import LangfuseFacade
from advanced_rag.backend.environment import Environment
from advanced_rag.evaluation.metrics.ragas_metrics import init_ragas_metrics

@dataclass
class MetricsConfig:
    # RAGAS Metrics - LLM involved
    use_faithfulness: bool = True
    use_context_precision: bool = True
    use_context_recall: bool = True
    use_factual_correctness: bool = True
    use_semantic_similarity: bool = True

    # Custom Context Source Metrics - No LLM involved
    use_context_sources_recall: bool = True
    use_context_sources_precision: bool = True
    use_context_sources_f1: bool = True

    # Custom Wordiness Metric - No LLM involved
    use_wordiness: bool = False

    # LLM Judge Metric - LLM involved
    use_llm_judge: bool = False


num_parallel_questions = 5
num_ragas_workers = 16


def assemble_experiment_name_from_env(
):
    chunk_size = os.getenv(Environment.CHUNK_SIZE)
    chunk_overlap = os.getenv(Environment.CHUNK_OVERLAP)
    retriever_type = os.getenv(Environment.RETRIEVER_TYPE)
    retrieved_number_of_documents = int(os.getenv(Environment.RETRIEVED_NUMBER_OF_DOCUMENTS))
    context_size_after_reranking = int(os.getenv(Environment.CONTEXT_SIZE_AFTER_RERANKING))
    use_reranking = eval(os.getenv(Environment.USE_RERANKING))
    chunking_strategy = os.getenv(Environment.CHUNKING_STRATEGY)

    context_size = min(
        context_size_after_reranking,
        retrieved_number_of_documents,
    ) if use_reranking else retrieved_number_of_documents

    return f'{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")}_chunk_{chunk_size}_{chunk_overlap}_retriever_{retriever_type}_no_docs_{context_size}_reranking_{use_reranking}_chunking_{chunking_strategy}'


async def evaluate_dataset(
        dataset_name: str,
        backend_port: int = 5000,
        metrics_config: Optional[MetricsConfig] = None,
):
    if metrics_config is None:
        metrics_config = MetricsConfig()
    
    init_ragas_metrics(num_ragas_workers, metrics_config)
    experiment_name = assemble_experiment_name_from_env()
    backend_client = BackendClient(backend_port)
    langfuse_facade = LangfuseFacade(backend_client, num_parallel_questions, metrics_config)
    
    start_time = time.time()
    await langfuse_facade.evaluate_dataset(dataset_name, experiment_name)
    elapsed_time = time.time() - start_time
    
    print(f"\nEvaluation took: {elapsed_time:.2f} seconds ({elapsed_time/60:.2f} minutes)")


if __name__ == "__main__":
    asyncio.run(evaluate_dataset("rag_source"))
