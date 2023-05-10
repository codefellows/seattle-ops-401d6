# Lecture Notes: Logging and Monitoring

## Logging and Monitoring

**Why**
- Why use AWS CloudTrail and Amazon CloudWatch?
  - Monitor your cloud resources
  - Automate cloud threat detection and response
  - Acts as a cloud SIEM to aggregate event logs and ensure their integrity

**What**
- What is AWS CloudTrail?
  - **AWS CloudTrail** is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account.
  - Each CloudTrail log includes the following parameters:
    - The service
    - The name of API action performed
    - Region resource located in
    - Response elements
    - Principal that made the request
    - Date and time of the request
    - IP address of the requester

  - Maintains event history of account activity, including CLI
  - Important part of AWS cloud threat detection
  - Pricing
    - "You can view, filter, and download the most recent 90 days of your account activity for all management events in supported AWS services free of charge."
  - What types of events are handled by AWS CloudTrail?
    - CloudTrail event classification:
      - API vs Non-API
      - Management vs Data Events

    |Event type |Enabled  |Type |Console |API
    --- | --- | --- | --- | ---
    |Management|By default|API Activity, service events, sign-in events|data4|data5
    |data11|data12|data13|data14|data15

  - Log file integrity validation
    - Optional CloudTrail feature that uses hash validation to ensure log integrity

- What is AWS CloudWatch?
  - "**Amazon CloudWatch** is a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), and IT managers." Key functions include:
    - Infrastructure monitoring and troubleshooting
    - Resource optimization
    - Application monitoring
    - Log analytics
  - "Amazon CloudWatch enables you to set alarms and automate actions based on either predefined thresholds, or on machine learning algorithms that identify anomalous behavior in your metrics"
  - Key components of CloudWatch include:
    - Alarms
    - Dashboards
    - Logs
      - **CloudWatch Logs** is a log aggregation service that supports ingestion of both AWS and non-AWS sources
      - Example supported logs:
        - Route 53 DNS query logs
        - VPC flow logs
        - CloudTrail logs
      - Logs from the same source are organized into a single log stream
      - Retention can be as short as 1 day or as long as 10 years
      - Archivable to S3 bucket
    - Metric filters
    - Events
- What is Amazon EventBridge?
  - A serverless, fully managed, and scalable event bus that enables integrations between AWS services, SaaS and your applications.
  - EventBridge was formerly called CloudWatch Events, they are the same underlying service and API.
- What are VPC flow logs?
  - **VPC Flow Logs** is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC. Flow log data can be published to Amazon CloudWatch Logs or Amazon S3. After you've created a flow log, you can retrieve and view its data in the chosen destination."

**How**
- How do these cloud security systems work together?
  - Ref. [DEMO.md](DEMO.md)


# Lecture Notes: Zipfile Python module

The zipfile module allows us to work on zip files

**Example: Extracting a zip file**

This script extracts a zip file named "my_python_files.zip" in the same directory as of this python script

```python
# Imports the required modules
from zipfile import ZipFile

# specifying the zip file name
file_name = "my_python_files.zip"

# Opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
  # Printing all the contents of the zip file
  zip.printdir()

  # Extracting all the files
  print('Extracting all the files now...')
  zip.extractall()
  print('Done!')

  # the extract() method extracts a specific file
  # example: zip.extract('python_files/python_wiki.txt')
```
