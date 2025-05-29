# `os` module cheat sheet

## Path and File Metadata

### Get the name of the current file
`file_name = os.path.basename(__file__)` 
-→ 'main.py'

---

### Get the directory containing the current file
`current_dir = os.path.dirname(__file__)` 
-→ '/home/user/project/src'

---

### Get the absolute path of the current file
`absolute_file_path = os.path.abspath(__file__)` 
-→ '/home/user/project/src/main.py'

---

### Join paths safely (cross-platform)
`joined_path = os.path.join('folder', 'file.txt')` 
-→ 'folder/file.txt' or 'folder\\file.txt'

---

### Split a path into (head, tail)
`head, tail = os.path.split('/home/user/file.txt')` 
-→ ('/home/user', 'file.txt')

---

#### Check if a path exists
`path_exists = os.path.exists('some/path')`

---

#### List files in a directory
`files_in_dir = os.listdir('some/dir')`

---

#### Create a directory (if it doesn't exist)
`os.makedirs('some/dir', exist_ok=True)`

---

#### Remove a file
`os.remove('file.txt')`

---

#### Remove a directory
`os.rmdir('empty_dir')`

---

#### Get environment variable (returns None if not set)
`home_env = os.environ.get('HOME')`

---

#### Set environment variable
`os.environ['MY_VAR'] = 'value'`

---
## Example: Print file and directory info
```python
print("File:", os.path.basename(__file__))
print("Dir :", os.path.dirname(__file__))
print("Abs :", os.path.abspath(__file__))
```
# See also: [`os.path` docs](https://docs.python.org/3/library/os.path.html)