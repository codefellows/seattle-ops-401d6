# Ops Challenge - Automated Brute Force Wordlist Attack Tool Part 1 of 3

## Demo Code

The demo code below introduces concepts necessary to complete the challenge.

This example code uses PyAutoGUI to cycle through the alphabet.

```python

# Import libraries
import time, getpass

# Declare functions
def iterator ():
    filepath = input("Enter your dictionary filepath:\n")
    #filepath = '/home/osboxes/Desktop/rockyou2.txt' #test filepath
    
    file = open(filepath, encoding = "ISO-8859-1") # address encoding problem
    line = file.readline()
    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close()

# def check_password()
# Add password recognition code here
#
#
#

# Main

if __name__ == "__main__": # when my computer runs this file...do this stuff
    while True:
        mode = input("""
Brue Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Exit
    Please enter a number: 
""")
        if (mode == "1"):
            iterator()
        elif (mode == "2"):
            check_password()
        elif (mode == '3'):
            break
        else:
            print("Invalid selection...") 

```
"DEMO.md" 45L, 1015C                                                                                                                                                 1,1           Top
