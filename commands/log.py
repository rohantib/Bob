from classes import *
from helper_functions import *
import os

def method(servers_and_threads):
    print # Line break
    print "Existing emails:"
    for email_key in servers_and_threads:
        print email_key
    print # Line break
    email = raw_input("Which email would you like to view the logs of? ")
    if os.path.exists(".emails/%s" % (email)):
        with open("%s/output.log" % (servers_and_threads[email]["Server"].data_path), "r") as log_file:
            logs = log_file.readlines()
        if len(logs) == 0:
            print "Nothing in the log file for %s. Start spamming with it!" % (email)
        else:
            print "Last couple lines of log file for %s:" % (email)
            print # Line break
            for line in logs[-5:]:
                print line
    else:
        print "%s is not an existing spam email." % (email)




# Uses the Command class to set up your command in a predefined format and makes it accessible in memory
command_object = command.Command("log", "View the last couple lines of an email's log file", method)
