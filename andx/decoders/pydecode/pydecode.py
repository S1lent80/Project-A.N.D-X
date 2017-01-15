import os
import sys
import codecs
import base64
import binascii

# Custom module directory
sys.path.insert(0,"modules")

# Make the menu, but first, clear the Terminal

os.system("clear")


# Variables
author = 'S1lent'
__version__ = '1.0.0'
# -> Colors
xgs = "\033[32m"
xrs = "\033[31m"
xys = "\033[33m"
ce = "\033[30m"


# Functions
def menu_banner():
	print xgs + "=" * 89 + ce + "\n"
	print xys + "\t\tPyDecode - Python Decoder" + ce + "\n"
	print xgs + "\t\tAuthor: " + ce + author
	print xgs + "\t\tVersion: " + ce + __version__ + "\n"
	print xgs + "=" * 89 + ce + "\n"

def opt_1_banner():
	print xgs + "=" * 89 + ce + "\n"
	print xys + "\t\tHex Decode Mode" + ce + "\n"
	print xgs + "=" * 89 + ce + "\n\n"

def opt_2_banner():
	print xgs + "=" * 89 + ce + "\n"
	print xys + "\t\tBase64 Decode Mode" + ce + "\n"
	print xgs + "=" * 89 + ce + "\n\n"

# Classes
class cmd_access:
	@staticmethod
	# Options
	def enc_str(a):
		choice = raw_input("\nWhich encoding should I use? [B]ase64 [H]ex: ")
		# If else statements
		pass

	def prompt():
		a = raw_input(xgs + "X:PROMPT> " + ce)


# Main
menu = {}
menu[xgs + '1' + ce] = xys + "Decode Hex string" + ce
menu[xgs + '2' + ce] = xys + "Decode Base64 String" + ce 
menu[xgs + '3' + ce] = xys + "Decode BinAscii String" + ce
menu[xgs + '4' + ce] = xys + "Exit program..." + ce + "\n\n"
# More menu options

while True:
	menu_banner()
	options = menu.keys()
	options.sort()
	for entry in options:
		print entry, menu[entry]
	select = raw_input(xgs + "Please choose an option: " + ce)
	if select == '1':
		os.system("clear")
		# Call function opt_1_banner
		opt_1_banner()
		print("")
		string_1 = raw_input(xgs + "Decode Hex string: " + ce)
		if len(string_1) == 0:
			print xrs + "[-]" + ce + " Please input a Hex string for me to decode..."
		elif string_1 == "x_prompt" or string_1 == "prompt" or string_1 == "xcmd":
			cmd_access.prompt()
			pass
		# a = string_1
		# b = binascii.a2b_hex(a)
		# a2 = codecs.getdecoder(a)
		print("")
		print string_1.decode('hex')
		os.system("read -p 1 line")
		os.system("clear")
	elif select == '2':
		os.system("clear")
		# Call function opt_2_banner
		opt_2_banner()
		print("")
		string_2 = raw_input(xgs + "Decode Base64 string: " + ce)
		if len(string_2) == 0:
			print xrs + "[-]" + ce + " Please input a Base64 string for me to decode..."
		a2 = base64.b16decode(string_2)
		print("")
		print xgs + "[+]" + ce + " The Base64 string is: " + xys + a2 + ce
		os.system("read -p -1 line")
		os.system("clear")
	elif select == '3':
		# Pass for now
		pass
	elif select == '4':
		print("")
		# I will have it print something random later on
		print xgs + "Have a nice day!" + ce
		break
	else:
		print xrs + "[-]" + ce + " Unknown option selected..."
