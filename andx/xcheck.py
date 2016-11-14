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
exc = "\033[31m[!]\033[30m"                        # Red [!]
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
SCANNERS = "/root/andx/scanners"
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
print "\t\t\t\t  Running in: " + getpass.getuser()                                         # Prints Running in: root
print xgs + "-" * 84 + xge                                                                 # Prints 84 "-"
print xgs + "*" * 84 + xge + "\n"                                                          # Prints 84 "*"
print regular + " Note: Some directories will create sub-directories.\n"
# Check for needed directories, if the directory exists, print that it exists
print regular + " Checking directories...\n"
if os.path.exists(LOGS):
    pass
else:
    try:
        os.makedirs(LOGS)
        pass
    except Exception as e:
        print minus + " Could not create directory..."
        pass

if os.path.exists(CONFIG):
    print plus + " Directory: " + xgs + CONFIG + xge + " exists..."
    file1 = open(xconfig,"w")
    file1.write("==========[ Xcheck " + __version__ + " ]==============================================\n\n")
    file1.write("Directory [Config (config)]:           " + CONFIG + " exists...\n")
    if os.stat(CONFIG) == 0:
        print minus + " Directory: " + xgs + CONFIG + xge + " existed, but isn't there now..."
        question_02 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        if 'M' in question_02 or 'm' in question_02:
            dir_02 = raw_input("Enter the new directory: ")
            if os.path.exists(dir_02) and os.path.join(dir_02, "/config") or os.path.join(dir_02, "config"):
                file1.write("Directory [ Alt ] Config (config):      " + dir_02 + "\n")
            else:
                print minus + " Directory cannot be found..."
                print info + " Exiting..."
                sys.exit(1)
        elif 'D' in question_02 or 'd' in question_02:
            print info + " Creating directory: " + xgs + CONFIG + xge
            try:
                os.makedirs(CONFIG)
                pass
            except KeyboardInterrupt:
                # Print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e:
                print exc + " Could not create directory: " + xgs + CONFIG + xge + " error -> " + str(e)
                # Write to log file
                file2 = open(xlog_a,"w")
                file2.write("[ ERROR ]: " + str(e) + "\n")
                print info + " Exiting..."
                sys.exit(1)
        else:
            print minus + " Option not found..."
            pass
else:
    print info + " Creating directory: " + xgs + CONFIG + xge
    try:
        os.makedirs(CONFIG)
        file1.write("Directory [Config (config)]:     " + CONFIG + " created...\n")
        file1.close()
        pass
    except Exception as e:
        print exc + " Could not create directory: " + xgs + CONFIG + xge + " error -> " + str(e)
        # Write to log file
        file2.write("[ ERROR ]: " + str(e) + "\n")
        print info + " Exiting..."
        sys.exit(1)
if os.path.exists(XRTK):
    print plus + " Directory: " + xgs + XRTK + xge + " exists..."
    file1.write("Directory [ Xrtk (xrtk)]:              " + XRTK + " exists...\n")
    pass
    if os.stat(XRTK) == 0:
        print minus + " Directory: " + xgs + XRTK + xge + " existed, but isn't there now..."
        question_01 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        if 'M' in question_01 or 'm' in question_01:
            dir_01 = raw_input("Enter the new directory: ")
            if os.path.exists(dir_01) and os.path.join(dir_01, "/config") or os.path.join(dir_01, "config"):
                file1.write("Directory [ Alt ] Xrtk (xrtk):     " + XRTK + "\n")
                file1.close()
            else:
                print minus + " Could not find directory..."
                print info + " Exiting..."
                sys.exit(1)
        elif 'D' in question_01 or 'd' in question_01:
            print info + " Creating directory: " + xgs + XRTK + xge
            try:
                os.makedirs(XRTK)
                pass
            except KeyboardInterrupt:
                # Print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e2:
                print exc + " Could not create directory: " + xgs + XRTK + xge + " error -> " + str(e2)
                file2.write("[ ERROR ]: " + str(e2) + "\n")
                file2.close()
        else:
            print minus + " Option not found..."
            pass
else:
    print info + " Creating directory: " + xgs + XRTK + xge
    try:
        os.makedirs(XRTK)
        file1.write("Directory [ Xrtk (xrtk)]:         " + XRTK + " created...\n")
        file1.close()
    except Exception as e3:
        print minus + " Could not create directory: " + xgs + XRTK + xge + " error -> " + str(e3)
        file2.write("[ ERROR ]: " + str(e3) + "\n")
        file2.close()
        print info + " Exiting..."
        sys.exit(1)
if os.path.exists(SCANNERS):
    print plus + " Directory: " + xgs + SCANNERS + xge + " exists..."
    file1.write("Directory [ Scanners (scanners)]:      " + SCANNERS + " exists...\n")
    file1.close()
    if os.stat(SCANNERS) == 0:
        print minus + " Directory: " + xgs + SCANNERS + xge + " existed, but isn't there now..."
        question_08 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        if 'M' in question_08 or 'm' in question_08:
            dir_08 = raw_input("Enter the new directory: ")
            if os.path.exists(dir_08) or os.path.join(dir_08, "/scanners") or os.path.join(dir_08, "scanners"):
                file1.write("Directory [ Alt ] Scanners (scanners):     " + dir_08 + "\n")
                file1.close()
            else:
                print minus + " Directory not found..."
                print info + " Exiting..."
                sys.exit(1)
        elif 'D' in question_08 or 'd' in question_08:
            print info + " Creating directory: " + xgs + SCANNERS + xge
            try:
                os.makedirs(SCANNERS)
            except KeyboardInterrupt:
                # Print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e4:
                print exc + " Could not create directory: " + xgs + SCANNERS + xge + " error -> " + str(e4)
                print info + " Exiting..."
                sys.exit(1)
        else:
            pass
else:
    print info + " Creating directory: " + xgs + SCANNERS + xge
    try:
        os.makedirs(SCANNERS)
        file1.write("Directory [ Scanners (scanners)]:     " + SCANNERS + " created...\n")
        file1.close()
    except Exception as e5:
        print exc + " Could not create directory: " + xgs + SCANNERS + xge + " error -> " + str(e5)
        print info + " Exiting..."
        sys.exit(1)
# Create the sub-directories and files for the [ Scanners (scanners)] directory



# if __name__ == '__main__':
#    opts()
