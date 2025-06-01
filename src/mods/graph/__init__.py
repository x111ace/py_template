# src/mods/graph/__init__.py

from ...mods import *
from ..utils import *



# MAIN APP STATE
class AppState(BaseModel):
    exit_app: bool = False



# ADD FORWARD DECLARATION FOR ALL NODES HERE
# ENSURE IT USES THE CORRECT NODE CLASS NAME
class ExampleNode(BaseNode[AppState]): ...



@dataclass
class MainMenu(BaseNode[AppState]): # INIT/MAIN NODE
    async def run(self, ctx: GraphRunContext[AppState]
                  ) -> Union[End, ExampleNode]: # ADD NODES HERE
        print("\n--- MAIN MENU ---\n"
              "\n[0] Exit\n"
              "\n[1] Example Node"
              "\n[2] Example Graph"
            # "\n[3] Newly Created"
            )
        
        while True:
            main_menu_option = input("\n> ")



            if main_menu_option == "0":
                printR("\nExiting...", speed=0.01)
                return End(None)
            


            # THIS EXAMPLE NODE WILL BE REPLACED WITH A CREATED NODE
            elif main_menu_option == "1":
                # ADD NODE IMPORT HERE 
                from .example import ExampleNode
                # PREVENTS CIRCULAR IMPORTS
                return ExampleNode()
                


            elif main_menu_option == "2":
                # ADD GRAPH IMPORT HERE 
                from .test import test_graph
                # PREVENTS CIRCULAR IMPORTS
                await test_graph()
                # THIS PART WON'T WORK IF
                # USING A NODE vs FUNCTION
                if ctx.state.exit_app:
                    return End(None)



            else:
                printR("\nInvalid choice. Please try again.", speed=0.01)



            return End(None)