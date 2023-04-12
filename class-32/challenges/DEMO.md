# Ops Challenge - Signature-based Malware Detection Part 2 of 3

## Demo Code

The demo code below introduces concepts necessary to complete the challenge.

```python
# Python program to find the SHA-1 message digest of a file
# importing the hashlib module
import hashlib

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

# substitute file name below as the parameter
message = hash_file("track1.mp3")
print(message)

```

This next demo code generate MD5 hash from a target file.

```python
# Python program to find MD5 hash value of a file
import hashlib
 
filename = input("Enter the file name: ")
md5_hash = hashlib.md5()
with open(filename,"rb") as f:
    # Read and update hash in chunks of 4K
    for byte_block in iter(lambda: f.read(4096),b""):
        md5_hash.update(byte_block)
    print(md5_hash.hexdigest())
```
