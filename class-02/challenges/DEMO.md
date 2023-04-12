# Ops Challenge - Uptime Sensor Tool Part 1 of 2

## Formatting Your Scripts

All Python scripts should include the shebang `#!/usr/bin/env python3` and be named with a `.py` file extension.

## Demo Code

The demo code below introduces concepts necessary to complete the challenge.

> Note: You may use any or none of the code provided below to complete the challenge objectives.

### Python's datetime library

You may wish to utilize Python's datetime library for this challenge.

**Notes**

- Datetime module comes built into Python, so you do not need to install anything
- The module supplies classes to work with date and time
- `Date` and `datetime` are an object in Python, so when you manipulate them, you are actually manipulating objects and **not** strings or timestamps
- The `datetime` module is categorized into 6 main classes:
  - **date**: contains year, month, and date according to the Gregorian calendar
  - **time**: represents the local time of the day which is independent of any particular day
  - **datetime**: is a combination of date and time along with the attributes year, month, day, hour, minute, second, microsecond, etc
  - **timedelta**: A duration expressing the difference between two date, time or datetime instances to microsecond resolution
  - **tzinfo**: provides time zone information objects
  - **timezone**: class that implements the tzinfo abstract base class as a fixed offset from the UTC

**Example: Print current date and time**

```python
#!/usr/bin/env python3

import datetime

now = datetime.datetime.now()
print("Current date and time: ")
print(str(now))
```

**Example: Date object representing date in Python**

```python
#!/usr/bin/env python3

## Python program to demonstrate date class

# import the date class
from datetime import date

# Initializing constructor and passing arguments in the format year, month, date
my_date = date(1996, 12, 11)

print("Date passed as argument is", my_date)

# Uncommenting my_date = date(1996, 12, 39) will raise a ValueError as it is outside range

# Uncommenting my_date = date('1996', 12, 11) will raise a TypeError as a string is passed instead of an integer
```

**Example: Get Current Date**

To return the current local date today() function of date class is used.
today() function comes with several attributes (year, month and day)

```python
#!/usr/bin/env python3

# Python program to print current date
from datetime import date

# Calling the today function of date class
today = date.today()

print("Today's date is", today)
```

**Example: Get Today's year, month and date**

```python
#!/usr/bin/env python3
from datetime import date

# date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("current day:", today.day)
```

**Example: Get date from Timestamp**

We can create date objects from timestamps y=using the fromtimestamp() method.
The timestamp is the number of seconds from 1st January 1970 at UTC to a particular date

```python
from datetime import datetime

# Getting Datetime from timestamp
date_time = datetime.fromtimestamp(1887639468)
print("Datetime from timestamp:", date_time)
```

**Example: Convert Date to String**

```python
from datetime import date

# Calling the today function of date class
today = date.today()

# Converting the date to the string
Str = date.isoformat(today)
print("String Representation", Str)
print(type(Str))
```

### Python's time library

Python time module allows to work with time in Python. Allows functionality like getting the current time, pausing the program from executing, etc.
Python also has a time library with a very useful `sleep` function that lets us pause the script execution for the specified amount of time.

**What is epoch?**
The epoch is the point where time starts and is platform dependent
On Windows and most Unix systems, the epoch is January 1, 1970, 00:00:00 (UTC) and leap seconds are not counted towards the time in seconds since the epoch

**Example: Getting epoch**

```python
# To check what the epoch is on a given platform we can use time.gmtime(0)
import time

print(time.gmtime(0))
```

**Example: Current time in seconds since epoch**

```python
import time

curr = time.time()
print("Current time in seconds since epoch =", curr)
```

**Example: Getting time string from seconds**

`time.ctime()` function returns a 24 character time string but takes seconds as argument and computes time till mentioned seconds. If no argument is passed, time is calculated until the present

```python
import time

# Getting current time by passing the number of seconds since epoch
curr = time.ctime(1627908313.717886)
print("Current time:", curr)
```

**Example: Delaying execution time of programs in Python**

Execution can be delayed using `time.sleep()` method. This method is used to halt the program execution for the time specified in the arguments.

```python
#!/usr/bin/env python3

import time

for i in range(4):

  # using sleep() to halt execution
  time.sleep(1)
  print(i)

print("Start : %s" % time.ctime())
time.sleep( 5 )
print("End : %s" % time.ctime()
```

### Creating an infinite loop

We can use `while True:` to create an unending cycle of commands repeated in perpetuity.

```python

#!/usr/bin/env python3

import time

while True:
   print("Start : %s" % time.ctime())
   time.sleep( 5 )
   print("End : %s" % time.ctime())
```

### Pinging using the OS commands

There are a few ways to approach using ping. This first approach uses operating system commands and is probably the easiest to perform.

```python

#!/usr/bin/env python3

import os;

print(os.system("ping 127.0.0.1"))

```

### Pinging single targets using pythonping

Another approach is to use the `pythonping` library. First you'll need to install pip3. Run `apt install python3-pip` to load up pip for Python3.

Pip3 (PyPi for Python 3) is a library management tool for Python3. We'll use Python3 for most of Ops 401.

Load [pythonping 1.0.14](https://pypi.org/project/pythonping/) using `sudo pip3 install pythonping`.

Execute the below script with `sudo` to avoid permissions issues.

```python

#!/usr/bin/env python3

# The above shebang line is good convention for Python scripts in 401.

# Import Python libraries
from pythonping import ping

# Main
print(ping('8.8.8.8', verbose=True))

```

### Pinging multiple targets using multiping

Another tool you can use is multiping.

Install with `sudo pip3 install multiping`.

```python

#!/usr/bin/env python3

# A small demo, which demonstrates how to use MultiPing

from multiping import MultiPing
from multiping import multi_ping

if __name__ == "__main__":

    # A list of addresses and names, which should be pinged.
    addrs = ["8.8.8.8", "cnn.com", "127.0.0.1", "youtube.com",
             "2001:4860:4860::8888"]

    print("sending one round of pings and checking twice for responses")
    mp = MultiPing(addrs)
    mp.send()
    # First attempt: We probably will only have received response from
    # localhost so far. Note: 0.01 seconds is usually a very unrealistic
    # timeout value. 1 second, or so, may be more useful in a real world
    # example.
    responses, no_responses = mp.receive(0.01)

    print("   received responses:  %s" % list(responses.keys()))
    print("   no responses so far: %s" % no_responses)

    # By now we should have received responses from the others as well
    print("   --- trying another receive ---")
    responses, no_responses = mp.receive(0.1)
    print("   received responses:  %s" % list(responses.keys()))
    print("   still no responses:  %s" % no_responses)
    print("")

    # Sometimes ICMP packets can get lost. It's easy to retry (re-send the
    # ping) to those hosts that haven't responded, yet. Send can be called
    # multiple times and will result in pings to be resent to those addresses
    # from which we have not heard back, yet. Here we try three pings max.
    print("sending again, but waiting with retries if no response received")
    mp = MultiPing(addrs)
    for i in range(3):
        mp.send()
        responses, no_response = mp.receive(0.01)

        print("    received responses:     %s" % list(responses.keys()))
        if not no_response:
            print("    all done, received responses from everyone")
            break
        else:
            print("    %d. retry, resending to: %s" % (i + 1, no_response))
    if no_response:
        print("    no response received in time, even after 3 retries: %s" %
              no_response)
    print("")

    # Having control over your retries is powerful and gives you lots of
    # flexibility, but sometimes you don't want to deal with it manually and
    # just want 'the right thing' to be done for you.
    #
    # Fortunately, MultiPing provides a ready-made function to do the retry for
    # you, called multi_ping(). Specify the overall timeout and the number of
    # additional retries (which are attempted within this timeout). Omit the
    # 'retry' parameter or set to 0 and there will only be a single send.
    #
    # We are also adding an address we won't be able to resolve and set the
    # 'ignore_lookup_errors' flag, to show that those can be ignored if wanted.
    # They will just appear in the 'no response' return list. If the flag is
    # not set then an exception would be thrown.
    addrs.append("cannot.resolve.thiscom")
    print("sending again, waiting with retries via provided send_receive()")
    responses, no_response = multi_ping(addrs, timeout=0.5, retry=2,
                                        ignore_lookup_errors=True)
    print("    reponses: %s" % list(responses.keys()))
    if no_responses:
        print("    no response received in time, even after retries: %s" %
              no_response)

```

These code samples should help you complete today's Ops Challenge. Good luck
