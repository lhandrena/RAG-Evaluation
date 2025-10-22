from enum import StrEnum


class ChunkingStrategy(StrEnum):
    RECURSIVE = "RECURSIVE"
    SEMANTIC = "SEMANTIC"
    SEMANTIC_LLM = "SEMANTIC_LLM"
