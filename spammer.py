import smtplib, threading, time, random
from helper_functions import *
from classes import *
import commands

#Get Data
toaddrs = file_IO.get_targets("targets.txt")
if len(toaddrs) == 0:
	print "No emails to spam... quitting spammer"
	exit()

print("Spamming %s..." % (", ".join(toaddrs)))
usernames, passwords = file_IO.get_usernames_passwords("credentials.txt")
messages_sent = file_IO.get_messages_sent("messages_sent.txt")
daily_limit = 500
seconds_in_a_day = 24*60*60
servers = server_management.initialize_servers(usernames,passwords)
messages = file_IO.get_messages("message.txt")


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
			file_IO.write_to_messages(messages_sent, "messages_sent.txt")
		except smtplib.SMTPServerDisconnected:
			print "Disconnected by ban, email %s" % (usernames[index])
			servers[index] = server_management.initialize_a_server(usernames[index], passwords[index])
			print "Logged in again to %s" % (usernames[index])
	time.sleep(seconds_in_a_day/daily_limit) #To wait between messages and avoid daily limit
