from classes import *
from helper_functions import *

def method(servers_and_threads, arguments):
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
            email_num = int(raw_input("What is the number of the email would you like to edit the messages of? "))
        except ValueError:
            print "You did not enter a number."
        else:
            if email_num > 0 and email_num <= len(servers_and_threads):
                email = servers_and_threads.keys()[email_num-1]
            else:
                print "Invalid number entered."
                return
    server = servers_and_threads[email]["Server"]
    print "Email: %s" % (server.email)
    print "Password: %s" % (server.password)
    print "Status: %s" % (server.status)
    print "Total messages sent: %s" % (server.messages_sent)
    print "Targets: %s" % (", ".join(server.targets))
    # Prints messages - linebreaks may be present so each is printed on a separate line
    print "Messages:"
    for index, message in enumerate(server.messages):
        print "%d - %s" % (index, message)
    print # Line break


# Uses the Command class to set up your command in a predefined format and makes it accessible in memory
command_object = command.Command("data", "Get all the data of a specified email", " <email>", 1, method) # " <email>" needs space at the beginning to be printed correctly in documentation
