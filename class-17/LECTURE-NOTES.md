# Lecture Notes: Cloud Network Security

## Cloud Network Security

- **Why** (5 min)
  - Why would we use traditional network infrastructure in the cloud?
  - Why use a VPC when you have elastic IPs?

- **What** (10 min)
  - What network security components should we learn how to use on the cloud?
    - Security Groups
    - VPC
      - Private subnet
      - Public subnet
    - Internet gateway
    - NAT gateway
  - An **Amazon Virtual Private Cloud (Amazon VPC)** enables you to launch AWS resources into a virtual network that you've defined
    - Resembles a traditional LAN except with access to scalability of AWS
  - A **subnet** is a range of IP addresses in your VPC, much like a traditional LAN subnet.
    - Must fit within the scope of your VPC
      - Example: 192.168.0.0/16 as as VPC would support a 192.168.1.0/24 subnet.
    - A **public subnet** hosts public-facing services like a web site or file server.
      - An **internet gateway** is a gateway that you attach to your VPC to enable communication between resources in your VPC and the internet.
    - A **private subnet** does not allow access to resources from outside the VPC, and is instead meant for internal resources.
      - You can use a **network address translation (NAT) gateway** to enable instances in a private subnet to connect to the internet or other AWS services, but prevent the internet from initiating a connection with those instances.
      - NAT gateways will charge you.
      - A **route table** is a set of rules, called routes, that are used to determine where network traffic is directed.
  - **CIDR (Classless Inter-Domain Routing) Block** is an internet protocol address allocation and route aggregation methodology. AWS recommends referencing the CIDR article on Wikipedia.

- **How** (30 min)
  - Ref. [DEMO.md](DEMO.md)

# Lecture Notes: Paramiko

Paramiko is a Python library that makes a connection with a remote device through SSH. Paramiko uses SSH2 and supports the SFTP client and server model

**Installing Paramiko**

To install paramiko run the following commands. Paramiko needs cryptography as a dependency

```bash
pip install paramiko
pip install cryptography
```

Once installed, you can connect to a remote SSH server using paramiko

```python
import paramiko

# Create object of SSHCLient and connecting to SSH
ssh = paramiko.SSHClient()

# Adding new host key to the local HostKeys object(in case of missing) AutoAddPolicy for missing host key to be set before connection setup
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('1.1.1.2`, port=22, username='UserName', password='PassWord', timeout=3)

# Execute command on SSH terminal using exec_command
stdin, stdout, stderr = ssh.exec_command('show ip interface brief')
```

**Example: Printing the username**

```python
import paramiko
output_file = 'paramiko.org'


def paramiko_GKG(hostname, command):
 print('running')
 try:
  port = '22'

  # created client using paramiko
  client = paramiko.SSHClient()

  # here we are loading the system host keys
  client.load_system_host_keys()

  # connecting paramiko using host name and password
  client.connect(hostname, port=22, username='geeksForgeeks',
     password='geeksForgeeks')

  # below line command will actually execute in your remote machine
  (stdin, stdout, stderr) = client.exec_command(command)

  # redirecting all the output in cmd_output variable
  cmd_output = stdout.read()
  print('log printing: ', command, cmd_output)

  # we are creating file which will read our cmd_output and write it in output_file
  with open(output_file, "w+") as file:
   file.write(str(cmd_output))

  # we are returning the output
  return output_file
 finally:
  client.close()


paramiko_GKG('10.10.10.1', 'uname')
```
