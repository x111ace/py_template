# src/mods/graph/test/__init__.py

from pydantic_graph.mermaid import generate_code as mermaid_code_generator # Added import
from pydantic_graph.persistence.in_mem import FullStatePersistence
from pydantic_graph import Graph
import pydantic

from ....mods import *
from ...utils import *

"""
To add a new node:
1. Create a new file, using `testnode.py` as a reference.
2. Add a forward declaration for the new node in this file.
3. Add the node to the menu print statement, for display.
4. Add an `elif` statement for the new node in the `MainNODE`.
5. Import and add the new node to the execution function.
"""

# NEW GRAPH STATE
class InnerState(BaseModel):
    exit_app: bool = False



# ADD FORWARD DECLARATION FOR ALL NODES HERE
# ENSURE IT USES THE CORRECT NODE CLASS NAME
class TestNODE(BaseNode[InnerState]): ...



@dataclass
class MainNODE(BaseNode[InnerState]): # INIT/MAIN NODE
    async def run(self, ctx: GraphRunContext[InnerState]
                  ) -> Union[End, TestNODE]: # ADD NODES HERE
        print("\n--- GRAPH MENU ---\n"
              "\n[0] Exit\n"
              "\n[1] Test NODE"
            # "\n[2] Newly Created"
            # "\n[3] Newly Created"
              "\n\n[M] Main Menu"
            )
        
        while True:
            # Use asyncio.to_thread for blocking input in async function
            graph_option = await asyncio.to_thread(input, "\n> ")

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



async def test_graph(persist=False, mermaid=False):
    printR("\nHello, from `ExampleGraph`! Beginning a new graph...", speed=0.01)
    session_snapshots: Optional[List[Dict[str, Any]]] = [] # Initialize as empty list
    # Use in-memory FullStatePersistence to track the inner graph's session snapshots
    # New instance is created each time the inner graph is called, with fresh history.
    in_memory_persistence = FullStatePersistence()
    final_state = None

    # IMPORT NODES HERE TO AVOID CIRCULAR IMPORTS
    from .testnode import TestNODE 

    # SETUP INNER GRAPH
    inner_app_graph = Graph(
        nodes=(MainNODE, TestNODE), # ADD NODES HERE
        state_type=InnerState
    )

    # SET INNER GRAPH PERSISTENCE
    in_memory_persistence.set_graph_types(inner_app_graph) # Corrected call

    # RUN INNER GRAPH
    try:
        # No need to load initial snapshot for a fresh in-memory persistence run typically,
        # unless you have a more complex resumption logic for the inner graph itself.
        start_node = MainNODE()
        current_state = InnerState()

        # No file to clear

        async with inner_app_graph.iter(start_node, state=current_state, persistence=in_memory_persistence) as run:
            while True:
                next_node_or_end = await run.next()
                if isinstance(next_node_or_end, End):
                    break
            final_state = current_state
        
        # After the run, get snapshots using the persistence object's own type adapter
        if hasattr(in_memory_persistence, '_snapshots_type_adapter') and in_memory_persistence._snapshots_type_adapter:
            session_snapshots = in_memory_persistence._snapshots_type_adapter.dump_python(
                in_memory_persistence.history,
                mode='json', # Ensures Pydantic models within snapshots are dicts
                # exclude_unset=True # Optional: if you want to skip fields that were not explicitly set
            )
        else:
            logging.error("Snapshot type adapter not found or not set on in_memory_persistence!")
            session_snapshots = [] # Default to empty list if adapter is missing

    except Exception as e:
        logging.error(f"Occurred while running inner graph\n: {e}")
        # Ensure session_snapshots is initialized if an error occurs before its assignment
        if 'session_snapshots' not in locals():
            session_snapshots = []
    finally:
        exit_flag = final_state.exit_app if final_state else False
        if persist == True:
            logging.info(f"Returning in-memory snapshots.\n: {session_snapshots}")

        if mermaid == True:
            # --- Generate and Print Mermaid Code ---
            mermaid_output = mermaid_code_generator(inner_app_graph, start_node=start_node, direction='TB')
            logging.info("Mermaid Diagram Code (Inner Graph)\n```mermaid\n" + mermaid_output + "\n```")

        return exit_flag, session_snapshots
    
