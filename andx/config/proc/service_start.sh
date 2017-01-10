#!/bin/bash

# Service menu

# Variables
path='/root/andx/config/proc'
alt='alt'
author='S1lent'
version='1.0.0'
date_now=$(date +%y"/"%m"/"%d)
date_sys=$(date)
# write_data_a=$(date_now > /root/andx/config/xconfig.txt)
# write_data_b=$(date_sys > /root/andx/config/xconfig.txt)

# Check if directory exists (alt)
if [ ! -d $alt ]; then
	mkdir $alt
else
	# Directory exists...
	echo -e "\033[32m[+]\033[0m Directory /$alt  exist..."
fi

# Just checking something
if [ ! -d $path ]; then
	echo -e "\n\033[31m[-]\033[0m Directory: $path\ , doesn't exist, enter the path to the directory\n"
	read -p "Path to directory: "
	if [[ -d $REPlY ]]; then
		cd; echo "PATH_ALT($path) = $REPLY" >> /root/andx/config/xconfig.txt
	else
		echo -e "\n\033[31mCould not find directory: \033[0m $path\n"
	fi
fi
#
echo -e "\033[32m[>]\033[0m User: $USER"
echo -e "\033[32m[>]\033[0m UID:  $UID"
echo -e "\033[32m[>]\033[0m HOME: $HOME"
#
echo
echo -e "\033[32mDate: \033[0m$date_now  -  $date_sys"
echo
#
if [ ! -f "config" ]; then
	echo -e "\n\033[33m[I]\033[0m Creating file 'config.txt' in current directory: \033[32m$path\033[0m\n"
	echo -e "\033[32m[+]\033[0m Writing data to 'config.txt'"
	touch config.txt
	date > config.txt
	who > config.txt
else
	echo -e "\033[32m[+]\033[0m Writing data to 'config.txt'"
	date > config.txt
	who > config.txt
fi
#
# Clear the Terminal
#
clear 
#
# The functions
#
function start_ssh
{
	# SSH service
}

function start_network
{
	# Start network manager
	if [ "$(id -u)" != 0 ]; then
		sudo service networking start | service network-manager start
	else
		service networking start | service network-manager start
	fi
}

# Menu
function menu
{
	# Menu code
}




