# src/run.py

import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

PY_PATH_RUN = os.path.abspath(__file__)

# --- --- --- --- --- --- --- --- ---

def run():
    from main import main
    main()

if __name__ == "__main__":
    run()