# src/mods/graph/test/__init__.py

from pydantic_graph.persistence.in_mem import FullStatePersistence # Corrected import
from pydantic_graph import Graph
import pydantic

from ....mods import *
from ...utils import *



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
            # Use asyncio.to_thread for blocking input in async function
            graph_option = await asyncio.to_thread(input, "\n> ")

            if graph_option.lower() == "m":
                printR("\nReturning to Main Menu...", speed=0.01)
                return End(None)
            elif graph_option == "0":
                ctx.state.exit_app = True
                printR("\nExiting...", speed=0.01)
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
    final_test_state = None
    session_snapshots: Optional[List[Dict[str, Any]]] = [] # Initialize as empty list
    
    # Use in-memory FullStatePersistence for this run of the inner graph
    # A new instance is created each time test_graph is called, so history is fresh.
    in_memory_persistence = FullStatePersistence()
    # in_memory_persistence.deep_copy = False # Optional: if state/nodes are simple and deep copies are slow

    from .testnode import TestNODE # Ensure TestNODE is imported correctly
    inner_app_graph = Graph(
        nodes=(MainTestNODE, TestNODE),
        state_type=TestState
    )
    # Set graph types for the in-memory persistence instance
    in_memory_persistence.set_graph_types(inner_app_graph) # Corrected call

    try:
        # No need to load initial snapshot for a fresh in-memory persistence run typically,
        # unless you have a more complex resumption logic for the inner graph itself.
        start_test_node = MainTestNODE()
        current_test_state = TestState()

        # No file to clear

        async with inner_app_graph.iter(start_test_node, state=current_test_state, persistence=in_memory_persistence) as run:
            while True:
                next_node_or_end = await run.next()
                if isinstance(next_node_or_end, End):
                    break
            final_test_state = current_test_state
        
        # After the run, get snapshots using the persistence object's own type adapter
        if hasattr(in_memory_persistence, '_snapshots_type_adapter') and in_memory_persistence._snapshots_type_adapter:
            session_snapshots = in_memory_persistence._snapshots_type_adapter.dump_python(
                in_memory_persistence.history,
                mode='json', # Ensures Pydantic models within snapshots are dicts
                # exclude_unset=True # Optional: if you want to skip fields that were not explicitly set
            )
        else:
            logging.error("[test_graph] Snapshot type adapter not found or not set on in_memory_persistence!")
            session_snapshots = [] # Default to empty list if adapter is missing

    except Exception as e:
        logging.error(f"Occurred while running inner graph\n: {e}")
        # Ensure session_snapshots is initialized if an error occurs before its assignment
        if 'session_snapshots' not in locals():
            session_snapshots = []
    finally:
        exit_status = final_test_state.exit_app if final_test_state else False
        logging.info(f"Returning in-memory snapshots\n: {session_snapshots}")
        return exit_status, session_snapshots
