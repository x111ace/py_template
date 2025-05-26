import sys, os

# --- --- --- --- --- --- --- --- ---

def test_print_file_info():
    from mods import utils
    # The function print_file_info prints and returns file, dir, root info as strings.
    file_path, dir_path, root_path = utils.print_file_path(
        FILE=utils.MODULES_DIR,
        MODS=utils.SOURCE_CODE_DIR,
        ROOT=utils.FULL_PROJECT_ROOT
    )
    # Check that the returned values are as expected in structure and type.
    assert isinstance(file_path, str)
    assert isinstance(dir_path, str)
    assert isinstance(root_path, str)
    # Check that the returned values contain expected content.
    assert file_path.startswith("FILE PATH:")
    assert dir_path.startswith("DIRECTORY:")
    assert root_path.startswith("ROOT PATH:")

# --- --- --- --- --- --- --- --- ---

def run_tests():
    os.system("python -m pytest")

if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
    run_tests()
