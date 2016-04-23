#!/usr/bin/python
from helper_functions import *
from classes import *
from commands import * #Run all the files in the package "commands" to initialize all command objects

servers_and_threads = set_up_emails.initialize_servers_and_threads()

#Welcome message
print "Welcome to the Python spammer bot! Type \"help\" for a list of commands."

while True:
	try:
		user_input = raw_input("Enter command: ")
		command.Command.run_command(servers_and_threads, user_input)
	except KeyboardInterrupt:
		print # Line break
		print "Exitting spammer..."
		exit()
