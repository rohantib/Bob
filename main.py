#!/usr/bin/python
import helper_functions
import classes
from commands import * #Run all the files in the package "commands" to initialize all command objects

#Initialize all servers and their corresponding threads
servers_and_threads = helper_functions.set_up_emails.initialize_servers_and_threads()

#Welcome message
print "Hey there! Let's start spamming! I'm thirsty to rain it on someone's inbox. Type \"help\" for a list of commands, and let's get going!"
print "If you desperately need to quit when I'm in the middle of something, hit CTRL+C. But you risk breaking me when you do that, so please try not to!"

while True:
	try:
		user_input = raw_input("Enter command: ")
		classes.command.Command.run_command(servers_and_threads, user_input)
	except KeyboardInterrupt:
		print # Line break
		print "Bob is quitting... Goodbye!"
		exit()
