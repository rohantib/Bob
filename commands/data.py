from classes import *
from helper_functions import *
import os

def method(servers_and_threads):
    print # Line break
    print "Existing emails:"
    for email_key in servers_and_threads:
        print email_key
    print # Line break
    email = raw_input("Which email would you like to view the data of? ")
    print # Line break
    if os.path.exists(".emails/%s" % (email)):
        server = servers_and_threads[email]["Server"]
        print "Email: %s" % (server.email)
        print "Password: %s" % (server.password)
        print "Status: %s" % (server.status)
        print "Total messages sent: %s" % (server.messages_sent)
        print "Targets: %s" % (", ".join(server.targets))
        # Prints messages - linebreaks may be present so each is printed on a separate line
        print "Messages:"
        for index, message in enumerate(server.messages):
            print "[%d] - %s" % (index, message)
        print # Line break
    else:
        print "%s is not an existing spam email." % (email)

# Uses the Command class to set up your command in a predefined format and makes it accessible in memory
command_object = command.Command("data", "Get all the data of a specified email", method)
