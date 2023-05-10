# Lecture Notes: Cloud Identity and Access Management (IAM) with AWS

## IAM

- **Why**
  The 2019 Capital One data breach sets the stage for today's discussion on IAM.

  > "On July 29, 2019, the FBI arrested Paige A. Thompson (also known by the alias “erratic”) for allegedly hacking into Capital One databases and stealing the data. CapitalOne disclosed the estimated the data loss at approximately 1 million Social Insurance Numbers of Canadian credit card customers, about 140,000 Social Security numbers and 80,000 linked bank account numbers of the credit card customers" -Cloudneeti

  The root cause of the vulnerability was misconfigured profiles (IAM).

- Why do we need to study cloud IAM controls in cybersecurity?

- **What** (10 min)
  - What is IAM? According to [ISC2](https://cisspdomain.com/#domain5):
    - 5.1 Control physical and logical access to assets
      - Information
      - Systems
      - Devices
      - Facilities
    - 5.2 Manage identification and authentication of people, devices, and services
      - Identity management implementation
      - Single/multi-factor authentication
      - Accountability
      - Session management
      - Registration and proofing of identity
      - Federated Identity Management (FIM)
      - Credential management systems
    - 5.3 Integrate identity as a third-party service
      - On-premise
      - Cloud
      - Federated
    - 5.4 Implement and manage authorization mechanisms
      - Role Based Access Control (RBAC)
      - Rule-based access control
      - Mandatory Access Control (MAC)
      - Discretionary Access Control (DAC)
      - Attribute Based Access Control (ABAC)
    - 5.5 Manage the identity and access provisioning lifecycle
      - User access review
      - System account access review
      - Provisioning and deprovisioning
  - What IAM concepts are unique to AWS IAM?
    - Principals
      - Specifies the user, account, service, or other entity that is allowed or denied access to a resource
    - Root Users
      - Root users in AWS can perform all actions
    - IAM Users
      - Users can belong to multiple user groups
    - IAM Groups
      - A collection of IAM users
      - Contain many users
      - Can't be nested (no groups inside groups)
    - IAM Roles
      - Similar to users but instead of being associated with one person, a role is intended to be assumed by anyone who needs it
      - Does not have standard long-term credentials (passwords or access keys)
      - When you assume a role, it gives you temporary security credentials for your role session
    - AWS Security Token Services (STS)
    - Roles for cross-account access
      - A role that grants access to resources in one account to a trusted principal in a different account
    - AWS service role for EC2
      - Special type of service role that an application running on an EC2 instance can assume to perform actions in your account
    - Policy documents
    - Identity-based policies
      - Inline Policy
      - Customer-Managed Policy
      - AWS-Managed Policy
    - S3 Policies
      - ACL
      - Bucket

- **How** (30 min)
- How is proper IAM implemented?
  - Integrate security principles into existing management of users
  - Know your NIST!
    - NIST documents can be long, dry, and feel overbearing to use in a practical/efficient way.
    - Use NIST as a guideline or checklist on how to define your policies
    - Government organizations may impose NIST as a requirement
    - NIST SP800-63B

Ref. [DEMO.md](DEMO.md)

# Lecture Notes: Read a file line by line in Python

**Method 1: Read a File Line by Line using readlines()**

`readlines()` is used to read all the lines at a single go and then return them as each line a string element in a list. This can be used for small files since it reads the whole file content to the memory and the split it into separate lines. We can then iterate over the list and strip the newline '\n' character using `strip()` function

**Example:**

```python
# Python code to demonstrate readlines()

L = ["Geeks\n", "for\n", "Geeks\n"]

# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()

# Using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
	count += 1
	print("Line{}: {}".format(count, line.strip()))
```

**Method 2: Read a File Line by Line using readline()**

`readline()` function reads a line of the file and returns it in the form of the string. It takes parameter `n`, which specifies the max number of bytes that will be read. It will not read more than one line, even if `n` is more than the length of the line. Returns the next line of the file which contains a newline character in the end.

**Example**

```python
# Python program to demonstrate readline()

L = ["Geeks\n", "for\n", "Geeks\n"]

# Writing to a file
file1 = open('myfile.txt', 'w')
file1.writelines((L))
file1.close()

# Using readline()
file1 = open('myfile.txt', 'r')
count = 0

while True:
	count += 1

	# Get next line from file
	line = file1.readline()

	# if line is empty end of file is reached
	if not line:
		break
	print("Line{}: {}".format(count, line.strip()))

file1.close()
```

**Method 3: Read a File line by line using for loop**

This final way of reading a file line-by-line includes iterating over a file object in for a loop. This takes advantage of a built-in Python function that allows us to iterate over the file object implicitly using a for loop in a combination with using the iterable object.

`strip()` is an built-in function that returns a copy of the string with both leading and trailing characters removed

**Example**

```python
# Python program to demonstrate reading files using for loop

L = ["Geeks\n", "for\n", "Geeks\n"]

# Writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()

# Opening file
file1 = open('myfile.txt', 'r')
count = 0

# Using for loop
print("Using for loop")
for line in file1:
	count += 1
	print("Line{}: {}".format(count, line.strip()))

# Closing files
file1.close()
```
