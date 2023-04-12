# Ops Challenge - Network Scanning with Scapy Part 1 of 3

# Python scapy

Scapy is a free and open-source tool used for packet manipulation programs. Scapy can decode data packets and can capture them.

Install scapy using the command `pip3 install scapy-python3`

**Scapy functions**

- `ARP()`: This function allows us to create ARP packets (request or response)

```python
import scapy.all as scapy

request = scapy.ARP()
```

- `summary()`: This method provides you with the status of the packet that we have created. Only gives you the basic idea (what is the type of packet, destination, etc.)

```python
import scapy.all as scapy

request = scapy.ARP()
print(request.summary())
```

- `show()`: Gives you more detailed information about the packet

```python
import scapy.all as scapy

request = scapy.ARP()
print(request.show())
```

- `ls()`: Allows you to see what are the fields that we can set for a specific packet

```python
import scapy.all as scapy

request = scapy.ARP()
print(scapy.ls(scapy.ARP()))
```

**Steps for creating Network Scanner**

Steps for creating Network Scanner –

1. Create an ARP packet using ARP() method.
2. Set the network range using variable.
3. Create an Ethernet packet using Ether() method.
4. Set the destination to broadcast using variable hwdst.
5. Combine ARP request packet and Ethernet frame using ‘/’.
6. Send this to your network and capture the response from different devices.
7. Print the IP and MAC address from the response packets.

## Demo Code

The demo code below introduces concepts necessary to complete the challenge.

This first example takes an IP or a name as first parameter, send an ICMP echo request packet and display the completely dissected return packet:

```python

#! /usr/bin/env python

import sys
from scapy.all import sr1,IP,ICMP

p=sr1(IP(dst=sys.argv[1])/ICMP())
if p:
    p.show()

```

The second example scans a specific port on a given host IP, then returns the response.

```python

#! /usr/bin/env python3

# Run this with sudo

from scapy.all import ICMP, IP, sr1, TCP

# Define target host and TCP port to scan
host = "scanme.nmap.org"
port_range = 22
src_port = 22
dst_port = 22

response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)

print(response)

```
