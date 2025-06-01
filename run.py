# src/run.py

from src.mods import *

PY_PATH_RUN = os.path.abspath(__file__)

def handle_exit(signum, frame):
    print("\n\n(Ctrl+C) Exiting...")
    from src.mods.utils import clean
    clean()
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_exit)
    try:
        from src.main import main
        main()
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        from src.mods.utils import clean
        clean()