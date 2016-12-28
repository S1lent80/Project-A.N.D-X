import os
import sys
import imp 
import pytz
import time
import astral
import random
import datetime
import platform
import optparse
from optparse import OptionParser
from time import sleep
from sys import platform as osid
from astral import Astral 
from os import walk
from datetime import datetime, time
# Custom module directory
sys.path.insert(0,"modules")


# *********************************************************************************************

# Check if the user is running Windows
if osid == 'win32':
    try:
        print "I cannot run on Windows, please run me on a Linux System..."
        print("")
        os.system('pause')
    except:
        os.system('echo "I cannot run on windows systems, please run me on a Linux system..."')
        os.system('echo')
        os.system('pause')
    finally:
        sys.exit(1)

# Check if the user is in root
if os.geteuid() == 1:
    print "\nPlease run me as root...\n"
    sys.exit(1)

# *******************************************************************************************

# *******************************************************************************************
# Variables
__version__ = '1.0.0'
author = 'S1lent'
# -> Colors
xgs = "\033[32m"
xrs = "\033[31m"
xys = "\033[33m"
ce = "\033[30m"
# -> Symbols
plus = "\033[32m[+]\033[30m"
minus = "\033[31m[-]\033[30m"
# -> Lists
greet = ['Hello, ', 'Hi, ','Hey, ','*Yawn* Hello, ','*Yawn* Hi, ','*Yawn* Hey, ']



# Classes
class tStyles:
    BOLD = '\033[1m'
    UNLINE = '\033[4m'
    TE = '\033[0m'

# Functions



# *************************************************************************************************
## Main ##
os.system('clear')
greet_random = random.choice(greet)
print xgs + "-" * 4 + "[ " + ce + greet_random + "what can I do for you?" + xgs + " ]" + "-" * 48 + ce + "\n"
