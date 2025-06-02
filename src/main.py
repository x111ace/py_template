# py_template/src/main.py

##################################
# --- Import Project Modules --- #
##################################

from pydantic_graph.mermaid import generate_code as mermaid_code_generator # Added import
from pydantic_graph.persistence.file import FileStatePersistence # Added import
from pydantic_graph import Graph

from src.mods.graph import AppState, MainMenu
from src.mods.graph.example import ExampleNode

from src.mods.__init__ import *
from src.mods.utils import *

###################################
# --- Define from __init__.py --- #
###################################

PY_PATH_MAIN = os.path.abspath(__file__)

SOURCE_CODE = os.path.dirname(PY_PATH_MAIN)
if SOURCE_CODE != SRC_DIR:
    print(f"SRC_DIR != SOURCE_CODE_DIR...")
else:
    SRC_DIR = SOURCE_CODE

MODULES = os.path.join(SRC_DIR, 'mods')
if MODULES != MOD_DIR:
    print(f"MODS_DIR != MODULES_DIR...")
else:
    MOD_DIR = MODULES

ROOTED = os.path.dirname(SRC_DIR)
if ROOTED != ROOTPTH:
    print(f"ROOT_DIR != FULL_PROJECT_ROOT...")
else:
    ROOTPTH = ROOTED

FILEi = print_file_path 
TR33 = print_project_tree

# --- --- --- --- --- --- --- --- ---

def main_graph(persist=False, mermaid=False):
    initial_node = MainMenu()
    state = AppState()
    app_graph = Graph(
        nodes=(MainMenu, ExampleNode), # ADD NODES HERE
        state_type=AppState)

    # Clear persistence file to start auto start fresh
    if persist == False and APP_PERSISTENCE_FILE.exists():
        os.remove(APP_PERSISTENCE_FILE)

    persistence = FileStatePersistence(APP_PERSISTENCE_FILE)
    persistence.set_graph_types(app_graph) # Register graph types

    # --- Graph Execution with Persistence ---
    async def run_with_persistence():
        # Try to load from persistence, otherwise start fresh
        initial_snapshot = await persistence.load_next()
        start_node = initial_snapshot.node if initial_snapshot else initial_node
        current_state = initial_snapshot.state if initial_snapshot else state
        
        if APP_PERSISTENCE_FILE.exists() and initial_snapshot: # Clear if we loaded something
            try:
                os.remove(APP_PERSISTENCE_FILE)
            except Exception as e:
                logging.warning(f"Could not clear old persistence file\n: {e}")

        async with app_graph.iter(start_node, state=current_state, persistence=persistence) as run:
            while True:
                next_node_or_end = await run.next()
                if isinstance(next_node_or_end, End):
                    # print(f"Graph ended with: {next_node_or_end.data}") # Optional: for debugging
                    break
                # print(f"Next node: {type(next_node_or_end).__name__}") # Optional: for debugging

    asyncio.run(run_with_persistence())
    
    # Clear persistence file to start auto start fresh
    if persist == False and APP_PERSISTENCE_FILE.exists():
        os.remove(APP_PERSISTENCE_FILE)

    # --- Generate and Print Mermaid Code ---
    if mermaid == True:
        mermaid_output = mermaid_code_generator(app_graph, start_node=initial_node, direction='TB')
        logging.info("Mermaid Diagram Code (Main Graph)\n```mermaid\n" + mermaid_output + "\n```")

def main():
    # FILEi(MOD=MOD_DIR, DIR=SRC_DIR, ROOT=ROOTPTH, output=True)
    # TR33(ROOT=ROOTPTH, output=True)
    main_graph()

