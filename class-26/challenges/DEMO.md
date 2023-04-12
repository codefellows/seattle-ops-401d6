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
