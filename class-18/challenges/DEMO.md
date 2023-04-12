# Ops Challenge - Automated Brute Force Wordlist Attack Tool Part 3 of 3

## Demo Code

The demo code below introduces concepts necessary to complete the challenge.

This example code is from [How to Brute Force ZIP File Passwords in Python](https://www.thepythoncode.com/article/crack-zip-file-password-in-python).

```python

# Demo Class 18
#
# The Python "zipfile" library at https://docs.python.org/3/library/zipfile.html allows us to interact with files using the ZIP archive and compression standard. 

from zipfile import ZipFile

zip_file = ### Your password protected zip file ###
password = ### Password to guess ###

with ZipFile(zip_file) as zf:
  zf.extractall(pwd=bytes(password,'utf-8'))

```
"DEMO.md" 45L, 1015C                                                                                                                                                 1,1           Top


