import os
import sys
import imp 
import tqdm
import time
import getpass
import optparse
import platform
from optparse import OptionParser
from tqdm import *
from time import sleep
from sys import platform as osid

## Project: A.N.D-X (Andromeda-x)  -  Version: 1.0.0  -  Xver: 1.0 ##

__version__ = '1.0.0'

## Check if the user is running windows ##
if osid == 'win32':
    # Print the error message
    print "[!] I cannot run on windows. It will break my modules..."
    print("")
    os.system("pause")
    sys.exit(1)

## Check if the user is in root ##
if os.geteuid() == 1:
    print "\033[31m[-]\033[30 Please run this script as root. Try [sudo] python xcheck.py or 'sudo su' than run the script."
    sys.exit(1)

build = '[1.1]'
version = '1.0'
if version > __version__ or version >= build and __version__ + 1:
    print "[I] Older version in use: " + version + ".build[ " + version + 1 + " ]"
    pass
else:
    pass

## Opts ##
def opts():
    parser = OptionParser(usage="[sudo] xcheck.py [OPTIONS] [ARGS]", conflict_handler="resolve")
    parser.add_option("-D", "--dir", dest="chkDir", default="False", help="Check for a directory")
    parser.add_option("-f", "--file", dest="chkFile", default="False", help="Check for a file")
    parser.add_option("-C", "--createdir", dest="createDir", default="False", help="Create a directory")
    parser.add_option("-c", "--createfile", dest="createFile", default="False", help="Create a file")
    parser.add_option("-v", "--verbose", dest="verbose", default="False", help="Be verbose")
    parser.add_option("-V", "--version", dest="verbose", default="False", help="Show the current script version")

    (option, args) = parser.parse_args()
    if options.chkDir == '1':
        dir1 = raw_input("Enter a directory: ")
        if os.path.exists(dir1):
            print "\033[32m[+]\033[30m Directory exists..."
            sys.exit(1)
        else:
            print "\033[31m[-]\033[30m Directory doesn't exist..."
            sys.exit(1)
    elif options.chkFile == '1':
        file1 = raw_input("Enter a file: ")
        if os.path.isfile("file1"):
            print "\033[32m[+]\033[30m File exists..."
            sys.exit(1)
        else:
            print "\033[31m[-]\033[30m File doesn't exist..."
            sys.exit(1)
    elif options.createDir == '1':
        dir2 = raw_input("Directory to create (with path if needed): ")
        try:
            os.makedirs(dir2)
            pass
        except Exception as e:
            print "\033[31m[-]\033[30m Could not create directory  -  error -> " + str(e)
            sys.exit(1)
    elif options.createFile == '1':
        file2 = raw_input("File to create (with path if needed): ")
        try:
            file3 = open(file2,"wr+")
            file3.close()
        except Exception as e:
            print "\033[31m[-]\033[30m Could not create file  -  error -> " + str(e)
            sys.exit(1)
    # Verbose 

    elif options.version == 'show':
        print __version__
        sys.exit(1)
    else:
        print "\033[31m[-]\033[30m Option not found..."
        sys.exit(1)

## Main ##
os.system("clear")

print "Loading, please wait...\n"
for x in tqdm(range(100)):
    sleep(0.05)
print "\nDone\n"

## Variables ##
author = 'S1lent'
email = 'silentcore32@gmail.com'
email2 = 'gleb.bair@my.sinclair.edu'
xver = '1.0'
xgs = "\033[32m"                                   # Green start
xge = "\033[30m"                                   # Green end
plus = "\033[32m[+]\033[30m"                       # Green [+]
minus = "\033[31m[-]\033[30m"                      # Red [-]
info = "[I]"                                       # Self explanitory
info_urgent = "\033[31m[I]\033[30m"                # Red [I]
regular = "[*]"                                    # Self explanitory
regular_urgent = "\033[31m[*]\033[30m"             # Red [*]

## Directories ##
CONFIG = "/root/andx/config"
BOTS = "/root/andx/bots"
XRTK = "/root/andx/xrtk"
XBD = "/root/andx/xbd"
SRCS = "/root/andx/srcs"
XGUI = "/root/andx/xgui"
LOGS = "/root/andx/logs"
SITE = "/root/andx/site"
# Directories (Site [site])
site_downloads = "/root/andx/site/downloads"
site_css = "/root/andx/site/css"
site_images = "/root/andx/site/images"
site_js = "/root/andx/site/javascript"
site_php = "/root/andx/site/php"
site_java = "/root/andx/site/java"
site_python = "/root/andx/site/python"

## Files ##
xconfig = "/root/andx/config/xconfig.txt"
xlog_a = "/root/andx/logs/xlogs-a.txt"
# Files (Site [site] {HTML (.html)})
index_html = "/root/andx/site/index.html"
downloads_html = "/root/andx/site/downloads.html"
help_html = "/root/andx/site/help.html"
about_html = "/root/andx/site/about.html"
register_html = "/root/andx/site/registeration.html"

## Main ##
print("")
print xgs + "=" * 84 + xge + "\n"                                                          # Prints 84 "="
print "\t\t\t " + "-" * 4 + "=" * 5 + "[ By: " + author + " ]" + "=" * 5 + "-" * 4         # Prints ----=====[ By: ${author} ]=====---- 
print "\t\t\t          " + "Version: " + __version__ + "\n"                                # Prints Version ${__version__}
print "\t\t\t Questions? " + email                                                         # Prints Questions? ${email}
print "\t\t\t\t  Running in: " + getpass.getuser()
print xgs + "-" * 84 + xge                                                                 # Prints 84 "-"
print xgs + "*" * 84 + xge + "\n"                                                          # Prints 84 "*"
print regular + " Note: Some directories will create sub-directories.\n"
# Check for needed directories, if the directory exists, print that it exists



# if __name__ == '__main__':
#    opts()
