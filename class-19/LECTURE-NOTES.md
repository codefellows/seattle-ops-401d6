# Lecture Notes: Cloud Detective Controls

## Amazon GuardDuty

- **Why** (5 min)
  - Why should we learn how to use Amazon GuardDuty?
    - Helps us detect threats in our cloud environment
    - Example: "For enhanced security, National Australia Bank deployed Amazon GuardDuty, a fully managed intelligent threat detection service that continuously monitors account activity for malicious or unauthorized behavior, to help protect all of its AWS workloads and safeguard customers’ data in the cloud." -Source: [Businesswire](https://www.businesswire.com/news/home/20181129005084/en/National-Australia-Bank-Selects-AWS-as-its-Long-Term-Strategic-Cloud-Provider)

- **What** (10 min)
  - What is event-driven architecture?
    - **Event-Driven Architecture** consist of decoupled systems that run in response to events.
    - Events trigger and communicate between separate services
    - Modern applications
    - Microservices
    - Three key components:
      - Event producers
      - Event routers
      - Event consumers

  - What is AWS Lambda?
    - **AWS Lambda** is a compute service that runs code without the need for provisioning or managing servers (serverless)
    - Code is executed on cloud compute infrastructure (no instances necessary)
    - Run Lambda functions in response to events
      - Example, state changes in a S3 bucket
      - Respond to security concerns automatically
      - Alternatively, developers can build serverless applications with Lambda

  - What is the canary in the coal mine all about?
    - Origins of “Canary in the coal mine”
    - From 1911 to 1986, coal miners brought caged canaries (birds) into coal mines to detect toxic gases
    - Upon detection, canary screeched (or died) and warned miners of danger
    - Why a canary?
      - A “sentinel species” more sensitive to carbon monoxide and toxic gas
    - Later replaced with electronic sensor tools
    - Boils down to be configurable scripts to continuously monitor your application endpoints and APIs

  - What is Amazon GuardDuty?
    - **Amazon GuardDuty** analyzes selected logs using machine learning models and threat intelligence to produce observable records of suspicious activities, referred to as "findings."
    - Log sources
      - AmazonVPC Flow Logs
      - AWS CloudTrail
      - DNS queries
    - Automatically gathers info from these services without configuration, such as creating a trail in CloudTrail
    - Components
      - A **detector** consumes information and generates findings within a specific AWS account and region.
      - Findings
        - Archivable using suppression rules
  - Where GuardDuty sends events

- **How** (30 min)
  - How Amazon GuardDuty protects the environment utilizing:
    - Amazon VPC Flow logs
    - AWS CloudTrail
    - DNS requests
  - How to manage GuardDuty findings
  - Ref. [DEMO.md](DEMO.md)
