from classes import *
from helper_functions import *

def method(servers_and_threads):
    if len(servers_and_threads) == 0:
        print 'No email has been set up yet. Use the command "add_email" to set up a new spam email.'
    else:
        print #Line break
        for email in servers_and_threads:
            print email
    print #Line break

command_object = command.Command("emails", "Lists all set up spam emails", method)
