import os
import sys
import platform
from sys import platform as osid

## Module: Tool Check  -  Version: 1.0.0  -  Xver: 1.0 ##

# A small Python module to check for needed tools

# Variables
xgs = "\033[32m"                                   # Green start
xge = "\033[30m"                                   # Green end
plus = "\033[32m[+]\033[30m"                       # Green [+]
minus = "\033[31m[-]\033[30m"                      # Red [-]

# Lists
tool_list = ['Responder','Metasploit','Sqlmap','Nmap','Nikto']
path_list = ['root','Downloads','Documents','Pictures','Music','usr','share','bin','local']

# Files
file2 = open("/root/andx/config/path_config_tools.txt","+rw")

if osid == 'win32':
    try:
        print "Module cannot run on Windows platforms..."
        print("")
        os.system("pause")
        sys.exit(1)
    except:
        os.system('cmd.exe echo "This module cannot run on Windows platforms..."')
        print("")
        os.system("pause")
        sys.exit(1)

# Check for Metasploit
def msfcheck():
    # Variables
    msf_reg_path = '/usr/share/metasploit-framework'
    msf_opt_path = '/opt/metasploit'
    # Path check
    if os.path.exists(msf_reg_path) or os.path.join("/usr/share/","metasploit-framework") or os.path.join("/usr/share","/metasploit-framework"):
        print plus + " Metasploit path: " + xgs + msf_reg_path + xge + " exists..."
        try:
            file2.write("METASPLOIT_REGULAR_PATH = " + msf_reg_path + "\n")
            pass
        except Exception as e3:
            print minus + " Could not write to file: " + xgs + file2 + xge + " error -> " + str(e3)
            pass
        pass
    elif os.path.exists(msf_opt_path) or os.path.join("/opt","/metasploit") or os.path.join("/opt/","metasploit"):
        print plus + " Metasploit path: " + xgs + msf_opt_path + xge + " exists..."
        try:
            file2.write(",ETASPLOIT_OPT_PATH = " + msf_opt_path + "\n")
            pass
        except Exception as e4:
            print minus + " Could not write to file: " + xgs + file2 + xge + " error -> " + str(e4)
            pass
        pass
    elif not os.path.exists(msf_reg_path) or not os.path.exists(msf_opt_path):
        print minus + " Could not find metasploit in: " + xgs + msf_reg_path + xge + " or " + xgs + msf_opt_path + xge + "...\n"
        # Install Metasploit, for now, use the 'os.system'
        if os.path.join("/root","/Downloads") or os.path.exists("/root/Downloads"):
            # Download Metasploit installer (Linux Edition) to there
            try:
                os.chdir("/root/Downloads")
                pass
            except Exception as e:
                print "\n[-] Could not change directory into " + "/" + path_list[0] + "/" + path_list[1] + " error -> " + str(e)
                pass
            try:
                file2.write("PROC_INSTALL_METASPLOIT::PATH = " + "/" + path_list[0] + "/" + path_list[1] + "\n")
                pass
            except Exception as e2:
                print minus + " Could not write to file: " + xgs + file2 + xge + " error -> " + str(e2)
                pass
        else:
            try:
                os.makedirs("/root/Downloads")
                file2.write("PATH_METASPLOIT_INSTALL::STATUS = CREATED::PATH_OBJECT.PATH = " + "/" + path_list[0] + "/" + path_list[1] + "\n")
                pass
            except Exception as e5:
                print minus + " Could not create directory: " + xgs + "/" + path_list[0] + "/" + path_list[1] + xge + " error -> " + str(e5)
                pass
                # Download and install Metasploit Linux Edition

def responder_check():
    # Check for responder 
    responder_dir = "/usr/share/responder"
    responder_config_file = "/usr/share/responder/Responder.conf"
    responder_alt_path = ""
    # Check the usual directory
    if os.path.exists(responder_dir) and os.path.isfile(responder_config_file):
        print plus + " Responder exists in the directory: " + xgs + responder_dir + xge + " : " + " file: " + xgs + responder_config_file + xge
        file2.write("PATH_RESPONDER_DIRECTORY = " + responder_dir + "\n")
        pass
    elif not os.path.exists(responder_dir) and os.stat(responder_dir) == 0:
        print minus + " Could not find Responder in: " + xgs + responder_dir + xge
        question01 = raw_input("Maybe it was [M]oved or is [R]elocated in another directory? : ")
        while not 'M' or 'm' or 'R' or 'r' in question01:
            print "\nMaybe it was [M|m]oved or [R|r]elocated: hint, enter an [M|m] or [R|r]\n"
        if 'M' in question01 or 'm' in question01:
            newDir01 = raw_input("Enter the new directory: ")
            if newDir01 == False or len(newDir01) == 0 or not os.path.join(newDir01,"/responder") or not os.path.join(newDir01,"responder"):
                if len(newDir01) == 0:
                    print "\nI need an input for the new directory path...\n"
                else:
                    pass
                print minus + " I could not find the directory needed...\n"
                pass
            else:
                file2.write("RESPONDER_NEW_DIRECTORY::MAIN_DIRECTORY = " + newDir01 + "\n")
                pass
        elif 'R' in question01 or 'r' in question01:
            try:
                dir01 = raw_input("Enter the alternate directory: ")
                if len(dir) == "" or len(dir01) == 0 or dir01 == False:
                    print "\nI need a(n) input for the alternative Responder directory...\n"
                else:
                    responder_alt_path = dir01
                    file2.write("RESPONDER_ALT_DIRECTORY::MAIN = " + responder_alt_path + "\n")
                    pass
            except:
                print "[ ERROR ]"
                pass
