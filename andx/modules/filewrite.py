import os
import sys
import imp 
import platform
from sys import platform as osid

## Python Module: FileWrite.py  -  filewrite.py  -  Version: 1.0.0  -  Xver: 1.0 ##

# Write to the files needed for the tool
# -> Extensions: .html, .css, .py, .c, .cpp, .php, .js

def writehtml(index_html):
    # Check if the file exists...
    if os.path.isfile(index_html):
        pass
    else:
        print "[ ERROR ] - File: " + index_html + " doesn't exist..."
        print "[I] Exiting..."
        sys.exit(1)
    index = open(index_html,"w")
    index.write("""
    <!DOCTYPE html>
    <html lang="en">
    <meta>2290-2280-2329</meta>
    <title>Project A.N.D-X | Project Andromeda-X</title>
    <br />
    <h1><div align="center">Project A.N.D-X | Project Andromeda-X</div></h1>
    <br />
    """)
    