# Ops Challenge - Signature-based Malware Detection Part 1 of 3

## Demo Code

### Searching in Windows Command Prompt

Let's practice searching Windows from Command Prompt for specific files and folders. These commands will demonstrate recursion, wildcarding, and the use of options associated with the `dir` command. Be sure to use Command Prompt and not PowerShell.

```
# Open Command Prompt. View manual to dir using:
dir /?

# Note that /B uses bare format, and /S recursively displays files and directories.

# Search a specific file in this directory using this syntax.
dir /b/s *.file_extension

# Example: dir /b/s *.png would search for all png files recursively

# Alternatively, we can search for a file by name
dir "\search term*" /s

# Example: dir *picture*.jpg /s

# We can search for folders recursively as well.
dir "Name of folder to search" /AD /b /s

# Example: dir Images /AD /b /s

# If you only know the partial name of the folder you're looking for, try:
dir /s/b /A:D "D:*partial-name-of-folder*"

# Example: dir /s/b /A:D "D:*Stea*" would help you find folders with the word "steam" in their names
```
### Searching Linux from Bash

Here's how we might search recursively search a directory in Linux for a file by its name.

```bash
find [DIR TO SEARCH] -name [FILE NAME]
```
