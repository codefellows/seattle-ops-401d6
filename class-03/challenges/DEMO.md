# Ops Challenge - Uptime Sensor Tool Part 2 of 2

## Demo Code

The demo code below introduces concepts necessary to complete the challenge.

Python offers a library to send emails - `smtplib`
`smtplib` creates a Simple Mail Transfer Protocol client session object which is used to send emails to any valid email id on the internet. The Port number used here is `587`

### Send mail from a Gmail account

Steps to send mail from gmail using Python

1. `smtplib` library needs to be imported
1. Create a session, using its instance SMTP to encapsulate an SMTP connection
   `s = smtplib.SMTP('smtp.gmail.com', 587)`
1. Pass the first parameter of the server location and the second parameter of the port to use. For Gmail, use port number 587
1. For security reasons, put the SMTP connection in TLS mode. TLS mode encrypts all the SMTP commands. After that, for security and authentication, you need to pass your Gmail account credentials in the login instance. The compiler will show an authentication error if you enter an invalid email id or password.
1. Store the message you need to send in a variable. Using the `sendmail()` instance send your `message.sendmail()` uses three parameters: `sender_email_id`, `receiver_email_id`, `message_to_be_sent`. The parameters need to be in the same sequence

**Code Implementation**

This will send the email from your account.

```python
import smtplib

# Creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# Start TLS for security
s.starttls()

# Authentication
s.login("sender_email_id", "sender_email_id_password")

# Message to be sent
message = "Message_you_need_to_send"

# Sending the mail
s.sendmail("sender_email_id", "receiver_email_id", message)

# Terminating the session
s.quit()
```

```python

# This script is optimized for Gmail. Yours may vary for this assignment. Replace values as indicated for the script to function.

import smtplib
server = smtplib.SMTP_SSL(MAILSERVER, PORTNUMBER) # Replace MAILSERVER and PORTNUMBER with the correct values
server.ehlo()

# Next, log in to the server
server.login(SENDEREMAILADDRESS, PASSWORD) # Replace SENDEREMAILADDRESS and PASSWORD with the correct values

# Send the mail
msg = "Hello!" # The /n separates the message from the headers
server.sendmail(SENDEREMAILADDRESS, DESTINATIONEMAILADDRESS, msg) # Replace SENDEREMAILADDRESS and DESTINATIONEMAILADDRESS with the correct values
server.quit()

```

**Example: Send email to multiple recipients using Python**

```python
import smtplib

# list of email_id to send the mail
li = ["xxxxx@gmail.com", "yyyyy@gmail.com"]

for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("sender_email_id", "sender_email_id_password")
    message = "Message_you_need_to_send"
    s.sendmail("sender_email_id", dest, message)
    s.quit()
```
