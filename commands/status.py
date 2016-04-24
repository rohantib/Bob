from classes import *
from helper_functions import *

def method(servers_and_threads):
    print "Which email would you like to check the status of? \n"
    for email in servers_and_threads:
        print email
    print # Line Break
    email = raw_input("Enter email: ").strip()
    try:
        print '"%s": %s' % (email, servers_and_threads[email]["Server"].status)
    except KeyError:
        print "Email %s does not exist as an option." % (email)
    print # Line break

command_object = command.Command("status", "Check the status of a specified spam email", method)
