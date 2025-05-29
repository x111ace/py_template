# src/run.py

import os

PY_PATH_RUN = os.path.abspath(__file__)

if __name__ == "__main__":
    from src.main import main
    main()
    from src.mods.utils import clean
    clean()