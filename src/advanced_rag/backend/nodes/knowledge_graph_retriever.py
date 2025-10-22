from typing import Any

from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import PromptTemplate
from langchain_neo4j import GraphCypherQAChain, Neo4jGraph

from .base_node import BaseNode
from .prompt_templates.cypher_generation_prompt import CypherGenerationPrompt
from .state import State


class KnowledgeGraphRetriever(BaseNode):
    def __init__(
            self,
            node_name: str,
            llm: BaseChatModel,
            graph: Neo4jGraph,
    ):
        super().__init__(node_name)
        self.graph = graph
        self.llm = llm

    def traverse(
            self,
            state: State,
    ) -> State:
        cypher = self.create_cypher(state)
        print("answer: ", cypher)
        result: list[dict[str, Any]] = self.graph.query(cypher)
        print("result: ", result)

        state.knowledge_graph_context = result
        return state

    def create_cypher(
            self,
            state,
    ):
        cypher_generation_prompt = PromptTemplate(
            input_variables=[
                "schema",
                "question",
                "chat_history"
            ], template=CypherGenerationPrompt.get_prompt(),
        )

        graph_cypher_chain: GraphCypherQAChain = GraphCypherQAChain.from_llm(
            self.llm,
            graph=self.graph,
            cypher_prompt=cypher_generation_prompt,
            allow_dangerous_requests=True,
            verbose=True,
            validate_cypher=True,
        )
        self.graph.refresh_schema()
        cypher = graph_cypher_chain.cypher_generation_chain.invoke(
            {
                "question":     state.get_current_question(),
                "chat_history": state.get_current_chat_history(),
                "schema":       self.graph.get_schema,
            },
        )

        # Lösung ohne extra generator und nur mit GraphCypherQAChain
        # qa_answer = graph_cypher_chain.invoke(
        #     {
        #         "query":        state.get_current_question(),
        #         "schema":       self.graph.get_schema,
        #         "chat_history": state.get_current_chat_history(),
        #     },
        # )
        # print(qa_answer["result"])

        return cypher
