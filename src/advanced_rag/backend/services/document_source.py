from enum import StrEnum


class DocumentSource(StrEnum):
    def __new__(
            cls,
            value: str,
            path: str,
            topic: str,
    ):
        member = str.__new__(cls, value)
        member._value_ = value
        member.path = path
        member.topic = topic
        return member

    TAGESSCHAU = 'TAGESSCHAU', 'src/advanced_rag/scraping/tagesschau_dump', 'german news'
    LLM_GENERAL_SURVEY_PAPER = 'LLM_GENERAL_SURVEY_PAPER', 'src/advanced_rag//scraping/llm_paper', 'general survey papers about large language models'
    SHAKESPEARE = 'SHAKESPEARE', 'src/advanced_rag/scraping/knowledge_graph/shakespeare', 'the book Mac Beth from William Shakespeare'
