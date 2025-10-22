import textwrap


class GraphContextSummarizationPrompt:

    @staticmethod
    def get_prompt() -> str:
        prompt: str = textwrap.dedent(
            """
                you are an expert in summarizing books. Your task is to summarize the following book, keeping important information like characters,events and places.
            The summary will be used as a knowledge base for a graph database, so it should be concise and relevant.
            The content of the book is the following: 
            
            <context>
                {context}
            </context> 
                     
            Summary:
            """,
        )
        return prompt.strip()
