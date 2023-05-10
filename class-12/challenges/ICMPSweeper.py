# ----- ICMP Ping Sweep tool -----
from scapy.all import ICMP, IP, sr1, TCP
import ipaddress
# Python's ipaddress module which provides the ability to create, manipulate and operate on IPv4 and IPv6 addresses and networks. This is included with Python 3.3+, so you do not need to install it.

# Declare Variables
ip = "127.0.0.1"
myIp = "10.0.0.68"
host = "scanme.nmap.org"
network = '10.0.0.1/24'

# ----- Initialize an IPv4Address! -----
# ip4 = ipaddress.IPv4Address(ip)
# print(ip4.is_multicast)
  # Print True if the IP address is a loopback address.
# print("Is loopback: ", ip4.is_loopback)

# ----- Initialize an IPv4Network() -----
ip4Network = ipaddress.IPv4Network("192.168.1.0/24")
# Print the network address of the network.
print("Network address of the network: ", ip4Network.network_address)

  # Print the broadcast address
print("Broadcast address: ", ip4Network.broadcast_address)

  # Print the network mask.
print("Network mask: ", ip4Network.netmask)


response = sr1(IP(dst=host)/ICMP(), timeout=1, verbose=0)

# If the response is empty, then the host is down
if response is None:
  print("Host down")
# Check for ICMP codes
  if response.haslayer(ICMP):
    response.getlayer(ICMP).code # now compare the reutnred code to 1, 2, 3, 9, 10, or 13.
      # Then the host is actively blocking ICMP traffic.
      # How do you cast to Integer in Python? String ->(cast) Integer "2" X 2 => int("2")
# if no codes and reponse is good, host is up and responding! sebnd a RST(reset)
