# src/mods/graph/__init__.py

from ...mods import *
from ..utils import *



# MAIN APP STATE
class AppState(BaseModel):
    exit_app: bool = False
    inner_graph_snapshots: Optional[List[Dict[str, Any]]] = None



# ADD FORWARD DECLARATION FOR ALL NODES HERE
# ENSURE IT USES THE CORRECT NODE CLASS NAME
class ExampleNode(BaseNode[AppState]): ...



@dataclass
class MainMenu(BaseNode[AppState]): # INIT/MAIN NODE
    async def run(self, ctx: GraphRunContext[AppState]
                  ) -> Union[End, ExampleNode, 'MainMenu']: # Use string literal for self-reference
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
                # ADD GRAPH IMPORT HERE 
                from .test import test_graph
                # IMPORTANT: Clear the snapshots from AppState *before* returning.
                # This ensures they are part of the persisted state for *this* MainMenu completion,
                # but AppState is clean for the *next* node transition.
                if ctx.state.inner_graph_snapshots is not None:
                    ctx.state.inner_graph_snapshots = None 
                else:
                    printR("\nNo snapshots to clear.", speed=0.01)
                # test_graph returns a tuple: (exit_status, snapshots_data)
                should_exit_main_app, returned_snapshots = await test_graph()
                # Store the returned snapshots in the current AppState
                ctx.state.inner_graph_snapshots = returned_snapshots
                
                node_to_return = None
                if should_exit_main_app:
                    ctx.state.exit_app = True 
                    node_to_return = End(None)
                else:
                    # If inner graph didn't signal exit, return to MainMenu
                    node_to_return = MainMenu()

                return node_to_return
            else:
                printR("\nInvalid choice. Please try again.", speed=0.01)
                # Loop back by continuing the while loop, or explicitly return MainMenu() if preferred
                # If we just continue, the prompt reappears. Returning MainMenu() also achieves this.
                # Let's be explicit for clarity of state transition
                return MainMenu()
        # This part should ideally not be reached if all paths in while loop return.
        # However, as a fallback or if loop structure changes, it ensures an End.
        # return End(None) 