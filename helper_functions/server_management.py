"""
Helper functions to initialize SMPT servers with just function calls
"""
import smtplib
def initialize_a_server(username, password):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(username,password)
	return server

def initialize_servers(usernames, passwords):
	i = 0
	servers = []
	while i < len(usernames):
		servers.append(initialize_a_server(usernames[i], passwords[i]))
		print "Server initialized, email %s" % (usernames[i])
		i += 1
	return servers
