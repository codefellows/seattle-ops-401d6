# Ops Challenge - File Encryption Script Part 2 of 3

## Python os.walk()

- `OS.walk()` generates the file names in a directory tree by walking the tree either top-down or bottom-up.
- For each directory in the tree rooted at directory top (including top itself), yields a 3-tuple (dirpath, dirnames, filenames)
  - **root**: Prints out directories only from what you specified
  - **dirs**: Prints out sub-directories from root
  - **files**: Prints out all files from root and directories

**Example**

```python
# Driver function
import os

if __name__ == "__main__":
  for (root,dirs,files) in os.walk('.', topdown=True):
    print(root)
    print(dirs)
    print(files)
    print('--------------------------------------------')
```

## Demo Code

The demo code below introduces concepts necessary to complete the challenge.

```python
#!/usr/bin/env python3

# Purpose: In this demo, we'll recursively dig a folder for its contents, then return each path.
# This will allow us to perform operations en-masse, such as encryption.

# Import libraries
import os

# Begin recursive directory crawl
for root, dirs, files in os.walk(".", topdown=False):
# For each hit, concatenate the current directory pathing to left of result
   for file in files:
      print(os.path.join(root, file))
   for dir in dirs:
      print(os.path.join(root, dir))
```
