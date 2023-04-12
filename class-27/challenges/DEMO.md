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
