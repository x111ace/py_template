import sys, os

# --- --- --- --- --- --- --- --- ---

def test_print_file_info():
    from src.mods.__init__ import MOD_DIR, SRC_DIR, ROOTPTH
    from src.mods.utils import print_file_path

    # The function print_file_info prints and returns file, dir, root info as strings.
    mod_path, dir_path, root_path = print_file_path(
        MOD=MOD_DIR,
        DIR=SRC_DIR,
        ROOT=ROOTPTH
    )
    # Check that the returned values are as expected in structure and type.
    assert isinstance(mod_path, str)
    assert isinstance(dir_path, str)
    assert isinstance(root_path, str)
    # Check that the returned values contain expected content.
    assert mod_path.startswith("MODULE:")
    assert dir_path.startswith("DIRECTORY:")
    assert root_path.startswith("ROOT PATH:")

# --- --- --- --- --- --- --- --- ---

def run_tests():
    os.system("python -m pytest")

if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
    run_tests()
