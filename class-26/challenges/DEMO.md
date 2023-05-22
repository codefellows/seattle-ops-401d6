# Ops Challenge - Event Logging Tool Part 1 of 3

## Demo Code

The demo code below introduces concepts necessary to complete the challenge.

The below examples are from the [Ultimate Guide to Logging](https://www.loggly.com/ultimate-guide/python-logging-basics/) article.

The first example shows basic module-based logging.

```python

import logging

log = logging.getLogger(__name__)

def do_something():
    log.debug("Doing something!")

```

Next, let's take a look at logging using standard output. This will log all messages with level INFO or above to `stderr`.

```python

import logging
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

exit(main())

```

Try to incorporate logging capabilities into your Python tools.

# Lecture Notes: Python Logging

Python's built-in logging module allows writing status messages to a file or any other output streams. The file can contain the information on which part of the code is executed and what problems have occurred

**Levels of Log Message**

There are give built-in levels of the log message

- **Debug**: used to give detailed information, usually useful when diagnosing problems
- **Info**: used to confirm that things are working as expected
- **Warning**: used as an indication that something unexpected happened, or is a sign of some problem in the near future
- **Error**: sign of a serious problem
- **Critical**: sign that the program is unable to continue running, a serious error

**Example**

This code will generate a file with the provided name and will write logging messages to the file

```python
# importing module
import logging

# Create and configure logger
logging.basicConfig(filename="newfile.log",
     format='%(asctime)s %(message)s',
     filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
```
