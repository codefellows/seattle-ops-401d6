# Lab: Cloud IDS/IPS

## Overview

IDS/IPS systems can also be deployed to the cloud. Today you will deploy Suricata IDS to your AWS VPC.

## Resources

- [AWS VPC Traffic Mirroring Open Source Tools](https://docs.aws.amazon.com/vpc/latest/mirroring/tm-example-open-source.html){:target="_blank"}

## Tasks

### Part 1: Staging Suricata

1. Deploy Suricata IDS to the VPC (ref [AWS VPC Traffic Mirroring Open Source Tools](https://docs.aws.amazon.com/vpc/latest/mirroring/tm-example-open-source.html))
  1. Install the Suricata software on Ubuntu Linux Server
  2. You should already have traffic mirroring enabled. Point Suricata to the interface.

### Part 2: Write Rules

2. Repeat Tuesday's exercise in the Cloud/Suricata context:
  1. Locate the config file
  2. Write and test a rule that detects when ICMP packets transmitted to its IP from internet and raises an alert to the administrator
  3. Locate the log file
  4. Write and test a rule that detects when a RDP attempt is made to its IP from internet and raises an alert to the administrator

### Part 3: Write Enumeration Scan Detection Rules

3. Write rules that detect common types of NMAP scans (ref. [InfosecInstitute](https://resources.infosecinstitute.com/snort-network-recon-techniques/#article))
  1. Write and test a Snort rule to detect aggressive NMAP scanning
  2. Write and test a Snort rule to detect stealth TCP scanning
  3. Write and test a Snort rule to detect decoy scans

## Submission Instructions

1. Create a new blank Google Doc. Include above assignment submission text and images within this Google Doc.
1. Name the document according to your course code and assignment.
   - i.e. `seattle-ops-401d1: Reading 01` or `seattle-ops-401d1: Lab 04`.
1. Add your name & date at the top of the Google Doc.
1. Share your Google Doc so that "Anyone with the link can view".
1. Paste the link to your Google Doc in the discussion field below and share an observation from your experience in this lab.
