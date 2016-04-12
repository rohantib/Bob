"""
Module containing helper functions to get or write data from/to the files
containing inputs like message or credentials and data like the number of
messages sent
"""
def get_usernames_passwords(file_path):
	usernames = []
	passwords = []
	credentials_file = open(file_path, "r")
	for line in credentials_file:
		username, password = line.strip().split(" ")
		usernames.append(username)
		passwords.append(password)
	return usernames, passwords

def get_messages_sent(file_path):
	with open(file_path, "r") as messages_sent:
		messages = map(int, messages_sent.readlines()[0].strip().split(" "))
	print "%d total messages sent since first runtime" % (sum(messages))
	return messages

def write_to_messages(messages_sent, file_path):
	with open(file_path, "w") as messages:
		messages.write(" ".join(map(str, messages_sent)))

def get_targets(file_path):
	toaddrs = []
	with open(file_path, "r") as targets:
		for email in targets:
			if email[:1] != "#":
				toaddrs.append(email.strip())
	return toaddrs

def get_messages(file_path):
	messages = []
	with open(file_path, "r") as message:
		for line in message:
			messages.append(line)
	return messages
