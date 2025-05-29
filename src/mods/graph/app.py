from pydantic_graph import BaseNode, GraphRunContext, End
from dataclasses import dataclass
from ..utils import printR

# STATE
class AppState:
    pass

# FORWARD DECLARATION
class MainMenu(BaseNode[AppState]): ...

# MAIN NODE
@dataclass
class MainMenu(BaseNode[AppState]):
    async def run(self, ctx: GraphRunContext[AppState]) -> End:
        print("\n--- MAIN MENU ---\n"
              "\n[0] Exit\n")
        while True:
            main_menu_option = input("> ")
            if main_menu_option == "0":
                printR("\nExiting...")
                return End(None)
            else:
                printR("\nInvalid choice. Please try again.\n", speed=0.01)
