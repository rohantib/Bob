import smtplib
import time
import random

#Helper Function Definitions
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

def initliaze_a_server(username, password):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(username,password)
	return server
def initialize_servers(usernames, passwords):
	i = 0
	servers = []
	while i < len(usernames):
		servers.append(initliaze_a_server(usernames[i], passwords[i]))
		print "Server initialized, email %s" % (usernames[i])
		i += 1
	return servers

def write_to_messages(messages_sent, file_path):
	with open(file_path, "w") as messages:
		messages.write(" ".join(map(str, messages_sent)))

toaddrs = []
with open("targets.txt", "r") as targets:
	for email in targets:
		if email[:1] != "#":
			toaddrs.append(email.strip())
if len(toaddrs) == 0:
	print "No emails to spam... quitting spammer"
	exit()

print("Spamming %s..." % (", ".join(toaddrs)))
# Credentials (if needed)
usernames, passwords = get_usernames_passwords("credentials.txt")
messages_sent = get_messages_sent("messages_sent.txt")
daily_limit = 500
seconds_in_a_day = 24*60*60
servers = initialize_servers(usernames,passwords)
messages = []
with open("message.txt", "r") as message:
	for line in message:
		messages.append(line)

counter = 0
while True:
	for index, server in enumerate(servers):
		try:
			msg = messages[random.randrange(len(messages))]
			server.sendmail(usernames[index], toaddrs[counter], msg)
			messages_sent[index] += 1
			print "%s sent to %s" % (usernames[index], toaddrs[counter])
			print("%d message(s) sent today from %s, %d total message(s) from %s" % ((((messages_sent[index]-1) % daily_limit) + 1) , usernames[index], messages_sent[index], usernames[index]))
			counter = (counter + 1) % len(toaddrs)
			write_to_messages(messages_sent, "messages_sent.txt")
		except smtplib.SMTPServerDisconnected:
			print "Disconnected by ban, email %s" % (usernames[index])
			servers[index] = initliaze_a_server(usernames[index], passwords[index])
			print "Logged in again to %s" % (usernames[index])
	time.sleep(seconds_in_a_day/daily_limit) #To wait between messages and avoid daily limit
