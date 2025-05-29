# `os` module cheat sheet

## Directory Traversal

### Iterate over directory entries (with more info)
```python
with os.scandir('some/dir') as entries:
    for entry in entries:
        print(entry.name, entry.is_file(), entry.is_dir())
```
-→ Yields DirEntry objects, which have methods to check if the entry is a file or directory, and more metadata.

---

### Recursively walk through directories
```python
for root, dirs, files in os.walk('some/dir'):
    print('Root:', root)
    print('Dirs:', dirs)
    print('Files:', files)
```
-→ Walks the directory tree from top to bottom, yielding a tuple for each directory: (current path, list of subdirectories, list of files).

---

### Example: Find all files with a certain extension
```python
import os
for root, dirs, files in os.walk('some/dir'):
    for file in files:
        if file.endswith('.txt'):
            print(os.path.join(root, file))
```
-→ Prints the full path of every `.txt` file in the directory tree.

---

### Example: Recursively count all files
```python
import os
def count_files(path):
    count = 0
    for _, _, files in os.walk(path):
        count += len(files)
    return count
# Usage: count_files('some/dir')
```
-→ Returns the total number of files in the directory and all subdirectories.

---

### Example: Using recursion to traverse directories (manual pattern)
```python
import os
def traverse(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            traverse(entry.path)
        else:
            print(entry.path)
# Usage: traverse('some/dir')
```
-→ Recursively prints the path of every file in the directory tree using `os.scandir`.

---

# See also: [`os` directory functions docs](https://docs.python.org/3/library/os.html#os-directory-funcs)
