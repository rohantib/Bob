"""
Set up emails with a dictionary containing server and thread objects
"""
import os
import classes

def initialize_servers_and_threads():
	"""
	Returns a dictionary object containing an initialized server and thread object for each email
	"""
	servers_and_threads = {}
	for email in os.listdir(".emails"):
		server = classes.server.Server(email)
		servers_and_threads[email] = {"Server": server, "Thread": classes.server.ServerThread(server)}
	return servers_and_threads
