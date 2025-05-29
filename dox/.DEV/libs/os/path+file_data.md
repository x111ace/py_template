# `os` module cheat sheet

## Path and File Metadata

### Get file or directory metadata (stat)
`file_stats = os.stat('some/file/or/dir')`
-→ Returns a data object with information about the file or folder, such as its size, when it was last changed, and its permissions.

### Get metadata for a symbolic link itself (not the target)
`link_stats = os.lstat('some/symlink')`
-→ Like `os.stat`, but if the path is a shortcut (symbolic link), this gives info about the link itself, not the file it points to.

---

### Get file size (in bytes)
`file_size = os.stat('file.txt').st_size`
-→ The number of bytes in the file. For example, 2048 means the file is 2 KB.

---

### Get last modification time (as a timestamp)
`mod_time = os.stat('file.txt').st_mtime`
-→ The time the file was last changed, as a number (seconds since Jan 1, 1970). You can convert this to a readable date with the `time` module.

---

### Get last access time (as a timestamp)
`access_time = os.stat('file.txt').st_atime`
-→ The last time the file was opened or read, as a timestamp.

---

### Get creation time (Windows) or "ctime" (Unix: metadata change time)
`creation_time = os.stat('file.txt').st_ctime`
-→ On Windows, this is when the file was created. On Unix, this is when the file's info (like permissions) was last changed.

---

### Change file permissions
`os.chmod('file.txt', 0o644)`
-→ Changes who can read or write the file. For example, `0o644` means the owner can read/write, others can only read.

---

### Get file mode (permissions, as an int)
`file_mode = os.stat('file.txt').st_mode`
-→ A number that shows the file's permissions and type (like if it's a file or folder). You can use the `stat` module to read this more easily.

---

### Change file timestamps (access and modified)
`os.utime('file.txt', (new_atime, new_mtime))`
-→ Sets the last access and last modified times for the file. You give it two numbers (timestamps).

---

### Get metadata from an open file descriptor
`fd_stats = os.fstat(fd)`
-→ Gets file information using a file descriptor (an integer you get from opening a file with `os.open` or from `file.fileno()`).

---

### Example: Print file size and modification time
```python
import os
stats = os.stat('file.txt')
print("Size:", stats.st_size)        # prints the file size in bytes
print("Modified:", stats.st_mtime)   # prints the last modified time (timestamp)
```

# See also: [`os.stat` docs](https://docs.python.org/3/library/os.html#os.stat)
