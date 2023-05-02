# Utilize the scapy library
from scapy.all import ICMP, IP, sr1, TCP

# Define host IP
host = "scanme.nmap.org"
# Define port range or specific set of ports to scan
port_range = [22, 23, 80, 443, 3389]
# Test each port in the specified range using a for loop
for dst_port in port_range:
  src_port = 1025
  response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port,flags="S"), timeout=1, verbose=0)
  # print(response.summary) # a little info
  # print(response.show()) # A LOT OF INFO
  # If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
  if(response.haslayer(TCP)):
    if(response.getlayer(TCP).flags == 0x12):
      # PORT IS OPEN!!
  # If flag 0x14 received, notify user the port is closed.
  # If no flag is received, notify the user the port is filtered and silently dropped.
