# Ops Challenge - Event Logging Tool Part 2 of 3

## Demo Code

The demo code below introduces concepts necessary to complete the challenge.

```python
# For this to work, set each VALUE variable as called out below in comments.

import logging, time, os
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('my_logger')
handler = RotatingFileHandler('my_log.log', maxBytes=VALUE, backupCount=VALUE) #set each VALUE
logger.addHandler(handler)

for i in range(VALUE): #set each VALUE
    logmsg = "Hello world!"
    logmsg += str(i)
    logger.warning(logmsg)
    print("Logging Hello world! number", i)
    os.system("ls -al")
    time.sleep(.1)

```

# Lecture Notes: Python rotating log files

The python logging module gives us the `RotatingFileHandler` class and the `TimedRotatingFileHandler` class to split up the log files generated

**RotatingFileHandler**

`RotatingFileHandler` allows us to rotate logs into a new file every time the current log file reaches a certain size.

**Example**

This script will rotate logs into a new file when it reaches 500 bytes up to a max number of 2 backups

```python
import logging
import logging.handlers as handlers
import time

logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)

logHandler = handlers.RotatingFileHandler('app.log', maxBytes=500, backupCount=2)
logHandler.setLevel(logging.INFO)
logger.addHandler(logHandler)

def main():
    while True:
        time.sleep(1)
        logger.info("A Sample Log Statement")

main()
```

**TimedRotatingFileHandler**

`TimedRotatingFileHandler` allows us to capture log files by a time slice

```python
import logging
import logging.handlers as handlers
import time

logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)

logHandler = handlers.TimedRotatingFileHandler('timed_app.log', when='M', interval=1)
logHandler.setLevel(logging.INFO)
logger.addHandler(logHandler)

def main():
    while True:
        time.sleep(1)
        logger.info("A Sample Log Statement")

main()
```
