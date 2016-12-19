import os
import sys
import imp
import platform
from sys import platform as osid 

## Python Module: File Check  -  Version: 1.0.0  -  Xver: 1.0 ##

# Checks for needed files and directories that are associated with the project

__version__ = '1.0.0'

xver = 1.0

## Classes ##
class textstyle:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class textcolor_alt:
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    END = "\033[0m"

## Variables ##
xgs = "\033[32m"
xge = "\033[30m"
plus = "\033[32m[+]\033[30m"
minus = "\033[31m[-]\033[30m"
info = "[I]"
regular = "[*]"

## Functions ##
def help_main():
    # Help for this module

## Main ##
def filecheck(filecheck):
    # The help prompt
    if len(filecheck) == 0 or filecheck == False:
        print info + " I need an input. Type 'help' or 'help me' for help with commands..."
        pass
    elif filecheck == 'help' or filecheck == 'help me' or filecheck == 'I need help' or filecheck == 'i need help':

    

def dircheck(filecheck):
   