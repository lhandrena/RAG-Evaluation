from abc import ABC, abstractmethod

from advanced_rag.backend.nodes.state import State


class BaseNode(ABC):
    def __init__(
            self,
            node_name: str,
    ):
        self.node_name = node_name

    @abstractmethod
    def traverse(
            self,
            state: State,
    ) -> State:
        pass
