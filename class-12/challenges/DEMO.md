# Ops Challenge - Network Scanning with Scapy Part 2 of 3

## Python ipaddress module

Python's `ipaddress` module which provides the ability to create, manipulate and operate on IPv4 and IPv6 addresses and networks. This is included with Python 3.3+, so you do not need to install it.

### `IPv4Address` Objects

The `IPv4Address` objects have attributes relevant to IPv4 address. `ipaddress.IPv4Address('address')` construct an IPv4Address object representing IPv4 address 'address'

Attributes:

- `max_prefixlen`: Return the total number of bits in the IP address represented by IPv4Address object (32 for IPv4 and 128 for IPv6).
- `is_multicast`: Return True if the address is reserved for multicast use.
- `is_private`: Return True if the address is allocated for private networks.
- `is_global`: Return True if the address is allocated for public networks.
- `is_unspecified`: Return True if the address is unspecified.
- `is_reserved`: Return True if the address is otherwise IETF reserved.
- `is_loopback`: Return True if this is a loopback address.
- `is_link_local`: Return True if the address is reserved for link-local usage.

Examples:

```python
import ipaddress

# Creating an object of IPv4Address class and
# initializing it with an IPv4 address.
ip = ipaddress.IPv4Address('112.79.234.30')

# Print total number of bits in the ip.
print("Total no of bits in the ip: ", ip.max_prefixlen)

# Print True if the IP address is reserved for multicast use.
print("Is multicast: ", ip.is_multicast)

# Print True if the IP address is allocated for private networks.
print("Is private: ", ip.is_private)

# Print True if the IP address is global.
print("Is global: ", ip.is_global)

# Print True if the IP address is unspecified.
print("Is unspecified: ", ip.is_unspecified)

# Print True if the IP address is otherwise IETF reserved.
print("Is reversed: ", ip.is_reserved)

# Print True if the IP address is a loopback address.
print("Is loopback: ", ip.is_loopback)

# Print True if the IP address is Link-local
print("Is link-local: ", ip.is_link_local)

# next ip address
ip1 = ip + 1
print("Next ip: ", ip1)

# previous ip address
ip2 = ip - 1
print("Previous ip: ", ip2)

# Print True if ip1 is greater than ip2
print("Is ip1 is greater than ip2: ", ip1 > ip2)
```

### `IPv4Network` Objects

IPv4Network objects are used to inspect and define IP network.

Attributes:

- `network_address`: Return the network address for the network.
- `broadcast_address`: Return the broadcast address for the network. Packets sent to the broadcast address should be received by every host on the network.
- `netmask`: Return network mask of the network.
- `with_netmask`: Return a string representation of the network, with the mask in netmask notation.
- `with_hostmask`: Return a string representation of the network, with the mask in host mask notation.
- `prefixlen`: Return the length of the network prefix in bits.
- `num_addresses`: Return the total number of the address of this network.
- `hosts()`: Returns an iterator over the usable hosts in the network. The usable hosts are all the IP addresses that belong to the network, except the network address itself and the network broadcast address.
- `overlaps(other)`: Return True if this network is partly or wholly contained in other or other is wholly contained in this network.
- `subnets(prefixlen_diff)`: Return the subnets that join to make the current network definition, depending on the argument values. The prefixlen_diff parameter is the integer that indicates the amount our prefix length should be increased by.
- `supernet(prefixlen_diff)`: Return the supernet containing this network definition, the prefixlen_diff is the amount our prefix length should be decreased by.
- `subnet_of(other)`: Return True if this network is a subnet of other (new in python 3.7).
- `supernet_of(other)`: Return True if this network is a supernet of other (new in python 3.7).
- `compare_networks(other)`: Compare ip network with the other IP network. In this comparison only the network addresses are considered, host bits aren’t. It returns either -1, 0, or 1.

Examples:

```python
import ipaddress

# Initializing an IPv4 Network.
network = ipaddress.IPv4Network("192.168.1.0/24")

# Print the network address of the network.
print("Network address of the network: ", network.network_address)

# Print the broadcast address
print("Broadcast address: ", network.broadcast_address)

# Print the network mask.
print("Network mask: ", network.netmask)

# Print with_netmask.
print("with netmask: ", network.with_netmask)

# Print with_hostmask.
print("with_hostmask: ", network.with_hostmask)

# Print Length of network prefix in bits.
print("Length of network prefix in bits: ", network.prefixlen)

# Print the number of hosts under the network.
print("Total number of hosts under the network: ", network.num_addresses)

# Print if this network is under (or overlaps) 192.168.0.0/16
print("Overlaps 192.168.0.0/16: ", network.overlaps(ipaddress.IPv4Network("192.168.0.0/16")))

# Print the supernet of this network
print("Supernet: ", network.supernet(prefixlen_diff=1))

# Print if the network is subnet of 192.168.0.0/16.
print("The network is subnet of 192.168.0.0/16: ",
	network.subnet_of(ipaddress.IPv4Network("192.168.0.0/16")))

# Print if the network is supernet of 192.168.0.0/16.
print("The network is supernet of 192.168.0.0/16: ",
	network.supernet_of(ipaddress.IPv4Network("192.168.0.0/16")))

# Compare the ip network with 192.168.0.0/16.
print("Compare the network with 192.168.0.0/16: ",
	network.compare_networks(ipaddress.IPv4Network("192.168.0.0/16")))
```

### Demo Code

The demo code below introduces concepts necessary to complete the challenge.

```python

#!/usr/bin/env python3

import ipaddress
from scapy.all import ICMP, IP, sr1, TCP

# Define end host and TCP port range. Take care not to populate the host bits here.
network = "10.0.2.0/24"
ip_list = ipaddress.IPv4Network(network).hosts()
hosts_count = 0

for host in ip_list:
    print("Pinging", str(host), "- please wait...")
    response = sr1(
        IP(dst=str(host))/ICMP(),
        timeout=2,
        verbose=0
    )

print(response)
```
