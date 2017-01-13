#!/bin/bash

# A.N.D-X Setup Script

# Variables
dir_andx='/root/andx/'
setup='/root/andx/setup'
author='S1lent'

# Update the system
# But first check if the user is in root
if [ "$(id -u)" != 0 ]; then
	echo -e "\033[31m[-]\033[0m Please run this script as root..."
	exit 1
else
	# Clear the Terminal
	clear
	apt-get update
fi



