import textwrap


class QueryExpansionPrompt:

    @staticmethod
    def get_prompt_template() -> str:
        prompt: str = textwrap.dedent(
            """
            You are an expert at rephrasing user questions.

            If there are multiple common ways of phrasing a user question
            or common synonyms for key words in the question, make sure to return multiple versions
            of the query with the different phrasings.

            If there are acronyms or words you are not familiar with, do not try to rephrase them.
            Only provide queries, no numbering or explanation. Don't make any guesses.
            
            <format_instructions>
                {format_instructions}
            </format_instructions>

            Return up to 5 versions of the following question. Answer in German: 
            <original_question>
                "{original_query}"
            </original_question>    
            """,
        )
        return prompt.strip()

    @staticmethod
    def get_input_variables() -> list[str]:
        return [
            "original_query"
        ]

    @staticmethod
    def get_partial_variables(
            format_instructions: str,
    ) -> dict[str, str]:
        return {
            "format_instructions": format_instructions
        }
