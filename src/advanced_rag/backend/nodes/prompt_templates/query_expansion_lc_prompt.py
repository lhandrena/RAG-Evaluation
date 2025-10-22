import textwrap


class QueryExpansionLcPrompt:
    @staticmethod
    def get_prompt_template() -> str:
        # The prompt template is copied from langchain.retrievers.multiquery.DEFAULT_QUERY_PROMPT.
        # For comparing the own QueryExpansion implementation against the langchain implementation, it is adapted
        # such that rewrites the user question 5, instead of 3, times.
        prompt: str = textwrap.dedent(
            """
            You are an AI language model assistant. Your task is 
            to generate 5 different versions of the given user 
            question to retrieve relevant documents from a vector  database. 
            By generating multiple perspectives on the user question, 
            your goal is to help the user overcome some of the limitations 
            of distance-based similarity search. Provide these alternative 
            questions separated by newlines. Original question: {question}
            """,
        )
        return prompt.strip()

    @staticmethod
    def get_input_variables() -> list[str]:
        return [
            "question"
        ]
