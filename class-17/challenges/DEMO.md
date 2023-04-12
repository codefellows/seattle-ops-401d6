# Ops Challenge - Automated Brute Force Wordlist Attack Tool Part 2 of 3

## Demo Code

The demo code below introduces concepts necessary to complete the challenge.

```python
# Sample SSH authentication script
import time
import paramiko
import getpass

# Get input from user
host = input("Please provide an IP address to connect to:")
user = input("Please provide a username:")
password = getpass.getpass(prompt="Please provide a password:")
port = 22

# Create object of SSHCLient and connect to SSH
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
  ssh.connect(host, port, user, password)
  stdin, stdout, stderr = ssh.exec_command("whoami")
  time.sleep(3)
  output = stdout.read()
  print(output)
  stdin, stdout, stderr = ssh.exec_command("ls -l")
  time.sleep(3)
  output = stdout.read()
  print(output)
  stdin, stdout, stderr = ssh.exec_command("uptime")
  time.sleep(3)
  output = stdout.read()
  print(output)

except paramiko.AuthenticationException as e:
  print("Authentication Failed!")
  print(e)

ssh.close()

```
