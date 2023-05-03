# Import libraries
import random
from scapy.all import ICMP, IP, sr1, sr, TCP
import sys
from ipaddress import IPv4Network


# Variables
menu = ("TCP Port Range Scanner", "ICMP Ping Sweeper", "Exit")

# This function generates a menu for our user to interact with.
# It takes user inputs and validate it as an available option then calls the function or return to menu selection if user choice is invalid.
def display_menu():
    for option in range(0,len(menu)):
        print(str(option+1)+". "+menu[option])

    user_choice = input("Please input the number of the option you'd like: ")


    if user_choice == (len(menu)):
        sys.exit()

    elif user_choice == ("1"):
        tcpscan()

    elif user_choice == ("2"):
        ping_sweep()

    else:
        input("Wrong choice, hit any key to start over.")
        display_menu()

# TCP scan function
def tcpscan():
    host = input("Enter IP Address to scan: ")
    port_range = [22, 23, 80, 443, 3389]
    # Sends SYN with random source port for each destination port
    for dst_port in port_range:
        src_port = random.randint(1025,65534)
        resp = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='S'),timeout=1,verbose=0)

        # Port filtered response if no flag received
        if resp is None:
            print(f"{host}:{dst_port} is filtered (silently dropped).")

        elif (resp.haslayer(TCP)):
            # Port open notification for 0x12 flag
            if (resp.getlayer(TCP).flags == 0x12):
                # Send a RST to close the connection
                send_rst = sr(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),timeout=1,verbose=0)
                print(f"{host}:{dst_port} is closed.")

            # Port closed notification for 0x14 flag
            elif (resp.getlayer(TCP).flags == 0x14):
                print(f"{host}:{dst_port} is closed.")

        elif (resp.haslayer(ICMP)):
            # Port filtered response for no flag received
            if (
                int(resp.getlayer(ICMP).type) == 3 and
                int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
            ):
                print(f"{host}:{dst_port} is filtered (silently dropped). ")

# Ping sweep function
# This function gets a CIDR block address from the user then it pings each host and responds based on the challenge requirements
# It then counts how many hosts are online using an incrementing variable to do so.
def ping_sweep():

    # user input for IPv4 CIDR block
    network = input("Please enter the CIDR block for the IPv4 network you want to scan: ")

    # Variables for creating a list of addresses from the chosen network and setting a live host counter
    addresses = IPv4Network(network)
    live_count = 0

    # Send ICMP ping request, wait for reply
    for host in addresses:
        if (host in (addresses.network_address, addresses.broadcast_address)):
            # Skip these two addresses
            continue

        resp = sr1(IP(dst=str(host))/ICMP(),timeout=1,verbose=0)

        if resp is None:
            print(f"{host} is down or not responding. ")

        elif (
            int(resp.getlayer(ICMP).type) == 3 and
            int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
        ):
            print(f"{host} is blocking ICMP traffic.")
        else:
            print(f"{host} is responding.")
            live_count += 1

    print(f"{live_count}/{addresses.num_addresses} hosts are online. ")


# Main

display_menu()


# End
