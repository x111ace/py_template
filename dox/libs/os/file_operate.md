# `os` module cheat sheet

## Low-Level File Operations

### Open a file (returns a file descriptor)
```python
fd = os.open('file.txt', os.O_RDWR | os.O_CREAT)
```
-→ Opens a file for reading and writing. Returns a file descriptor (an integer). Use flags like `os.O_RDONLY`, `os.O_WRONLY`, `os.O_RDWR`, `os.O_CREAT`, etc.

### Read from a file descriptor
```python
content = os.read(fd, 1024)  # Read up to 1024 bytes
```
-→ Reads bytes from the file descriptor. Returns a bytes object.

### Write to a file descriptor
```python
os.write(fd, b'Hello, world!')
```
-→ Writes bytes to the file descriptor. Data must be bytes, not str.

---

### Move file pointer (seek)
```python
os.lseek(fd, 0, os.SEEK_SET)  # Move to start of file
```
-→ Moves the file descriptor's read/write position. Use `os.SEEK_SET`, `os.SEEK_CUR`, or `os.SEEK_END` for the third argument.

### Duplicate a file descriptor
```python
fd2 = os.dup(fd)
```
-→ Returns a duplicate of the file descriptor.

### Duplicate a file descriptor to a given fd
```python
os.dup2(fd, fd2)
```
-→ Duplicates fd to fd2, closing fd2 first if necessary.

### Get file metadata from a file descriptor
```python
stats = os.fstat(fd)
```
-→ Returns stat info (like os.stat, but for a file descriptor).

### Change permissions using a file descriptor
```python
os.fchmod(fd, 0o644)
```
-→ Changes file permissions (mode) for the open file.

### Change owner/group using a file descriptor
```python
os.fchown(fd, uid, gid)
```
-→ Changes the owner (uid) and group (gid) of the open file.

### Flush file changes to disk
```python
os.fsync(fd)
```
-→ Forces the OS to write all changes to disk for the given file descriptor.

### Flush file data (not metadata) to disk
```python
os.fdatasync(fd)
```
-→ Like fsync, but only flushes file data, not metadata (if supported by the OS).

### Close a file descriptor
```python
os.close(fd)
```
-→ Closes the file descriptor. Always close files when done.

---

### Truncate a file to a given length
```python
os.ftruncate(fd, length)
```
-→ Truncates the file to the specified length (in bytes).

### Rename a file
```python
os.rename('old.txt', 'new.txt')
```
-→ Renames a file or directory.

### Remove (delete) a file
```python
os.remove('file.txt')
```
-→ Deletes the specified file. Raises FileNotFoundError if it doesn't exist.

### Remove (delete) a file (alias for remove)
```python
os.unlink('file.txt')
```
-→ Another way to delete a file (identical to os.remove).

### Create a hard link
```python
os.link('source.txt', 'dest.txt')
```
-→ Creates a hard link pointing to the source file.

### Create a symbolic link
```python
os.symlink('source.txt', 'dest_link.txt')
```
-→ Creates a symbolic (soft) link pointing to the source file.

### Read the target of a symbolic link
```python
os.readlink('dest_link.txt')
```
-→ Returns the path to which the symbolic link points.

### Test permissions for a path
```python
os.access('file.txt', os.R_OK | os.W_OK)
```
-→ Checks if the file is readable and writable by the current process. Returns True or False.

### Example: Write and read a file using file descriptors
```python
import os
fd = os.open('example.txt', os.O_RDWR | os.O_CREAT)
os.write(fd, b'abc123')
os.lseek(fd, 0, os.SEEK_SET)  # Move to start of file
content = os.read(fd, 6)
print(content)  # b'abc123'
os.close(fd)
```
-→ Demonstrates writing, seeking, reading, and closing a file using low-level os functions.

### Error handling example
```python
import os
try:
    fd = os.open('nofile.txt', os.O_RDONLY)
except FileNotFoundError:
    print('File does not exist!')
```
-→ Shows how to handle errors when opening files.

# See also: [`os` file object docs](https://docs.python.org/3/library/os.html#os-file-objects)
