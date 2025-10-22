from advanced_rag.evaluation.metrics.metric_upload import upload_metric


def calculate_wordiness_score(llm_reply: str) -> float:
    """
    Calculate wordiness score based on word count.
    Returns 0 if answer has fewer than 30 words, 1 otherwise.

    Args:
        llm_reply: The LLM's response text

    Returns:
        float: 0.0 if word count < 30, 1.0 otherwise
    """
    #TODO: implementiere Wordiness metrik
    return 0.0


def upload_wordiness_metric(
        root_span,
        wordiness_score: float,
        metrics_config,
):
    """
    Upload wordiness metric to Langfuse if enabled in config.

    Args:
        root_span: The Langfuse trace span to attach the metric to
        wordiness_score: The calculated wordiness score
        metrics_config: Configuration object with metric flags
    """
    if metrics_config.use_wordiness:
        upload_metric(root_span, "wordiness", wordiness_score)
