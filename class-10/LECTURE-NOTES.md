# Lecture Notes

## Outline

Today we're introducing incident response, and how sysmon can facilitate improved operations by increasing the quality of Windows event log data.

### Lecture/Demo: Sysmon

- **Why**
  - Why use Sysmon?
    - Greatly improve Windows event logging verbosity and quality of details given
    - Better data source quality means better SIEM usefulness later
    - Ultimately, better defenses

- **What**
  - What is Sysmon?
    - "**System Monitor (Sysmon)** is a Windows system service and device driver that, once installed on a system, remains resident across system reboots to monitor and log system activity to the Windows event log. It provides detailed information about process creations, network connections, and changes to file creation time. By collecting the events it generates using Windows Event Collection or SIEM agents and subsequently analyzing them, you can identify malicious or anomalous activity and understand how intruders and malware operate on your network." -[Microsoft](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)
  - What is an IT security incident?
    - Computer system intrusion
    - Unauthorized systems access
    - Unauthorized systems change
    - Loss or theft of equipment
    - DDoS/DoS attack
    - IT resource misuse
    - User account compromise
  - What is security incident management?
    - The ISO/IEC Standard 27035 outlines a five-step process for **security incident management**, including:
      1. Prepare for handling incidents.
      1. Identify potential security incidents through monitoring and report all incidents.
      1. Assess identified incidents to determine the appropriate next steps for mitigating the risk.
      1. Respond to the incident by containing, investigating, and resolving it (based on outcome of step 3).
      1. Learn and document key takeaways from every incident.
  - What is a security incident report?
    - Documents information about a security incident and how the defenders responded

- **How**
  - How does Sysmon work?
    - Installed via Windows command line
    - Runs in background as service
