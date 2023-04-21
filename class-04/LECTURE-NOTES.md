# Lecture Notes: Systems Hardening with CIS Standards

## Sec+ Guide Alignment:

- Chapter 11: Endpoint Security
- Chapter 10: Cloud and Virtualization Security

## Lecture: CIS Hardening in the cloud

- **Why** (5 min)
  - Securely configuring your systems is one very important dimension of security risk management. Key benefits to secure configuration:
    - Enhanced system functionality
    - Significantly improved security
    - Simplified compliance and auditability; sometimes required for compliance
  - By default, computer systems "out of the box" tend to prioritize convenience over security, or lack the configuration necessary to make it an effective security defense in your environment until you take the time to configure it.
  - We can use certain industry standards to demonstrate secure configuration.

- **What** (10 min)
  - What is "systems hardening"?
    - Broadly speaking, **systems hardening** is a methodical approach to audit, identify, close, and control potential security vulnerabilities throughout your organization. This can be performed on:
      - Applications
      - Operating systems
      - Servers
      - Databases
      - Networks
  - What is CIS?
    - The **Center for Internet Security (CIS)** is a non-profit org that creates secure configuration benchmarks for computer systems.

  - What are CIS Controls?
    - **CIS Controls** are 20 categories of best practices to improve cyber defenses.
      - Why use CIS Controls?
        - "Leverage the battle-tested expertise of the global IT community to defend against cyber attacks
        - Focus security resources based on proven best practices, not on any one vendor’s solution
        - Organize an effective cybersecurity program according to Implementation Groups"
    - Implementation groups separate the recommended CIS controls by organization size
      - IG1: Small business, no IT staffing
      - IG2: Some IT staffing responsible for protecting infrastructure
      - IG3: Security experts employed

  - What are CIS Benchmarks?
    - **CIS benchmarks** are a set of configuration standards and best practices designed to help organizations ‘harden’ the security of their digital assets (Source: [Cimcor Blog](https://www.cimcor.com/blog/why-cis-benchmarks-are-critical-for-security-and-compliance))
      - "Relate specifically to the configuration of existing assets, excluding security defenses like firewalls and EDRs"
      - "Developed by consensus between experts that include SMEs, security vendors, the CIS benchmarking team, and even the global security community via the CIS Workbench"
      - "While not a regulatory requirement, most prominent compliance frameworks point to CIS benchmarks as the industry standard"
    - CIS benchmarks contain two levels
      - "Level 1 is designed to rapidly minimize the attack surface of an organization without hindering usability or business functionality. These standards can be considered the minimum level of security and compliance that all organizations should aim to meet or exceed."
      - "Level 2 is a more stringent set of standards designed to maximize an organization’s security posture through ‘defense in depth’. These standards are intended for environments where security is essential, and are more costly and labor intensive to implement."
- What is an AMI?
  - An [**Amazon Machine Image (AMI)**](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) provides the information required to launch an instance. It can be roughly compared to how OVA files are used for VirtualBox.
    - An AMI is a special type of virtual appliance that is used to create a virtual machine within EC2
    - AMIs can be customized. "You can launch an instance from an existing AMI, customize the instance (for example, install software on the instance), and then save this updated configuration as a custom AMI. Instances launched from this new custom AMI include the customizations that you made when you created the AMI." -[AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html#creating-an-ami)
    - **AMI Properties**
      - Template for the root volume for the instance
      - Launch permissions that control which AWS accounts can use the AMI to launch instances
      - A block device mapping that specifies the volumes to attach to the instance when it's launched
    - **AMI Characteristics**
      - Regions
      - Permissions for launching AMI
      - OS
      - Root device storage
      - Architecture

- What is AMI hardening and why is it important?
  - **AMI hardening** involves configuring AMIs to prioritize security over mere convenience
- What are prehardened CIS AMIs?
  - These are AMIs that have already been configured to meet CIS standards.

- What is AWS Config?
  - **AWS Config** is a "service that enables you to assess, audit, and evaluate the configurations of your AWS resources." AWS Config needs to be enabled in order to run CIS benchmark assessments in Security Hub.
  - Pricing based on changes recorded

- What is AWS Security Hub?
  - "**AWS Security Hub** provides you with a comprehensive view of your security state in AWS and helps you check your environment against security industry standards and best practices."
  - Free 30-day trial
  - Takes 2 hours to spin up

- **How** (30 min)
  - How can I audit my AWS EC2 instances against CIS benchmarks?
    - Enable AWS Config
    - Enable AWS Security Hub
  - CIS standards are listed by OS
  - Ref. [DEMO.md](DEMO.md)
