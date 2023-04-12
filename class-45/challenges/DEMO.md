# Ops Challenge - Create a Banner Grabber

## Demo Code

Copy this template down to your local coding environment and finish all TODOs.

The purpose of this script is to perform a banner grab using the python `socket` library.

```python
#!/usr/bin/python3

import socket

def bannergrab(host, port):
    timeout = #TODO: Set a timeout value.
    sockmod = socket.socket()
    sockmod.#TODO: Insert the correct `socket` function name here that accepts the host IP, then port number as parameters.
    sockmod.settimeout(timeout)
    print(sockmod.recv(1024))

def main():
    host = #TODO: Prompt the user to type an IP.
    port = #TODO: Prompt the user to type a port number that we'll convert to a "string" data type.
    bannergrab(host, port)

main()
```
