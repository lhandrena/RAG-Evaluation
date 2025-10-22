def upload_metric(
        root_span,
        metric_name: str,
        score_value: float,
):
    root_span.score_trace(
        name=metric_name,
        value=score_value,
    )
