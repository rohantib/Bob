from classes import *
from helper_functions import *

def method(servers_and_threads):
    print #Line break
    for email in servers_and_threads:
        print email
    print #Line break

command_object = command.Command("list_emails", "Lists all set up spam emails", method)
