from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable

from .base_node import BaseNode
from .prompt_templates.graph_rag_prompt import GraphRagPrompt
from .state import State


class GraphAnswerGenerator(BaseNode):

    def __init__(
            self,
            node_name: str,
            llm: Runnable,
    ):
        super().__init__(node_name)
        self.llm = llm

    def traverse(
            self,
            state: State,
    ) -> State:
        chain = self.create_llm_chain()

        response = chain.invoke(
            {
                "question":     state.get_current_question(),
                "context":      state.knowledge_graph_context,
                "chat_history": state.get_current_chat_history()
            },
        )

        state.answer = response
        return state

    def create_llm_chain(
            self,
    ):
        generation_prompt = PromptTemplate(
            input_variables=[
                "question"
                "context",
                "chat_history"
            ], template=GraphRagPrompt.get_prompt(),
        )
        chain = generation_prompt | self.llm | StrOutputParser()
        return chain
