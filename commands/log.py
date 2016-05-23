from classes import *
from helper_functions import *

def method(servers_and_threads):
    print # Line break
    # Argument Check
    if len(arguments) != 0:
        email = arguments[0]
        if not helpers_for_commands.email_is_valid(email):
            print "You did not enter a valid email."
            return
        elif email not in servers_and_threads.keys():
            print "Email %s is not an existing email." % (email)
            return
    else:
        # Get email if no email is supplied as argument
        print "Existing emails:"
        for email_index, email in enumerate(servers_and_threads.keys()):
            print "[%d] - %s" % (email_index+1, email)
        print # Line break
        try:
            email_num = int(raw_input("What is the number of the email you would like to view the log of? "))
        except ValueError:
            print "You did not enter a number."
        else:
            if email_num > 0 and email_num <= len(servers_and_threads):
                email = servers_and_threads.keys()[email_num-1]
            else:
                print "Invalid number entered."
                return
    with open("%s/output.log" % (servers_and_threads[email]["Server"].data_path), "r") as log_file:
        logs = log_file.readlines()
    if len(logs) == 0:
        print "Nothing in the log file for %s. Start spamming with it!" % (email)
    else:
        print "Last 5 lines of log file for %s:" % (email)
        print # Line break
        for line in logs[-5:]:
            print line
    print # Line break


# Uses the Command class to set up your command in a predefined format and makes it accessible in memory
command_object = command.Command("log", "View the last couple lines of an email's log file", " <email>", 1, method) # " <email>" needs space at the end to be printed correctly in documentation
