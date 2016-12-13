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

# **************************************************************************************************************************************************************************
# st.int(a) = 1.st.int[]{'1':'A' -> '2':'B' <- '$a':'C':$result};
# st.int(b) = 2.st.int[]{'1':'${a}' -> '2':'$B + $C' <- '$a[$B + $C]':$result};
# func main(int *(a), int *(b) -> $result[int *(a + ${$[a]} * b + ${$[b]})]) { a1 = char &*int[{2}] >> ${*} + ${'$a' + $b >> %}; result2 = a1 * 2 / 100; os.print $result }
# **************************************************************************************************************************************************************************

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
xrs = "\033[31m"                                   # Red start
xre = "\033[30m"                                   # Red end
xbs = "\033[34m"                                   # Blue start
xbe = "\033[30m"                                   # Blue end
xes = "\033[33m"                                   # Yellow start
xse = "\033[30m"                                   # Yellow end 
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
# Directories (Scanners [scanners])
scn_c = "/root/andx/scanners/c"
# - Directories (/scanners/c)
scn_c_src = "/root/andx/scanners/c/src"
scn_c_ps = "/root/andx/scanners/c/portscanner"
scn_c_vulns = "/root/andx/scanners/c/vulns"
# --------------------------------------------
scn_cpp = "/root/andx/scanners/c++"
scn_web = "/root/andx/scanners/web"
scn_os = "/root/andx/scanners/os"
REPORTER = "/root/andx/reporter"
XGUI = "/root/andx/xgui"
LOGS = "/root/andx/logs"
CHAT_BOT = "/root/andx/chat_bot"
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

## Lists ##
list_tools = ['Responder', 'Metasploit', 'Sqlmap', 'Nikto', 'Nmap']

## Main ##
print("")
# print xrs + "*" * 84 + xre                                                                                         # Prints 84 "*"
print xgs + "=" * 84 + xge + "\n"                                                                                    # Prints 84 "="
print "\t\t\t " + "-" * 4 + "=" * 5 + "[" + xes + " By: " + xse + xgs + author + xge + " ]" + "=" * 5 + "-" * 4      # Prints ----=====[ By: ${author} ]=====---- 
print "\t\t\t          " + xes + "Version: " + xse + xgs + __version__ + xge + "\n"                                  # Prints Version ${__version__}
print "\t\t\t " + xes + "Questions? " + xse + xgs + email + xge                                                      # Prints Questions? ${email}
print "\t\t\t\t" + xes + "  Running in: " + xse + xgs + getpass.getuser() + xge                                      # Prints Running in: root
print xgs + "-" * 84 + xge                                                                                           # Prints 84 "-"
print xgs + "*" * 84 + xge + "\n"                                                                                    # Prints 84 "*"
print regular + " Note: Some directories will create sub-directories.\n"
# Check for needed directories, if the directory exists, print that it exists
print regular + " Checking directories...\n"
if os.path.exists(LOGS):
    pass
else:
    try:
        os.makedirs(LOGS)
        file1 = open(xconfig,"w")
        pass
    except Exception as e:
        print minus + " Could not create directory..."
        pass
# ------------------------------------------------------------------------------------------------------------------------------------------------
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
            while len(dir_02) == 0:
                print minus + " I need a directory...\n"
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
        if not 'M' or 'm' or 'D' or 'd' in question_02 or len(question_02) == 0:
            print minus + " I need an input, please enter a 'M' ('m') if the file was moved, or 'D' ('d') if the file was deleted...\n"
            pass
        else:
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + CONFIG + xge
    try:
        os.makedirs(CONFIG)
        file1.write("Directory [Config (config)]:     " + CONFIG + " created...\n")
        pass
    except Exception as e:
        print exc + " Could not create directory: " + xgs + CONFIG + xge + " error -> " + str(e)
        # Write to log file
        file2.write("[ ERROR ]: " + str(e) + "\n")
        print info + " Exiting..."
        sys.exit(1)
# ----------------------------------------------------------------------------------------------------------------------------------------------
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
        if not 'M' or 'm' or 'D' or 'd' in question_01 or len(question_01) == 0:
            print minus + " Input needed: please type an [ 'M' ('m') = Moved or 'D' ('d') = Deleted ]...\n"
            pass
        else:
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + XRTK + xge
    try:
        os.makedirs(XRTK)
        file1.write("Directory [ Xrtk (xrtk)]:         " + XRTK + " created...\n")
    except Exception as e3:
        print minus + " Could not create directory: " + xgs + XRTK + xge + " error -> " + str(e3)
        file2.write("[ ERROR ]: " + str(e3) + "\n")
        print info + " Exiting..."
        sys.exit(1)
# ---------------------------------------------------------------------------------------------------------------------------------------------
if os.path.exists(SCANNERS):
    print plus + " Directory: " + xgs + SCANNERS + xge + " exists... Will now check for it's sub-directories..."
    file1.write("Directory [ Scanners (scanners)]:      " + SCANNERS + " exists...\n")
    if os.stat(SCANNERS) == 0:
        print minus + " Directory: " + xgs + SCANNERS + xge + " existed, but isn't there now..."
        question_08 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        if 'M' in question_08 or 'm' in question_08:
            dir_08 = raw_input("Enter the new directory: ")
            # After this program (project) is complete, no Anti-Virus will be able to protect you...You won't find, me - S1lent
            if os.path.exists(dir_08) or os.path.join(dir_08, "/scanners") or os.path.join(dir_08, "scanners"):
                file1.write("Directory [ Alt ] Scanners (scanners):     " + dir_08 + "\n")
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
        if not 'M' or 'm' or 'D' or 'd' in question_08 or len(question_08) == 0:
            print minus + " Please type an 'M' ('m') for Moved or 'D' ('d') for Deleted...\n"
            pass
        else:
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + SCANNERS + xge
    try:
        os.makedirs(SCANNERS)
        file1.write("Directory [ Scanners (scanners)]:     " + SCANNERS + " created...\n")
    except Exception as e5:
        print exc + " Could not create directory: " + xgs + SCANNERS + xge + " error -> " + str(e5)
        print info + " Exiting..."
        sys.exit(1)
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Create the sub-directories and files for the [ Scanners (scanners)] directory
## Check for directories and files ##
# [+] Directory: [ PATH_TO_SCANNERS ] exists...
# |_[SUB_DIR] - [ C ] exists...
# | |_[SUB_DIR] - [ SRC ] exists...
# | |_[SUB_DIR] - [ PORT_SCANNER ] exists...
# | |_[SUB_DIR] - [ VULNS ] exists...
# |-------------------------------------------
# |_[SUB_DIR] - [ C++ ] exists...
# |_[SUB_DIR] - [ Web ] exists...
# |_[SUB_DIR] - [ OS ] exists...
#####################################################################################
# I try to ask for help, no one replies...I try to talk to them, they won't listen, or not attempt to try to understand...They looked like people I could talk to, they sounded promising, they looked like they would understand...But no, I was mistaken, it was a mistake to think that I could put my hopes in them...Now, I do this alone...Without their help...My help, is the search engine, and knowledge of what I need to accomplish...
# ------------------------------------------------------------------------------------------------------------------------------------------------
if os.path.exists(scn_c):
    print xgs + "|__|_" + xge + "[Sub-Dir] - " + xgs + scn_c + xge + " exists..."
    file1.write("|_[SUB_DIR] - " + scn_c + " exists...\n")
    if os.stat(scn_c) == 0:
        print minus + " Directory: " + xgs + scn_c + xge + " existed, but isn't there now..."
        question_09 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        if 'M' in question_09 or 'm' in question_09:
            dir_09 = raw_input("Enter the new directory: ")
            if os.path.exists(dir_09) or os.path.join(dir_09, "/c") or os.path.join(dir_09, "c"):
                file1.write("|_[SUB_DIR_ALT] - " + dir_09 + "\n")
            else:
                print minus + " Could not find directory..."
                print info + " Exiting..."
                sys.exit(1)
        elif 'D' in question_09 or 'd' in question_09:
            print info + " Creating directory: " + xgs + scn_c + xge
            try:
                os.makedirs(scn_c)
            except KeyboardInterrupt:
                # Print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e8:
                print exc + " Could not create directory: " + xgs + scn_c + xge + " error -> " + str(e8)
                print info + " Exiting..."
                sys.exit(1)
        if not 'M' or 'm' or 'D' or 'd' or len(question_09) == 0:
            print minus + " Inputs are 'M' ('m') for Moved or 'D' ('d') for Deleted...\n"
            pass
        else:
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + scn_c + xge
    try:
        os.makedirs(scn_c)
        file1.write("|_[SUB_DIR] - " + scn_c + " created...\n")
    except Exception as e9:
        print exc + " Could not create directory: " + xgs + scn_c + xge + " error -> " + str(e9)
        print info + " Exiting..."
        sys.exit(1)
# -----------------------------------------------------------------------------------------------------------------------------------------------
if os.path.exists(scn_c_src):
    print xgs + "|____|_" + xge + "[SUB_DIR_C] - " + xgs + scn_c_src + xge + " exists..."
    file1.write("      |_[SUB_DIR_C] - " + scn_c_src + " exists...\n")
    if os.stat(scn_c_src) == 0:
        print minus + " [ SUB ] - Directory: " + xgs + scn_c_src + xge + " existed, but isn't there..."
        question_07 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        if 'M' in question_07 or 'm' in question_07:
            dir_07 = raw_input("Enter the new directory: ")
            if os.path.exists(dir_07) or os.path.join(dir_07, "/src") or os.path.join(dir_07, "src"):
                file1.write("      |_[SUB_DIR_C] - " + dir_07 + "\n")
            else:
                print minus + " Could not find directory..."
                print info + " Exiting..."
                sys.exit(1)
        elif 'D' in question_07 or 'd' in question_07:
            print info + " Creating directory: " + xgs + scn_c_src + xge
            try:
                os.makedirs(scn_c_src)
            except KeyboardInterrupt:
                # Print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e10:
                print exc + " Could not create directory: " + xgs + scn_c_src + xge + " error -> " + str(e10)
                print info + " Exiting..."
                sys.exit(1)
        if not 'M' or 'm' or 'D' or 'd' in question_07 or len(question_07) == 0:
            print minus + " Input needed, [M] = Moved, [D] = Deleted...\n"
            pass
        else:
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + scn_c_src + xge
    try:
        os.makedirs(scn_c_src)
        file1.write("|____|_[SUB_DIR_C] - " + scn_c_src + " created...\n")
    except Exception as e11:
        print exc + " Could not create directory: " + xgs + scn_c_src + xge + " error -> " + str(e11)
        print info + " Exiting..."
        sys.exit(1)
# ------------------------------------------------------------------------------------------------------------------------------------------------
if os.path.exists(scn_c_ps):
    print xgs + "|____|_" + xge + "[SUB_DIR_C] - " + xgs + scn_c_ps + xge + " exists..."
    file1.write("      |_[SUB_DIR_C] - " + scn_c_ps + " exists...\n")
    if os.stat(scn_c_ps) == 0:
        print minus + " Directory: " + xgs + scn_c_ps + xge + " existed, but isn't there..."
        question_03 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        if 'M' in question_03 or 'm' in question_03:
            dir_03 = raw_input("Enter the new directory: ")
            if os.path.exists(dir_03) or os.path.join(dir_03, "/portscanner") or os.path.join(dir_03, "portscanner"):
                file1.write("     |_[SUB_DIR_C] - " + scn_c_ps + "\n")
            else:
                print minus + " Could not find directory..."
                print info + " Exiting..."
                sys.exit(1)
        elif 'D' in question_03 or 'd' in question_03:
            print info + " Creating directory: " + xgs + scn_c_ps + xge
            try:
                os.makedirs(scn_c_ps)
            except KeyboardInterrupt:
                # Print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e12:
                print exc + " Could not create directory: " + xgs + scn_c_ps + xge + " error -> " + str(e12)
                print info + " Exiting..."
                sys.exit(1)
        else:
            pass
else:
    print info + " Creating directory: " + xgs + scn_c_ps + xge
    try:
        os.makedirs(scn_c_ps)
        file1.write("      |_[SUB_DIR_C] - " + scn_c_ps + " created...\n")
    except Exception as e13:
        print exc + " Could not create directory: " + xgs + scn_c_ps + xge + " error -> " + str(e13)
        print info + " Exiting..."
        sys.exit(1)
# ------------------------------------------------------------------------------------------------------------------------------------------------
if os.path.exists(scn_cpp):
    print xgs + "|_" + xge + "[SUB_DIR] - " + xgs + scn_cpp + xge + " exists..."
    file1.write("|_[SUB_DIR] - " + scn_cpp + " exists...\n")
    if os.stat(scn_cpp) == 0:
        print minus + " Directory: " + xgs + scn_cpp + xge + " existed, but isn't there..."
        question_05 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        if 'M' in question_04 or 'm' in question_04:
            dir_05 = raw_input("Enter the new directory: ")
            if os.path.exists(dir_05) or os.path.join(dir_05, "/cpp") or os.path.join(dir_05, "cpp"):
                file1.write("|_[SUB_DIR] - (Alt): " + dir_05 + "\n")
            else:
                print minus + " Could not find directory..."
                print info + " Exiting..."
                sys.exit(1)
        elif 'D' in question_04 or 'd' in question_04:
            print info + " Creating directory: " + xgs + scn_cpp + xge
            try:
                os.makedirs(scn_cpp)
            except KeyboardInterrupt:
                # Print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e14:
                print exc + " Could not create directory: " + xgs + scn_cpp + xge + " error -> " + str(e14)
                print info + " Exiting..."
                sys.exit(1)
        else:
            print minus + " Option not found..."
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + scn_cpp + xge
    try:
        os.makedirs(scn_cpp)
        file1.write("|_[SUB_DIR] - " + scn_cpp + " created...\n")
    except Exception as e15:
        print exc + " Could not create directory: " + xgs + scn_cpp + xge + " error -> " + str(e15)
        print info + " Exiting..."
        sys.exit(1)
# -------------------------------------------------------------------------------------------------------------------------------------------------
if os.path.exists(SITE):
    print plus + " Directory: " + xgs + SITE + xge + " exists...  -  Will now check it's sub-directories"
    file1.write("Directory [Site (site)]:               " + SITE + " exists...\n")
    if os.stat(SITE) == 0:
        print minus + " Directory: " + xgs + SITE + xge + " existed, but isn't there anymore...\n"
        question = raw_input("Was the file [M]oved or [D]eleted? : ")
        if 'M' in question or 'm' in question:
            dir3 = raw_input("Enter the new directory: ")
            if os.path.exists(dir3) or os.path.join(dir3,"/site") or os.path.join(dir3,"site"):
                file1.write("Directory [ Alt ] Site (site):     " + SITE + "\n")
            else:
                print minus + " Could not find directory..."
                print info + " Exiting..."
                sys.exit(1)
        if 'D' in question or 'd' in question:
            print info + " Creating directory: " + xgs + SITE + xge
            try:
                os.makedirs(SITE)
            except KeyboardInterrupt:
                # print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e16:
                print exc + " Could not create directory: " + xgs + SITE + xge + " error -> " + str(e16)
                print info + " Exiting..."
                sys.exit(1)
        if not 'M' in question or not 'm' in question or not 'D' in question or 'd' in question:
            print minus + " I need your input...Please select (type) 'M' or 'm' if the file was moved, or 'D' ('d') if the file was deleted...\n"
            pass
        else:
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + SITE + xge
    try:
        os.makedirs(SITE)
        file1.write("Directory [Site (site)]:             " + SITE + " created...\n")
    except Exception as e17:
        print exc + " Could not create directory: " + xgs + SITE + xge + " error -> " + str(e17)
        print info + " Exiting..."
        sys.exit(1)


# -------------------------------------------------------------------------------------------------------------------------------------------------
if os.path.exists(XBD):
    print("")
    print plus + " Directory: " + xgs + XBD + xge + " exists..."
    file1.write("\nDirectory [Xbd (xbd)]:                 " + XBD + " exists...\n")
    file1.close()
    if os.stat(XBD) == 0:
        print minus + " Directory: " + xgs + XBD + xge + " existed, but isn't there anymore..."
        question_04 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        if 'M' in question_04 or 'm' in question_04:
            dir_04 = raw_input("Enter the new directory: ")
            if os.path.exists(dir_04) or os.path.join(dir_04,"/xbd") or os.path.join(dir_04,"xbd"):
                file1.write("Directory [ Alt ] Xbd (xbd):    " + XBD + "\n")
                file1.close()
            else:
                print minus + " Could not find directory..."
                print info + " Exiting..."
                sys.exit(1)
        elif 'D' in question_04 or 'd' in question_04:
            print info + " Creating directory: " + xgs + XBD + xge
            try:
                os.makedirs(XBD)
            except KeyboardInterrupt:
                # Print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e6:
                print exc + " Could not create directory: " + xgs + XBD + xge + " error -> " + str(e6)
                print info + " Exiting..."
                sys.exit(1)
        else:
            pass
else:
    print info + " Creating directory: " + xgs + XBD + xge
    try:
        os.makedirs(XBD)
        file1.write("Directory [ Xbd (xbd)]:                 " + XBD + " created...\n")
        file1.close()
    except Exception as e7:
        print exc + " Could not create directory: " + xgs + XBD + xge + " error -> " + str(e7)
        print info + " Exiting..."
        sys.exit(1)



# if __name__ == '__main__':
#    opts()
