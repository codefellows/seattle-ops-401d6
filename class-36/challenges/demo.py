### Ops Challenge 36 ###

# 1. Prompts the user to type a URL or IP address.

# 2. Prompts the user to type a port number.

# 3. Performs banner grabbing using netcat against the target address at the target port; prints the results to the screen then moves on to the step below.

# 4. Performs banner grabbing using telnet against the target address at the target port; prints the results to the screen then moves on to the step below.

# 5. Performs banner grabbing using Nmap against the target address of all well-known ports; prints the results to the screen.

# NOTE: Be sure to only target approved URLs like scanme.nmap.org or web servers you own.


import os, sys, socket, time, telnetlib, signal, subprocess

### DEMO ###
# Creating our own socket connection and passing commands through that socket
def netcat(addr, port):
  #creatting a socket and a connection
  socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  socket1.connect((addr, port))
  print("Netcat...")

  #sneding the netcat command
  command = "nc " + addr + " " + str(port)
  print(command)
  socket1.sendall(command.encode())
  time.sleep(.5)
  socket1.shutdown(socket.SHUT_WR)

  # Repsonse placeholder
  output = ""

  # Convert the data that we received
  while True:
    data = socket1.recv(1024)
    if(not data):
      break
    output += data.decode()

  print(output)
  #close the connection
  socket1.close()

  return ""


def telnet(addr, port):
  return ""


def nmap(addr, port):
  return ""

### MAIN ###

# Collect address and port from user


### DEMO ###
# Passing commands to the command line through os.system
# address = input("What address would you like to Target?")
# command = "nc" + address + " 22"
# os.system(command)
# os.system("/n") # new line of space

netcat("scanme.nmap.org", 22)

