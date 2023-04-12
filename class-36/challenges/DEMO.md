# Ops Challenge - Web Application Fingerprinting 

## Demo Code

Computers love to talk. We can use this to our advantage anytime we're testing web servers for vulnerabilities.

We can use `Netcat` to perform banner grabbing from a Kali Linux box using `nc IP PORT` to see if there's a response. Here's this in action.

```bash
kali@kali:~$ nc scanme.nmap.org 22
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13 ###BANNER
```

Alternatively, we can use Telnet to perform similar banner grabbing with the syntax `telnet IP PORT` as depicted below.

```bash
kali@kali:~$ telnet 10.0.2.24 22
Trying 10.0.2.24...
Connected to 10.0.2.24.
Escape character is '^]'.
SSH-2.0-OpenSSH_5.3p1 Debian-3ubuntu4  ###BANNER
^
Protocol mismatch.
Connection closed by foreign host.

```

If you scout around the internet you'll quickly see there are many ways to perform banner grabbing.
