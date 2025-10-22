import textwrap


class GraphRagPrompt:

    @staticmethod
    def get_prompt() -> str:
        prompt: str = textwrap.dedent(
            """
            You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. 
        If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
        Question:
         
        <question>
            {question}
        </question>
        
        <chat_history>
            {chat_history}
        </chat_history>
         
        The following are structured useful facts:
        facts: 
        
        <facts>
            {context}
        </facts> 

        Answer the question only using these direct facts 
        Answer:
            """,
        )
        return prompt.strip()
