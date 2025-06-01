# src/mods/graph/__init__.py

from ...mods import *
from ..utils import *

"""
To add a new node:
1. Create a new file, using `example.py` as a reference.
2. Add a forward declaration for the new node in this file.
3. Add the node to the menu print statement, for display.
4. Add an `elif` statement for the new node in the `MainMenu`.
5. In `main.py`, import the node, and add it in the execution function.

To add a new graph:
1. Create a new folder, naming it as you wish for the new graph.
2. Use `test/` as a reference for the folder and file structure.
3. Create a main entry node and execute function in `__init__.py`.
4. Create new nodes as needed in the new folder, each as it's own file.
5. Replicate the entry from option `2` in `MainMenu` for the new graph.
"""

# MAIN APP STATE
class AppState(BaseModel):
    i_graph_: Optional[List[Dict[str, Any]]] = None
    exit_app: bool = False



# ADD FORWARD DECLARATION FOR ALL NODES HERE
# ENSURE IT USES THE CORRECT NODE CLASS NAME
class ExampleNode(BaseNode[AppState]): ...



@dataclass
class MainMenu(BaseNode[AppState]): # INIT/MAIN NODE
    async def run(self, ctx: GraphRunContext[AppState]
                  ) -> Union[End, ExampleNode]: # Use string literal for self-reference
        print("\n--- MAIN MENU ---\n"
              "\n[0] Exit\n"
              "\n[1] Example Node"
              "\n[2] Example Graph"
            # "\n[3] Newly Created"
            )
        
        while True:
            main_menu_option = await asyncio.to_thread(input, "\n> ")

            if main_menu_option == "0":
                ctx.state.exit_app = True
                printR("\nExiting...", speed=0.01)
                return End(None)
            


            # THIS EXAMPLE NODE WILL BE REPLACED WITH A CREATED NODE
            elif main_menu_option == "1":
                # ADD NODE IMPORT HERE 
                from .example import ExampleNode
                # PREVENTS CIRCULAR IMPORTS
                return ExampleNode()
                


            elif main_menu_option == "2":
                if ctx.state.i_graph_ is not None:
                    ctx.state.i_graph_ = None

                # ADD GRAPH IMPORT HERE 
                from .test import test_graph
                # RUN INNER GRAPH AND RETURN SNAPSHOTS OR EXIT FLAG
                exit_flag, returned_snapshots = await test_graph()

                ctx.state.i_graph_ = returned_snapshots
                node_to_return = None
                if exit_flag:
                    ctx.state.exit_app = True 
                    node_to_return = End(None)
                else:
                    node_to_return = MainMenu()
                return node_to_return
            

            
            else:
                printR("\nInvalid choice. Please try again.", speed=0.01)
