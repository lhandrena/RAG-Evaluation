from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

from advanced_rag.evaluation.metrics.metric_upload import upload_metric


class LLMJudgeResponse(BaseModel):
    """Response model für LLM Judge Evaluation."""
    score: float = Field(
        description="Score: 1.0 wenn Kriterium erfüllt, 0.0 wenn nicht erfüllt"
    )


# Prompt Template - Du kannst diesen Prompt beliebig anpassen!
# Beispiele:
# - "Ist die Antwort auf Deutsch?"
# - "Ist die Antwort für Jugendliche interessant?"
# - "Ist die Antwort höflich formuliert?"
# - "Ist die Antwort in einfacher Sprache geschrieben?"
JUDGE_PROMPT_TEMPLATE = """Du bist ein Evaluator für LLM-Antworten.

Deine Aufgabe: Gebe der Antwort eine Bewertung zwischen 0.0 und 1.0
{llm_reply}

"""


def evaluate_with_llm_judge(llm_reply: str) -> float:
    llm = ChatOpenAI(model="gpt-5-nano", temperature=0.4)
    
    prompt = JUDGE_PROMPT_TEMPLATE.format(llm_reply=llm_reply)
    response = llm.with_structured_output(LLMJudgeResponse).invoke(prompt)
    return response.score



def upload_llm_judge_metric(
    root_span,
    judge_score: float,
    metrics_config,
):
    """
    Upload LLM judge metric to Langfuse if enabled in config.

    Args:
        root_span: The Langfuse trace span to attach the metric to
        judge_score: The calculated judge score (0.0 or 1.0)
        metrics_config: Configuration object with metric flags
    """
    if metrics_config.use_llm_judge:
        upload_metric(root_span, "llm_judge", judge_score)
