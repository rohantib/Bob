#!/usr/bin/python
import helper_functions
import classes
from commands import * #Run all the files in the package "commands" to initialize all command objects
import os

if not os.path.exists(".emails"): # Checks if initial setup needs to be run for first use
	import initial_setup
	initial_setup.setup()
else: # This is in else because this output should not be shown after inital setup is run
	# Welcome message
	print "Hey there! Let's start spamming! I'm thirsty to rain it on someone's inbox. Type \"help\" for a list of commands, and let's get going!"
	print "If you desperately need to quit when I'm in the middle of something, hit CTRL+C. But you risk breaking me when you do that, so please try not to!"

#Initialize all servers and their corresponding threads
servers_and_threads = helper_functions.set_up_emails.initialize_servers_and_threads()

while True:
	try:
		user_input = raw_input("Enter command: ")
		classes.command.Command.run_command(servers_and_threads, user_input)
	except KeyboardInterrupt:
		print # Line break
		print "Bob is quitting... Goodbye!"
		exit()
