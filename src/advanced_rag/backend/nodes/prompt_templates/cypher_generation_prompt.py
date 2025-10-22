import textwrap


class CypherGenerationPrompt:

    @staticmethod
    def get_prompt() -> str:
        prompt: str = textwrap.dedent(
            """
            Task: Generate a Cypher statement to query a graph database.
            Instructions:
            Use only the provided relationship types and properties in the schema.
            Do not use any other relationship types or properties that are not provided.
            
            <schema>
                {schema}
            </schema>
            
            Note: Do not include any explanations or apologies in your responses.
            Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
            Do not include any text except the generated Cypher statement.
            Use Meaningful and concise names in the cypher statement.
            If you need information from the source material, you can access the documents through the property text on document nodes.
            examples:
                1. MATCH (person:Person)-[:MEMBER_OF]->(organisation:Organization) RETURN organisation.id
                2. MATCH (macbeth:Person {{id: 'Macbeth'}})-[:MARRIED]-(spouse:Person) RETURN spouse.id
                3. MATCH (donalbain:Person {{id: "Donalbain"}})-[:FLEES_TO]->(place:Place) RETURN place.id
                4. MATCH (duncan:Person {{id: "King Duncan"}})-[:PARENT]->(son:Person) RETURN son.id
            
            <chat_history>
                {chat_history}
            </chat_history>
            
            The question is:
            
            <question>
                {question}
            </question>
            """,
        )
        return prompt.strip()
