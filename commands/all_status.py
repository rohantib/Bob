from classes import *
from helper_functions import *

def method(servers_and_threads):
    print # Line break
    for email in servers_and_threads:
        print '"%s": %s' % (email, servers_and_threads[email]["Server"].status)
    print # Line break

command_object = command.Command("all_status", "Shows the status of every spam email", method)
