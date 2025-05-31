# py_template/src/main.py

##################################
# --- Import Project Modules --- #
##################################

# ADD FORWARD DECLARED NODES HERE AFTER STATE AND MAIN NODE

from src.mods.graph import AppState, MainMenu, ExampleNode, ExampleGraphNODE
from src.mods.__init__ import *
from src.mods.utils import *

from pydantic_graph import Graph
import asyncio
import os

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

# Obj: - 2:
FILEi = print_file_path 
TR33 = print_project_tree

# --- --- --- --- --- --- --- --- ---

def main_graph():
    initial_node = MainMenu()
    state = AppState()
    app_graph = Graph(
        nodes=(MainMenu, ExampleNode, ExampleGraphNODE), # ADD NODES HERE
        state_type=AppState)
    asyncio.run(app_graph.run(initial_node, state=state))

def main():
    # FILEi(MOD=MOD_DIR, DIR=SRC_DIR, ROOT=ROOTPTH, output=True)
    TR33(ROOT=ROOTPTH, output=True)
    main_graph()
