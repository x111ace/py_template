from pydantic_graph import BaseNode, GraphRunContext, End
from dataclasses import dataclass
from typing import Union

from ..utils import printR

# STATE
class AppState:
    pass

# FORWARD DECLARATION
class ExampleNode(BaseNode[AppState]): ...

# MAIN NODE
@dataclass
class MainMenu(BaseNode[AppState]):
    async def run(self, ctx: GraphRunContext[AppState]) -> Union[End, ExampleNode]:
        print("\n--- MAIN MENU ---\n"
              "\n[0] Exit\n[1] Example Node\n")
        while True:
            main_menu_option = input("> ")



            if main_menu_option == "0":
                printR("\nExiting...")
                return End(None)
            


            elif main_menu_option == "1":
                # Import here to avoid circular import
                from .app import ExampleNode
                return ExampleNode()
            


            else:
                printR("\nInvalid choice. Please try again.\n", speed=0.01)
