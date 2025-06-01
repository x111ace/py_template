# src/mods/graph/test/__init__.py

from pydantic_graph import Graph

from ....mods import *
from ...utils import *

from .. import MainMenu


# NEW GRAPH STATE
class TestState(BaseModel):
    exit_app: bool = False

# ADD FORWARD DECLARATION FOR ALL NODES HERE
# ENSURE IT USES THE CORRECT NODE CLASS NAME
class TestNODE(BaseNode[TestState]): ...

@dataclass
class MainTestNODE(BaseNode[TestState]): # INIT/MAIN NODE
    async def run(self, ctx: GraphRunContext[TestState]
                  ) -> Union[End, TestNODE]: # ADD NODES HERE
        print("\nTHIS IS A GRAPH INSIDE OF A GRAPH\n"
              "\n--- GRAPH MENU ---\n"
              "\n[M] Return to Main Menu\n"
              "\n[1] Test NODE"
            # "\n[2] Newly Created"
            # "\n[3] Newly Created"
            )
        
        while True:
            graph_option = input("\n> ")

            if graph_option.lower() == "m":
                printR("\nReturning to Main Menu...", speed=0.01)
                return End(None)
            elif graph_option == "0":
                printR("\nExiting...", speed=0.01)
                ctx.state.exit_app = True
                return End(None)
            
            # THIS EXAMPLE NODE WILL BE REPLACED WITH A CREATED NODE
            elif graph_option == "1":
                # ADD NODE IMPORT HERE 
                from .testnode import TestNODE
                # PREVENTS CIRCULAR IMPORTS
                return TestNODE()
                
            else:
                printR("\nInvalid choice. Please try again.", speed=0.01)



# --- --- --- --- --- ------ --- ---



async def test_graph():
    printR("\nHello, from `ExampleGraph`! Beginning a new graph...", speed=0.01)
    # THIS NODE WILL BE CALLED FROM THE OUTER GRAPH, TO EXECUTE THE INNER GRAPH
    try:
        initial_node = MainTestNODE()
        state = TestState()
        app_graph = Graph(
            nodes=(MainTestNODE, TestNODE), # ADD NODES HERE
            state_type=TestState)
        await app_graph.run(initial_node, state=state)
    except Exception as e:
        logging.error(f"Occurred while running graph\n: {e}")
    finally:
        # RETURN TO POINT OF ENTRY
        return MainMenu()
