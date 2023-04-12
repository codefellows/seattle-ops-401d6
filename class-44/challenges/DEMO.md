# Ops Challenge - Create a Port Scanner

## Demo Code

Copy this template down to your local coding environment and finish all TODOs.

The purpose of this script is to determine if a target port is open or closed, using strictly Python 3 commands. To do so, we'll be importing the socket module, a low-level networking interface for Python.

```python
#!/usr/bin/python3

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = # TODO: Set a timeout value here.
sockmod.settimeout(timeout)

hostip = # TODO: Collect a host IP from the user.
portno = # TODO: Collect a port number from the user, then convert it to an integer data type.

def portScanner(portno):
    if sockmod.FUNCTION((hostip, portno)): # TODO: Replace "FUNCTION" with the appropriate socket.function call as found in the [socket docs](https://docs.python.org/3/library/socket.html)
        print("Port closed")
    else:
        print("Port open")

portScanner(port)
```
