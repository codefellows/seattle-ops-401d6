# Lecture Notes: DLP and Classification

## Lecture 1 of 3: Data Loss Prevention (DLP)

- **Why** (5 min)

- Why use DLP?
  - PII/compliance requirements
  - Protecting intellectual property
  - Data visibility/monitoring

- **What** (10 min)

- What is DLP?
  - Data loss prevention is a data security control designed to monitor and control the movement of data by classification type
  - Differentiate
    - Program (policy)
    - Product (tool)

- What are the different types of DLP?
  - Endpoint
  - Network
    - Edge system (E.G. firewall)
  - Cloud
    - E.G O365 DLP

- What types of detection scenarios occur for systems like DLP and antivirus?
  - True positive
  - False positive
  - True negative
  - False negative

- What is driving the adoption of DLP systems?
  - Growth of CISO role
  - Compliance
  - Complexity of technologies/mobile devices
  - Data breaches
  - Stolen data sold on dark web

- What are some DLP best practices?
  - Figure out your objective for using DLP
  - Work with the C-level
  - Define roles and responsibilities
    - Data Owner - E.G. the administrator/CEO/board/president of a company
    - Data custodian - Professionals taking care of the actual data - like IT staff (generally) or HR staff (for HR-related data)
    - System owner - The individual that is in charge of one or more systems, which may contain and operate data owned by various data owners.


### Lecture 2 of 3: Data Classification

- **Why** (5 min)
- Why classify data?
  - Compliance such as GDPR
  - Manageability of systems and data
  - Improve security posture of organization
  - "Spring cleaning"

- **What** (10 min)
- What is data classification?
  - Process of organizing data by relevant categories so that it may be used and protected more efficiently.
  - [Standards for classification](https://digitalguardian.com/blog/what-data-classification-data-classification-definition)
    - Context-based data classification:
      - Content-based classification inspects and interprets files looking for sensitive information
      - Context-based classification looks at application, location, or creator among other variables as indirect indicators of sensitive information
    - User-based data classification:
      - User-based classification depends on a manual, end-user selection of each document.
      - User-based classification relies on user knowledge and discretion at creation, edit, review, or dissemination to flag sensitive documents.

  - **Data Roles and Responsibilities**
    - Data owner: Ultimately responsible
    - Data steward: responsible for data quality and oversight
    - Data custodian: information systems management
    - Data privacy officer: oversees PII assets

  - **Data Classifications**
    - Public (unclassified)
    - Confidential (secret)
    - Critical (Top-Secret)
    - Proprietary
      - Owned information of commercial value
    - Private/Personal Data
      - PII
    - Sensitive
      - Personal data such as beliefs, ethnic origin, or sexual orientation

  - **Privacy Notices and Data Retention**
    - Legislation and regulations
      - GDPR (General Data Protection Regulation)
        - Law made by the European Union that governs how personally identifiable information is collected, processed, and eventually deleted from a computer system
        - It is a regulation that requires businesses to protect their personal data
        - Personal data is defined broadly in GDPR:
          - Basic identity information (name, address, and ID numbers)
          - Health and genetic data
          - Biometric data
          - Racial data
          - Political opinions
      - Rights of data subjects
    - Privacy Notices
    - Impact Assessments
    - Data retention

  - **Data Sharing and Privacy Terms of Agreement**
    - Service Level Agreement (SLA)
    - Interconnection Security Agreement (ISA)
    - Non-disclosure Agreement (NDA)
    - Data Sharing and use agreement

- **How** (30 min)
- How to implement data classification?
  - Evaluate current data handling
  - Create a data classification policy
  - Prioritize and organize data


# Lecture: Ops Challenge 8

## PyAutoGUI

**PyAutoGUI** is a Python module which can automate your GUI and programmatically control your keyboard and mouse. PyAutoGUI does not come with python, so first you have to install it: `pip install PyAutoGUI`

`alert()`: Displays a simple message box with text and a single OK button. Returns the text of the button clicked on.

```python
import pyautogui

# Will display the alert box with the given text and when clicked OK it will return 'OK'
pyautogui.alert('Alert Box')
```

`confirm()`: Displays a message box with OK and Cancel buttons. Number and text of buttons can be customized. Returns the text of the button clicked on.

```python
import pyautogui

pyautogui.confirm('Do you want to continue?')
```

**To have multiple select options**

```python
# Python program to show confirm() function with multiple options
import pyautogui

pyautogui.confirm('Enter option Gfg', buttons = ['A', 'B', 'C'])
```

`prompt()`: Displays a message box with text input, and OK & Cancel buttons. Returns the text entered, or None if Cancel was clicked.

```python
# Python Program to show prompt() function
import pyautogui

pyautogui.prompt('What is your name?')
```

`password()`: Displays a message box with text input, and OK & Cancel buttons. Typed characters appear as *. Returns the text entered, or None if Cancel was clicked.

```python
# Python Program to show password() function
import pyautogui

pyautogui.password('Enter password (text will be hidden)')
```

## Urllib Module

Urllib package is the URL handling module for python. It is used to fetch URLs. It uses the *urlopen* function and is able to fetch URLs using a variety of different protocols

Urllib is a package that collects several modules for working with URLs, such as:

- urllib.request for opening and reading
- urllib.parse for parsing URLs
- urllib.error for the exceptions raised
- urllib.robotparser for parsing robot.txt files

If urllib is not present, install it using `pip install urllib`

**urllib.request Example**

```python
# Example that opens an URL
import urllib.request

request_url = urllib.request.urlopen('https://www.codefellows.org')
print(request_url.read())
```

**urllib.parse Example**

- This module helps us define functions to manipulate URLs and their component parts, to build or break them. Focuses on splitting a URL into small components or joining different URL components into URL strings.

```python
from urllib.parse import * parse_url = urlparse('https://www.geeksforgeeks.org / python-langtons-ant/')
print(parse_url)
print("\n")
unparse_url = urlunparse(parse_url)
print(unparse_url)
```

**urllib.error**

- This module defines the classes for exception raised by urllib.request. Whenever there is an error in fetching a URL, this module helps in raising exceptions. The following are exceptions raised:
- URLError: raised for the errors in URLs, or errors while fetching the URL due to connectivity
- HTTPError: raised for the exotic HTTP errors, such as the authentication request errors. It is a subclass or URLError.

```python
# URL Error

import urllib.request
import urllib.parse

# trying to read the URL but with no internet connectivity
try:
  x = urllib.request.urlopen('https://www.google.com')
  print(x.read())

# Catching the exception generated
except Exception as e :
  print(str(e))
```

```python
# HTTP Error

import urllib.request
import urllib.parse

# trying to read the URL
try:
 x = urllib.request.urlopen('https://www.google.com / search?q = test')
 print(x.read())

# Catching the exception generated
except Exception as e :
 print(str(e))
```

**urllib.robotparser**

- This module contains a single class, RobotFileParser. This class answers question about whether or not a particular URL that published robot.txt files. This file tells the web scraper about what parts of the server should not be accessed.

```python
# importing robot parser class
import urllib.robotparser as rb

bot = rb.RobotFileParser()

# checks where the website's robot.txt file reside
x = bot.set_url('https://www.geeksforgeeks.org / robot.txt')
print(x)

# reads the files
y = bot.read()
print(y)

# we can crawl the main site
z = bot.can_fetch('*', 'https://www.geeksforgeeks.org/')
print(z)

# but can not crawl the disallowed url
w = bot.can_fetch('*', 'https://www.geeksforgeeks.org / wp-admin/')
print(w)
```
