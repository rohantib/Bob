from classes import *
from helper_functions import *

def method(servers_and_threads):
    print "Which email would you like to spam with? \n"
    for email in servers_and_threads:
        print email
    print #Line Break
    email = raw_input("Enter email: ").strip()
    try:
        servers_and_threads[email]["Thread"].start()
        print "Spamming with %s..." % (email)
    except KeyError:
        print "Email %s is not set up." % (email)

command_object = command.Command("spam", "Begin spamming with a specific email", method)
