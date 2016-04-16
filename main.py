#!/usr/bin/python
from helper_functions import *
from classes import *
import time

servers_and_threads = set_up_emails.initialize_servers_and_threads()

#Welcome message
print "Welcome to the Python spammer bot! Type help for a list of commands."

while True:
	user_input = raw_input("Enter command: ")
	run_command(user_input, servers_and_threads)
