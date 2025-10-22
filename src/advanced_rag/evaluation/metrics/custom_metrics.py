from typing import Tuple

from langchain_core.documents import Document

from advanced_rag.evaluation.metrics.metric_upload import upload_metric


def calculate_context_sources_precision_and_recall(
        documents: list[Document],
        expected_sources,
) -> Tuple[float, float]:
    # Handle both string and dict formats for expected_sources
    if isinstance(expected_sources, dict):
        expected_sources_str = (
            expected_sources.get('expected_sources') or
            expected_sources.get('sources') or
            expected_sources.get('expected_articles', '')
        )
    else:
        expected_sources_str = expected_sources
    
    expected_documents: list[str] = expected_sources_str.split("|") if expected_sources_str else []
    found_sources: list[str] = [document.metadata["source"] for document in documents]
    relevant_documents: set[str] = set(expected_documents).intersection(set(found_sources))

    recall = len(relevant_documents) / len(expected_documents) if expected_documents else 0
    precision = len(relevant_documents) / len(found_sources) if found_sources else 0

    return recall, precision


def calculate_context_sources_f1(
        documents: list[Document],
        expected_sources,
):
    recall, precision = calculate_context_sources_precision_and_recall(documents, expected_sources)

    if precision + recall == 0:
        return 0

    return 2 * (precision * recall) / (precision + recall)


def upload_context_metrics(
        root_span,
        context_recall,
        context_precision,
        context_f1,
        metrics_config,
):
    metrics = {}
    
    if metrics_config.use_context_sources_recall:
        metrics["context_sources_recall"] = context_recall
    if metrics_config.use_context_sources_precision:
        metrics["context_sources_precision"] = context_precision
    if metrics_config.use_context_sources_f1:
        metrics["context_sources_F1"] = context_f1

    for metric_name, score_value in metrics.items():
        upload_metric(root_span, metric_name, score_value)
