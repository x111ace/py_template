from pydantic_graph import BaseNode, GraphRunContext
from dataclasses import dataclass

from ..utils import printR

from . import AppState
from . import MainMenu

@dataclass
class ExampleNode(BaseNode[AppState]):
    async def run(self, ctx: GraphRunContext[AppState]) -> MainMenu:
        printR("\nHello.\nHello,\nHello.\nHello, from `ExampleNode`! Returning to `MainMenu`...")
        return MainMenu()
