import asyncio
import os

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from ragas import RunConfig, SingleTurnSample
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import (
    Faithfulness,
    ContextPrecision,
    ContextRecall,
    FactualCorrectness,
    SemanticSimilarity,
    MetricWithLLM,
    MetricWithEmbeddings,
)

from advanced_rag.backend.environment import Environment
from advanced_rag.evaluation.metrics.metric_upload import upload_metric

all_metrics = []


def init_ragas_metrics(
        num_ragas_workers,
        metrics_config,
):
    global all_metrics
    all_metrics = []
    
    if metrics_config.use_faithfulness:
        all_metrics.append(Faithfulness())
    if metrics_config.use_context_precision:
        all_metrics.append(ContextPrecision())
    if metrics_config.use_context_recall:
        all_metrics.append(ContextRecall())
    if metrics_config.use_factual_correctness:
        all_metrics.append(FactualCorrectness(mode="recall"))
    if metrics_config.use_semantic_similarity:
        all_metrics.append(SemanticSimilarity())
    
    if not all_metrics:
        return
    
    llm = LangchainLLMWrapper(ChatOpenAI(model=os.getenv(Environment.RAGAS_MODEL)))
    emb = LangchainEmbeddingsWrapper(
        OpenAIEmbeddings(model=os.getenv(Environment.EMBEDDING_MODEL), show_progress_bar=False),
    )

    for metric in all_metrics:
        if isinstance(metric, MetricWithLLM):
            metric.llm = llm
        if isinstance(metric, MetricWithEmbeddings):
            metric.embeddings = emb
        run_config = RunConfig(max_workers=num_ragas_workers)
        metric.init(run_config)


async def score_with_ragas(
        user_input: str,
        retrieved_context: list[str],
        answer_reference: str,
        llm_reply: str,
) -> dict[str, float]:
    sample = SingleTurnSample(
        user_input=user_input,
        response=llm_reply,
        retrieved_contexts=retrieved_context,
        reference=answer_reference,
    )

    async def score_metric(
            metric,
    ):
        score = await metric.single_turn_ascore(sample)
        return metric.name, score

    scores_list = await asyncio.gather(*[score_metric(metric) for metric in all_metrics])
    return dict(scores_list)


def upload_ragas_metrics(
        ragas_scores,
        root_span,
):
    for metric_name, score_value in ragas_scores.items():
        upload_metric(root_span, metric_name, score_value)
