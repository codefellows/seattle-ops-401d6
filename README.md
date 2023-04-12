# Ops 401: Cybersecurity Engineering

## Course Information

- Course Level: Ops 401

## Course Prerequisites

- Ops 101
- Ops 102
- Ops 201
- Ops 301

> Students with previous relevant or equivalent experience can test out of this requirement in their application.

## Course Description

Ready to kickstart your exciting career in cyber security operations (SecOps)? In this intensive course, delve into critical topics like cyber frameworks, data encryption, cloud security, network security, threat modeling, shell scripting, vulnerability scanning, and incident response. Gain valuable ethical hacker skills in penetration testing, and show off your awesome new abilities in two resume-enhancing projects!

Designed to prepare you for today’s most in-demand security skills, this hands-on course emphasizes practical SecOps. Students will gain cutting-edge skills by analyzing systems vulnerabilities, implementing defenses against common threats, and using industry-relevant tooling.

## Certification

This course will substantially prepare you for achieving the learning objectives of CompTIA Security+ certification. This course covers significant aspects of all six domains required for Security+.

- 1.0 Threats, Attacks, and Vulnerabilities
- 2.0 Technologies and Tools
- 3.0 Architecture and Design
- 4.0 Identity and Access Management
- 5.0 Risk management
- 6.0 Cryptography and PKI

> Students register for the CompTIA Security+ SY0-601 during course prework, and take the exam during the final module. The student’s resulting score from taking CompTIA Security+ SY0-601 is then factored into the final grade for this course. Passing this course is largely contingent upon passing CompTIA Security+ SY0-601.

## Required Materials

### Reading Materials

[Sybex CompTIA Security+ Study Guide](https://www.amazon.com/CompTIA-Security-Study-Guide-SY0-601/dp/1119736250/ref=sr_1_3?dchild=1&keywords=sybex+security%2B&qid=1626223418&sr=8-3) (includes access to online practice exams)

### Personal Computer/Laptop

By the start of the first class, you need a working computer meeting the school-specified requirements.

### Ops Lab Kit

Ops courses require a second computer for lab. By the start of the first class, you will need to have obtained an Ops Lab Kit as directed by your school.

### Internet Connection

Each student is responsible for their access to the internet for purposes of this course and for research. Internet access is a required component of this course and will not be accepted as an excuse for missed work. If you know that you will be traveling, then make sure you plan accordingly.

### Applications

- [Zoom Video Conferencing Software](https://zoom.us)
- The latest version of [Google Chrome](https://www.google.com/chrome/browser/desktop/)
- [Visual Studio Code](https://code.visualstudio.com/)


## Program Learning Outcomes

At the end of this course, you will be prepared for a career in Cyber Security

## Student Learning Outcomes

Upon satisfactory completion of this course, a student should be able to:

### Describe and Define

#### Governance, Risk, and Compliance (GRC)

- Cybersecurity frameworks (e.g. SOC2)
- CIA triad
- Systems hardening
- Risk analysis, assessment, and reporting
- Security compliance and auditing

#### Data Security

- Data classification
- Data loss prevention (DLP)
- Data privacy concepts and regulation (GDPR, CCPA)
- Encryption standards
- Password security
- Protecting data at rest and in transit
- Public Key Infrastructure (PKI)
- SSL/TLS

#### SecOps Foundations

- Threat detection with IDS, SIEM
- Incident response lifecycle
- Indicators of compromise (IOC)
- SIEM deployment and operation
- SIEM log and event analysis
- SIEM troubleshooting, data ingestion, query writing
- Threat hunting techniques

#### Cloud Security

- Cloud identity and access management
- Cloud security in AWS
- Data loss prevention (DLP)
- Intrusion detection & prevention systems (IDS/IPS, Snort)
- Network traffic analysis
- Virtual private cloud (VPC)
- AWS native tooling (e.g. AWS CloudTrail)

#### Threat Modeling and Analysis

- Tactics, techniques, and procedures (TTPs)
- Cyber Kill-Chain
- MITRE ATT&CK
- OWASP
- STRIDE
- Threat Modeling
- Data flow diagrams

#### SecOps: Threat Hunting

- Malware detection with YARA rules, VirusTotal API
- Malware traffic analysis
- Forensic investigation
- Threat hunting with Zeek, RITA

#### AppSec and Vulnerability Analysis

- Web app scanning and exploitation with Burp Suite, w3af, OWASP ZAP
- CVE, CVSS
- Vulnerability scanning tools, e.g. Nessus
- Network and application vulnerability scans and assessments
- Scanner output handling, false positives, prioritization
- Vulnerability risk rating
- Vulnerability types and concepts

#### Penetration Testing

- Enumeration
- Exploitation
- Impact analysis
- Investigation and intelligence collection
- Legal considerations in pentest scoping
- Nmap, metasploit, datasploit
- OSINT
- Penetration test lifecycle
- Planning
- Scoping
- Target profiling and evaluation

### Execute

- Assess risk using quantitative or qualitative methods
- Document risk mitigations and perform security compliance audits
- Take a security project all the way from conceptual requirements to technical implementation
- Apply modern cryptographic principles to protect data at rest and in transit
- Use data loss prevention (DLP) tools
- Perform threat analysis and threat modeling using various tools such as STRIDE, cyber kill-chain, and MITRE ATT&CK
- Explore web application security
- Administer anti-malware systems and various security tools
- Analyze IT systems security with vulnerability scanning
- Perform penetration testing
- Configure an intrusion detection/prevention system (IDS/IPS)
- Performing incident response operations and SIEM event monitoring
- Deploy configure, and query a SIEM
- Oversee cloud security efforts using AWS native tooling

## Resources / Downloads

All required downloads of large files will be listed within the class schedule (below) to help you prepare for each class lab activity. It is your responsibility to:

- Maintain a reliable high speed internet connection.
- Maintain adequate hard drive space on your lab kit PC.
- Download the required files in a timely fashion, preferably well in advance of the class you'll be using it.

If you encounter issues downloading the required files for a class, troubleshoot the issue with your instructor outside of lecture. Your instructor will be responsible for maintaining working download links.

To avoid lengthy software installation and setup times, many of the required virtual machines used in this course have been prepared for you in advance. Unlike Ops 301, required infrastructure will commonly be provided to you by way of OVA files, unless the installation and setup of the infrastructure is a part of the learning objectives for the day.

It is generally a good idea to maintain a "core lab" in VirtualBox representing the key elements of a cyber range throughout the course and even past graduation:

- PfSense Router/Firewall
- Windows Server 2019 Domain Controller
- Windows 10 Endpoint (Domained)
- Ubuntu Server 20.10 Web Server
- Ubuntu Server 20.10 GitHub Repository Development Box
- Ubuntu Desktop 20.10 Threat Hunter/IDS Machine
- Kali Linux Attacker Box

Several labs and projects in Ops 401 require an AWS account and free tier hours to avoid incurring charges. It will be your responsibility to maintain and shut down cloud machines in a timely fashion to avoid incurring charges on AWS. Note that creating instances in EC2 involves the use of AMIs (Amazon Machine Images) and not OVAs.

Files customized for this course are intended for students and should not be shared/distributed beyond this class.

## Course Schedule

This course is composed of 8 modules, each module with its own theme and 2 projects....

Please refer to the downloads table at the bottom of this document to find the downloadable resources you will need for each lab.

### Module 1 Governance, Risk, and Compliance (GRC)

| Class # | Topic | Lab |
|-----------------|-----------|----------|
| 01 | Strategic Policy Development | Scenario: Policy Development + Automated Compliance |
| 02 | Cloud Security Principles and Frameworks | Scenario: IaaS Provider Recommendation based on SOC2 Compliance |
| 03 | Cyber Risk Analysis | Scenario: Create risk assessment report for client |
| 04 | Systems Hardening with CIS Standards | Deploy and harden a Windows 2019 server to EC2 |
| 05 | Career Coaching Workshop | Resume Review | |

### Module 2 Data Security

| Class # | Topic | Lab |
|-----------------|-----------|----------|
| 06 | Data File Encryption and Hashing | Transfer files securely between computers |
| 07 | Protecting Data at Rest | Full Disc Encryption on Windows and Linux |
| 08 | DLP and Classification | Implement Data Lost Prevention & Data Classification Solution |
| 09 | Public Key Infrastructure (PKI) | Use PKI in Windows and Linux to send and decrypt messages |
| 10 | Career Coaching Workshop | Personal Pitch | |

### Module 3 Security Operations

| Class # | Topic | Lab |
|-----------------|-----------|----------|
| 11 | Foundational SIEM Operations | Deploy and use SIEM Solution (Splunk) |
| 12 | Log Analysis with Splunk | Scenario: Search log data using splunk |
| 13 | Reconstructing a Cloud Attack Using Log Data | Scenario: Use Splunk to trace/re-create an attack |
| 14 | Intrusion Detection and Prevention Systems (IDS/IPS) | Deploy IDS/IPS and trigger rules  |
| 15 | Career Coaching Workshop | Targeted Job Search/Negotiations |  |

### Module 4 Cloud Security

| Class # | Topic | Lab |
|-----------------|-----------|----------|
| 16 | Cloud Identity and Access Management (IAM) with AWS | Configure users & groups via CLI |
| 17 | Cloud Network Security | Manage AWS networking and security |
| 18 | Cloud Logging and Monitoring | Enable logs and triggers in AWS |
| 19 | Cloud Detective Controls | Configure Amazon Guard Duty and logging triggers |
| 20 | Project Prep | Team Building, Planning | |

### Module 5 Midterm Project

### Module 6 Threat Modeling and Analysis

| Class # | Topic | Lab |
|-----------------|-----------|----------|
| 26 | Remote Code Execution | Reproduce attack, fix with RCE Script |
| 27 | Persistence | Keep open shell connection with remote computer |
| 28 | Log Clearing | Reproduce and then mitigate a log clearing attack |
| 29 | Modeling a Web Application | Scenario: Threat modeling and DFD |
| 30 | Career Coaching Workshop | Behavioral Interviews | |

### Module 7 Threat Hunting

| Class # | Topic | Lab |
|-----------------|-----------|----------|
| 31 | Threat Hunting with YARA | Write and test YARA rules |
| 32 | Malware Traffic Analysis with Wireshark | Find malicious attack with Wireshark; Incident Reporting |
| 33 | Threat Hunting with Zeek, RITA | Active Countermeasures Threat Hunting Scenarios |
| 34 | Forensic Investigation with Autopsy  | Post Mortem analysis of hard drive using Autopsy |
| 35 | Career Coaching Workshop | Technical Interviews | |

### Module 8 Web Application Security

| Class # | Topic | Lab |
|-----------------|-----------|----------|
| 36 | XSS with w3af, DVWA | Scan a web app using w3af |
| 37 | Automated AppSec with OWASP ZAP | Use ZAP to crawl and brute force attack a web app |
| 38 | Attacking Juice Shop with Burp Suite | Using Burp Suite to probe an app |
| 39 | SQLi with Burp Suite, Web Goat | Practice SQL Injection through scenarios |
| 40 | Career Coaching Workshop | Personal Presentation | |

### Module 9 Penetration Testing

| Class # | Topic | Lab |
|-----------------|-----------|----------|
| 41 | Reconnaissance with Maltego | Information gathering with Maltego |
| 42 | Pass the Hash with Mimikatz | Practice & Document a "pash the hash" attack |
| 43 | Traffic Sniffing with Ettercap | Implement a man-in-the-middle attack via spoofing |
| 44 | Pentest Practice 1 of 2 | Scenario: Use metasploit to gather information and start attack plan |
| 45 | Pentest Practice 2 of 2 | Scenario: Gather information, report findings |

### Module 10 Final Project

---

## Downloads Table

Files are either hosted externally by the source (for example, kali.org hosts Kali Linux ISO) or hosted by Code Fellows using iCloud (Mirror 1) or Google Drive (Mirror 2). You may be prompted to create a free user account for the corresponding service in order to download the hosted files.

Note that "Mirror 2" is an alternative source for downloading the same file. Use the Mirror 2 download link if the primary download link, Mirror 1, does not work. You do not need to download both the Mirror 1 and Mirror 2 for a given class; they are the same file. If none of the provided download links work, contact your instructor for assistance.

Occasionally an OS installer ISO is listed for the class, which indicates that the listed OS is required for the lab. For ISO files, you do not need to download more than one copy to a local computer. Many of these you likely already have saved locally if you completed previous prerequisite coursework with Code Fellows.

|Class |File |Size |Mirror 1 |Mirror 2 |
--- | --- | --- | --- | ---
|Class 1|SOC 2 Policy Docs |9 KB|[Download](https://docs.google.com/document/d/1-JRjrVBqYnLBNImWuZTR2df3TE3OwSdXneEbglNVhbs/edit?usp=share_link)|---
|Class 2|Cloud Security Policy Template PDF|813 KB|[Download](https://www.icloud.com/iclouddrive/0E1ux7MCK6hvgjOO9NeSAJGYA#Cloud_security_policy_template)|---
|Class 3|CyHy Sample Report_508C.pdf|1.65 MB|[Download](https://www.icloud.com/iclouddrive/0TMsjA7sxPdUxBj1o-rTmwlQQ#CyHy_Sample_Report_508C)|---
||Risk Assessment Worksheet.xlsx|410 KB|[Download](https://www.icloud.com/iclouddrive/0UQGtflOn3XjLgr8cMAMIw7Xw#Risk_Assessment_Worksheet)|---
|Class 5|class-05-cryptor.ova|2.63 GB|[Download](https://www.icloud.com/iclouddrive/0xXGE-M3-SdlP677X9MnaKGxA#class-05-cryptor)|---
||Win10 VM | 5.81 GB | [Download](https://www.icloud.com/iclouddrive/0fj3zpzdfMT-UcK5oIpm8DkaA#win10-v2)|---
||Windows Media Creation Tool|18.5 MB|[Download](https://support.microsoft.com/en-us/windows/create-installation-media-for-windows-99a58364-8c02-206f-aa6f-40c3b507420d)|---
||7-Zip Installer|1414 KB|[Download](https://www.7-zip.org/download.html)|---
|Class 7|Ubuntu Linux Desktop 20.10 ISO|2.7 GB|[Download](https://releases.ubuntu.com/20.10/ubuntu-20.10-desktop-amd64.iso?_ga=2.26182525.1148048504.1617140559-1691518363.1609958218)|---
|Class 8|FileZilla FTP Client Installer|13.5 MB|[Download](https://filezilla-project.org/download.php?type=client)|---
|| Win10 VM | 5.81 GB | [Download](https://www.icloud.com/iclouddrive/0fj3zpzdfMT-UcK5oIpm8DkaA#win10-v2)---
|Class 9|Gpg4win 3.1.13 Installer|13.5 MB|[Download](https://www.gpg4win.org)|---
|| Win10 VM | 5.81 GB | [Download](https://www.icloud.com/iclouddrive/0fj3zpzdfMT-UcK5oIpm8DkaA#win10-v2)---
|Class 10|class-10-target.ova|855 MB|[Download](https://www.icloud.com/iclouddrive/0HtOSiZI0qtq2_GDxHskf7E3g#class-10-target)|---
||ADHD4-sha1.ova|6.0 GB|[Download](https://adhdhost.s3.amazonaws.com/ADHD4/ADHD4-sha1.ova)|---
|Class 11-13|Class-11-13-SIEM.ova|2 GB|[Download](https://www.icloud.com/iclouddrive/042H2RmH3jpw3xWG41SzAgPdA#Class-11-13-SIEM)|---
|Class 14|Class-14-hunter3.ova|4 GB|[Download](https://www.icloud.com/iclouddrive/0LtGXX4-NEN8RC8r-YWYw5SRQ#class-14-hunter3)|---
|Class 15|Metasploitable 1|545 MB|[Download](https://download.vulnhub.com/metasploitable/Metasploitable.zip)|---
|Class 26|term2-baseline-lab-v4.zip (Contains winserv2019-dc1, pfsense-corpnet, siem.ova): Grab this bundle, or each OVA individually from below |25 GB|[Download](https://www.icloud.com/iclouddrive/0f5g1RsLEL_6xvqwhqJd5PL7A#term2-baseline-lab-v4)|[Download](https://drive.google.com/file/d/1_-2c_ExUmXNhuSUWZbfXgTt5ynlbibHS/view?usp=sharing)
||README.txt - **Includes login / network config details** |1.37 KB|[Download](https://www.icloud.com/iclouddrive/0HxGxI1n-kPEfNjCvK8EzlPvw#README)|[Download](https://drive.google.com/file/d/1x8dyPjabTQEv8cdxFk8IfnDuFwhlDE8s/view?usp=sharing)
||Kali Linux 64-bit Image (Attacker VM)|4.0 GB|[Download](https://www.kali.org/get-kali/#kali-virtual-machines)|
||win10-v2.ova (Single VM, fresh Win10 image)|5.81 GB|[Download](https://www.icloud.com/iclouddrive/0fj3zpzdfMT-UcK5oIpm8DkaA#win10-v2)|[Download](https://drive.google.com/file/d/1PqmgBpXUDP9dnS4vdVLAMoMt8iDUzxCQ/view?usp=sharing)
||ids.ova (Single VM with Snort)|9.88 GB|[Download](https://www.icloud.com/iclouddrive/0pt8y8UMeYUCvTSA22a3Fd7DA#ids)|[Download](https://drive.google.com/file/d/1sFC66FyKOFCNi6aO_GWJEaz0COAtkX7N/view?usp=sharing)
||winserv2019-dc1.ova (Single VM)|9.36 GB|[Download](https://www.icloud.com/iclouddrive/0k6wTtxJ0SIFpsVbaJokEJG2g#winserv2019-dc1)|[Download](https://drive.google.com/file/d/1TXLsmDNNKOQG9x18GRMKP1Md-6bOiT2J/view?usp=sharing)
||pfsense-corpnet.ova (Single VM)|748 MB|[Download](https://www.icloud.com/iclouddrive/0Mak9rX5eQNrQQ-s0vatjGsqw#pfsense-corpnet)|[Download](https://drive.google.com/file/d/1VPIw4B5W61qtOS183dFs_ncUffgmtDoC/view?usp=sharing)
||siem.ova (Single VM with Splunk)|13.5 GB|[Download](https://www.icloud.com/iclouddrive/0_xrcz8lVpgbiiCbWqYdtrW-g#siem)|[Download](https://drive.google.com/file/d/1kMkerDbFa-YBVNxqHFpTDJeARNZcAuO0/view?usp=sharing)
|Class 29|Microsoft Threat Modeling Tool|16.2 KB|[Download](https://aka.ms/threatmodelingtool)|---
|Class 30|Metasploitable 3|7 GB|[Download](https://www.icloud.com/iclouddrive/062XinnfDVzVPvtxNsh9g2fhw#class-30-metasploitable3)|[Download](https://drive.google.com/file/d/1waaTNsNOISGmaazOLcProRwDuSsTkJIF/view?usp=sharing)
|Class 31|class-31-34-flare-vm-v2.ova|21.3 GB|[Download](https://www.icloud.com/iclouddrive/0wjoDRK8mZgi22DrjlzfdV56g#class-31-34-flare-vm-v2)|[Download](https://drive.google.com/file/d/1xmPRkwhfyDGdQouHKX5YYktBCT7COXAX/view?usp=sharing)
|Class 33|sample-1500.pcap|1.6 GB|[Download](https://github.com/activecm/threat-hunting-labs/releases/download/v1.0/sample-1500.pcap)|---
||sample-500.pcap|832 MB|[Download](https://github.com/activecm/threat-hunting-labs/releases/download/v1.0/sample-500.pcap)|---
||sample-200.pcap|523 MB|[Download](https://github.com/activecm/threat-hunting-labs/releases/download/v1.0/sample-200.pcap)|---
|Class 35|class-35-webserv.ova|491 MB|[Download](https://www.icloud.com/iclouddrive/0fNbdKpA9As6hJG0Ei_yeXUIg#class-35-webserv)|[Download](https://drive.google.com/file/d/1T9aAouWHWK6ya8GKVSj0V2yh4P1hgMwn/view?usp=sharing)
|Class 36|class-36-39-security-dojo.ova|5.82 GB|[Download](https://www.icloud.com/iclouddrive/038L_6Xqfav8PV8Ic_MFe5bYA#class-36-39-security-dojo)|[Download](https://drive.google.com/file/d/1mswI6EpRk8NmJW6QrbG_bOcVM11pqlhU/view?usp=sharing)
|Class 40|Kali Linux 64-bit Image|4 GB|[Download](https://www.kali.org/get-kali/#kali-virtual-machines)|---
||class-40-target.ova|646 MB|[Download](https://www.icloud.com/iclouddrive/0tifOBBxEC_5vLgKobI-_QchA#class-40-target)|---
|Class 42|class-42-target1-win7.ova|7.22 GB|[Download](https://www.icloud.com/iclouddrive/0IEL6LLuw_9G1nLRT2zx0XzUQ#class-42-target1-win7)|---
||class-42-target2-win7 2.ova|6.15 GB|[Download](https://www.icloud.com/iclouddrive/0NlKozf3kX9OyEylAWrNG02cg#class-42-target2-win7_2)|---
|Class 44|class-44-target.ova|855 MB|[Download](https://www.icloud.com/iclouddrive/0cD5O0wXDPYckCNM2Et7fCHhw#class-44-target)|---
|Class 45|class-45-target.ova|7.01 GB|[Download](https://www.icloud.com/iclouddrive/0kCQRwLBykZiwNul-NXLuZgBQ#class-45-target)|---

## Downloads by Module

The following is a more detailed breakdown of required VMs and downloads for each class. If you're wondering "Can I delete the VM from today?" take a look at here to see what's coming up next in terms of required downloads. Links to download mirrors will not be provided here; see the above table for all download mirrors.

### Module 1 Governance, Risk, and Compliance (GRC)

- Class 1
  - SOC 2 Policy Docs Templates by Blissfully.zip
- Class 2
  - Cloud Security Policy Template PDF
- Class 3
  - CyHy Sample Report_508C.pdf
  - Risk Assessment Worksheet.xlsx
- Class 4
  - No downloads
- Class 5
  - A Windows 10 VM is required for this Ops Challenge. This can be installed with any of the below options:
    - Media Creation Tool
    - MSEdge on Win10 (x64) Stable 1809 6.75GB Download
  - 7-Zip Installer 1414KB Download

### Module 2 Data Security

- Class 6
  - No downloads
- Class 7
  - A Windows 10 VM and Ubuntu Linux Desktop VM are required for this lab
- Class 8
  - A Windows 10 VM is required for this lab
  - FileZilla Download
- Class 9
  - A Windows 10 VM is required for this lab
  - Gpg4win 3.1.13 Download
- Class 10
  - A Kali Linux VM is required for this lab

### Module 3 Security Operations 1

- Class 11
  - Class-11-13-splunkserv.ova (10 GB)
- Class 12
  - No downloads, uses the OVA from Class 11
- Class 13
  - No downloads, uses the OVA from Class 11
- Class 14
  - Ubuntu IDS OVA
- Class 15
  - This Ops Challenge requires Kali Linux.
  - Metasploitable 1 OVA

### Module 4 Cloud Security

- Class 16
  - No downloads
- Class 17
  - No downloads
- Class 18
  - No downloads
- Class 19
  - No downloads
- Class 20
  - No downloads

### Module 5 Midterm Project

### Module 6 Threat Modeling and Analysis

- Class 26
  - Term 2 Baseline Lab
- Class 27
  - Term 2 Baseline Lab
- Class 28
  - Term 2 Baseline Lab
- Class 29
  - Microsoft Threat Modeling Tool
- Class 30
  - The following VMs are used in this Ops Challenge:
    - Kali Linux
    - Metasploitable 3
    - Windows 10

### Module 7 Threat Hunting

- Class 31
  - The FLARE VM is required for this lab
- Class 32
  - The FLARE VM is required for this lab
- Class 33
  - This lab will have you analyze some PCAP files from Active Countermeasures. Download these to a VM where you've installed Zeek, RITA, and Wireshark.
    - sample-1500.pcap (1.6 GB)
    - sample-500.pcap (832 MB)
    - sample-200.pcap (523 MB)
- Class 34
  - The FLARE VM is required for this lab
- Class 35
  - class-35-webserv.ova (491 MB)

### Module 8 Web Application Security

- Class 36
  - class-36-39-security-dojo.ova
- Class 37
  - The class-36-39-security-dojo.ova is required for this lab
- Class 38
  - The class-36-39-security-dojo.ova is required for this lab
- Class 39
  - The class-36-39-security-dojo.ova is required for this lab
- Class 40
  - Kali VM
  - class-40-target.ova

### Module 9 Penetration Testing

- Class 41
  - This lab requires a Kali VM.
- Class 42
  - class-42-target1-win7.ova
  - class-42-target2-win7.ova
- Class 43
  - This lab requires a Kali VM and class-42-target2-win7.ova
- Class 44
  - class-44-target.ova
- Class 45
  - class-45-target.ova

### Module 10 Final Project
