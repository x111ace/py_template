# py_template/src/main.py

##################################
# --- Import Project Modules --- #
##################################

from mods.graph.app import AppState, MainMenu
from mods import __init__, utils

from pydantic_graph import Graph
import asyncio
import os

###################################
# --- Define from __init__.py --- #
###################################

PY_PATH_MAIN = os.path.abspath(__file__)

SOURCE_CODE_DIR = __init__.SOURCE_CODE_DIR # py_template\src
SRC_DIR = os.path.dirname(PY_PATH_MAIN)
if SRC_DIR != SOURCE_CODE_DIR:
    print(f"SRC_DIR != SOURCE_CODE_DIR...")
else:
    SOURCE_CODE_DIR = SRC_DIR

MODULES_DIR = __init__.MODULES_DIR # py_template\src\mods
MODS_DIR = os.path.join(SRC_DIR, 'mods')
if MODS_DIR != MODULES_DIR:
    print(f"MODS_DIR != MODULES_DIR...")
else:
    MODULES_DIR = MODS_DIR

FULL_PROJECT_ROOT = __init__.FULL_PROJECT_ROOT # py_template
ROOT_DIR = os.path.dirname(SRC_DIR)
if ROOT_DIR != FULL_PROJECT_ROOT:
    print(f"ROOT_DIR != FULL_PROJECT_ROOT...")
else:
    FULL_PROJECT_ROOT = ROOT_DIR

# Obj: - 2:
printR = utils.printR 
FILEi = utils.print_file_path 
TR33 = utils.print_project_tree

# --- --- --- --- --- --- --- --- ---

def main():
    initial_node = MainMenu()
    state = AppState()
    app_graph = Graph(
        nodes=(MainMenu,), # ADD NODES HERE
        state_type=AppState)
    asyncio.run(app_graph.run(initial_node, state=state))


if __name__ == "__main__":      
    main()
    TR33(ROOT=FULL_PROJECT_ROOT, output=True)
    FILEi(MOD=MODULES_DIR, DIR=SOURCE_CODE_DIR, ROOT=FULL_PROJECT_ROOT, output=True)
