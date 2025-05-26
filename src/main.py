# py_template/src/main.py

##################################
# --- Import Project Modules --- #
##################################

"""
Obj:
    - 1: Import project modules
    - 2: Define Library Imports
"""

# Obj: - 1:
from mods import __init__, utils

# Obj: - 2:
import os

###################################
# --- Define from __init__.py --- #
###################################

"""
Obj:
    - 1: Set variables for directories in `__init__.py`
    - 2: Set variables for functions in `utils.py`
    - 3: Define script variables for directories
"""

# Obj: - 1:
MODULES_DIR = __init__.MODULES_DIR # py_template\src\mods
SOURCE_CODE_DIR = __init__.SOURCE_CODE_DIR # py_template\src
FULL_PROJECT_ROOT = __init__.FULL_PROJECT_ROOT # py_template

# Obj: - 2:
printR = utils.printR 
FILEi = utils.print_file_path 
TR33 = utils.print_project_tree

# Obj: - 3:
PY_PATH_MAIN = os.path.abspath(__file__)

SRC_DIR = os.path.dirname(PY_PATH_MAIN)
SOURCE_CODE_DIR = SRC_DIR

MODS_DIR = os.path.join(SRC_DIR, 'mods')
MODULES_DIR = MODS_DIR

ROOT_DIR = os.path.dirname(SRC_DIR)
FULL_PROJECT_ROOT = ROOT_DIR

# --- --- --- --- --- --- --- --- ---

def main():
    FILEi(
        FILE=MODULES_DIR,
        MODS=SOURCE_CODE_DIR,
        ROOT=FULL_PROJECT_ROOT
    )
    
    TR33(ROOT=FULL_PROJECT_ROOT)

if __name__ == "__main__":      
    main()