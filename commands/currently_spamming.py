from classes import *
from helper_functions import *

def method(servers_and_threads):
    print "Emails that are currently spamming:"
    print #Line break
    for email in servers_and_threads:
        if servers_and_threads[email]["Server"].currently_spamming == True:
            print email
    print #Line break


command_object = command.Command("currently_spamming", "Lists all emails that are currently spamming", method)
