import os
import sys
import re
import csv
import time
import random
import platform
import selenium
from time import sleep
from time import time
from random import uniform
from random import randint
from selenium import webdriver
from sys import platform as osid
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException

# Check if the user is running windows
if osid == 'win32':
	try:
		os.system('start cmd.exe echo "I dont run on windows"')
	except:
		os.system('exit')
else:
	pass

# I think I will include this in the ChatBot along with everything else...
# The function that will write statistics
def stat(loops, time):
	cvs_stat_file = open("stat.csv","w")
	with open("stat.csv","a", newline="") as cvsfile:
		spamwriter = csv.writer(cvsfile, delimeter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow([loops, time])

# Check if the path (and or object) exists
def check_xpath_object(xpath):
	try:
		driver.find_element_by_xpath(xpath)
	# The exception if the path and or object doesn't exist
	except NoSuchElementException as e:
		# Print the error
		print "\033[31m[-]\033[0m [ ERROR ] - %s" % (e)
		return False
	return True

# Define the program wait time
def wait(a, b):
	# The two times will be chosen at random
	rand = uniform(a, b)
	sleep(rand)

def dimention(driver):
	# N/A [ NULL ]
	# The directory of the target images for the program
	a = int(driver.find_element_by_xpath('//div[@id="rc-imageselect-target"'))
	# Demention is 3 by default
	return a if a else 3

# Main procedure: The program must identify and submit pictures to the captcha (the solution images)
def captcha_solve(driver):
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "rc-imageselect-target")))
	dim = dimention(driver)
	# Check if the tiles are clickable
	if check_exists_by_xpath('//div[@id="rc-imageselect-target"]/table/tbody/tr/td[@class="rc-imageselect-tileselected"]'):
		rand2 = 0
	else:
		rand2 = 1
	# Wait before the click is initialized on the tiles
	wait_between(0.5, 1.0)
	# Initialize the click on the tile
	tile1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XAPTH, '//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(randint(1, dim), randint(1, dim)))))
	tile1.click()
	if (rand2):
		try:
			driver.find_element_by_xpath('//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(randint(1, dim), randint(1, dim))).click()
		except NoSuchElementException as e2:
			# Print the error
			print "\033[31m[-]\033[0m [ ERROR ] - %s" % (e2)
			print("\n\rNo such element for the tile...\n")
	# Click the submit button after the images have been selected
	# ID of the button: recaptcha-verify-button, this can be changed
	driver.find_element_by_id("recaptcha-verify-button").click()

# Get the start time
start_time = time()
url = "<Your URL Here>"
driver = webdriver.Firefox()
driver.get(url)
# The main window
main_window = driver.current_window_handle

# Move the driver to the first iFrame and set it there
driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])

# Locate the check box
# The ID is recaptcha-anchor, but you can rename it to fit your needs
check_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "recaptcha-anchor")))

# Wait and then click the checkbox
# You can of course set your own wait times
wait_between(0.5, 0.7)
# Click the checkbox
CheckBox.click()

# Back to the main window
driver.switch_to.windows(main_window)
# Wait again
wait_between(1.0, 1.5)

# Switch to the second iframe by tag name
driver.switch_to_frame(driver.find_element_by_tag_name("iframe")[1])
b = 1
while b < 130:
	print("\n\033[32m[ >> ]\033[0m\r{0}-th loop".format(b))
	# Check to see if the checkbox is checked at the 1rst frame
	driver.switch_to.window(main_window)
	WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))
	wait_between(1.0, 2.0)
	if check_exists_by_xpath('//span[@aria-checked="true"]'):
		# Show that the path exists
		print "\n\033[32m[+]\033[0m Path.$PATH('//span[*.*].@aria-checked.bool=True)\n"
		# Save the results
		write_stat(i, round(time() - start) - 1)
		break
	driver.switch_too.window(main_window)
	# The second frame to solve the picture captcha
	wait_between(0.2, 1.4)
	driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[1])
	solve_images(driver)
	b = b + 1
