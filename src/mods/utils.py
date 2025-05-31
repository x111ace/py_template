# py_template/src/mods/utils.py

##################################
# --- Import Project Modules --- #
##################################

from .__init__ import *

PY_PATH_UTILS = os.path.abspath(__file__)

####################################
# --- File / Folder Operations --- #
####################################

def print_project_tree(ROOT, output=False):
    """
    Returns a complete file tree as a string, including all folders and subfolders recursively,
    using pretty tree characters (├──, └──, │). Folders and subfolders are listed first (top to bottom),
    then files, always in alphabetical order.

    Args:
        ROOT (str): The root directory to start the tree from.
        print_output (bool): If True, prints the tree. Always returns the tree as a string.

    Returns:
        str: The formatted file tree.
    """
    # [engineering] Ignore __pycache__ and .git folders. Folders before files, both sorted alphabetically.
    tree_lines = []

    def _tree(dir_path, prefix=""):
        # Exclude __pycache__ and .git folders
        entries = [e for e in os.listdir(dir_path) if e not in ("__pycache__", ".pytest_cache", ".git", "venv", "venv_test")]
        folders = sorted([e for e in entries if os.path.isdir(os.path.join(dir_path, e))])
        files = sorted([e for e in entries if not os.path.isdir(os.path.join(dir_path, e))])
        sorted_entries = folders + files
        entries_count = len(sorted_entries)
        for idx, entry in enumerate(sorted_entries):
            path = os.path.join(dir_path, entry)
            connector = "└── " if idx == entries_count - 1 else "├── "
            if os.path.isdir(path):
                tree_lines.append(f"{prefix}{connector}{entry}/")
                extension = "    " if idx == entries_count - 1 else "│   "
                _tree(path, prefix + extension)
            else:
                tree_lines.append(f"{prefix}{connector}{entry}")

    # Add the root directory itself
    tree_lines.append(os.path.basename(os.path.abspath(ROOT)) + "/")
    _tree(ROOT)
    file_tree = "\n".join(tree_lines)
    if output:
        print(file_tree)
    return file_tree

def print_file_path(MOD, DIR, ROOT, output=False):
    """
    Print the file path, directory, and root path of the current file.

    Returns:
        tuple: A tuple containing the file path, directory path, and root path.
    """
    # ---
    # print(f"This file {__file__}:", os.path.abspath(__file__)) 
    mod_path = ( # This file's path = scanbatchpdf\src\mods\scanbatchpdf.py
        f"MODULE:\n{ind2_4}{MOD}\n")
    # ---
    # print("This directory: ", os.path.dirname(os.path.abspath(__file__))) 
    dir_path = ( # This file's directory = scanbatchpdf\src\mods
        f"DIRECTORY:\n{ind2_4}{DIR}\n")
    # ---
    # print("This root folder:", os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
    root_path = ( # This file's parent directory = scanbatchpdf\mods
        f"ROOT PATH:\n{ind2_4}{ROOT}\n")
    # ---
    paths_to_print = (
        "--- File Path Info ---"
        +"\n\n"+
        "Printing info from this "
        +mod_path+"\n"+dir_path+"\n"+root_path
    )
    if output:
        print(paths_to_print)
    return mod_path, dir_path, root_path

def clean():
    """
    Clean the project's __pycache__ folder.
    """
    for root, dirs, files in os.walk(ROOTPTH):
        for dir in dirs:
            if dir in ("__pycache__", ".pytest_cache"):
                pycache_path = os.path.join(root, dir)
                shutil.rmtree(pycache_path)
        
#####################################
# --- CLI / Terminal Operations --- #
#####################################

def printR(text, speed=0.03, end='\n', flush=True, mode=None, elipses=False):
    """
    Print the given text to stdout one character at a time, with a speed between each character,
    and optionally transform the text using 'mode' (upper, lower, reverse).
    Adds a longer pause after punctuation for more natural pacing.
    If elipses=False, ellipses ("...") print at normal speed and are treated as mid-sentence punctuation; if True, they animate.

    Args:
        text (str): The text to print.
        speed (float|str): Speed in seconds between each character, or a string mode. Default is 0.03.
        end (str): String appended after the last character. Default is newline.
        flush (bool): Whether to flush after each character. Default is True.
        mode (str|None): Optional text transformation: 'upper', 'lower', 'reverse'.
        elipses (bool): Whether to animate ellipses. Default is True.
    """
    # If speed is a string and matches a mode, treat as mode for backward compatibility.
    _mode = speed if isinstance(speed, str) else None
    _speed = 0.03  # default

    # Mode-based configuration for speed
    if _mode in ("fastr", "fast", "normal", "slow", "instant"):
        if _mode == "fastr":
            _speed = 0.00639
        elif _mode == "fast":
            _speed = 0.012
        elif _mode == "normal":
            _speed = 0.024
        elif _mode == "slow":
            _speed = 0.036
        elif _mode == "instant":
            _speed = 0
    elif isinstance(speed, (int, float)):
        _speed = speed
    elif speed == "":
        _speed = 0.024

    # Text transformation via mode
    if mode == "reverse":
        text = str(text)[::-1]
    elif mode == "upper":
        text = str(text).upper()
    elif mode == "lower":
        text = str(text).lower()
    else:
        text = str(text)

    # Print logic with punctuation pause
    if _speed == 0:
        sys.stdout.write(text)
        sys.stdout.write(end)
        if flush:
            sys.stdout.flush()
        return

    mid_sentence_punctuation = {'-', '—', ',', ';', ':'}
    end_sentence_punctuation = {'.', '!', '?'}

    i = 0
    text_len = len(text)
    while i < text_len:
        # Check for ellipsis "..."
        if text[i:i+3] == "..." and elipses:
            ellipsis_speed = _speed * 8
            for _ in range(3):
                sys.stdout.write(".")
                if flush:
                    sys.stdout.flush()
                time.sleep(ellipsis_speed)
            for _ in range(3):
                sys.stdout.write("\b \b")
                if flush:
                    sys.stdout.flush()
                time.sleep(ellipsis_speed)
            for _ in range(3):
                sys.stdout.write(".")
                if flush:
                    sys.stdout.flush()
                time.sleep(ellipsis_speed)
            for _ in range(3):
                sys.stdout.write("\b \b")
                if flush:
                    sys.stdout.flush()
                time.sleep(ellipsis_speed)
            for _ in range(3):
                sys.stdout.write(".")
                if flush:
                    sys.stdout.flush()
                time.sleep(ellipsis_speed)
            if flush:
                sys.stdout.flush()
            time.sleep(_speed * 3)
            i += 3
            continue
        elif text[i:i+3] == "..." and not elipses:
            # Print the ellipsis at normal speed, but treat as mid-sentence punctuation for pause
            for j in range(3):
                sys.stdout.write(".")
                if flush:
                    sys.stdout.flush()
                time.sleep(_speed)
            # After printing "...", pause as if it were mid-sentence punctuation
            time.sleep(_speed * 8)
            i += 3
            continue
        char = text[i]
        sys.stdout.write(char)
        if flush:
            sys.stdout.flush()
        if char in end_sentence_punctuation:
            time.sleep(_speed * 14)
        elif char in mid_sentence_punctuation:
            time.sleep(_speed * 8)
        else:
            time.sleep(_speed)
        i += 1
    sys.stdout.write(end)
    if flush:
        sys.stdout.flush()
