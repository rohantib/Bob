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
            email_num = int(raw_input("What is the number of the email you would like to spam with? "))
        except ValueError:
            print "You did not enter a number."
        else:
            if email_num > 0 and email_num <= len(servers_and_threads):
                email = servers_and_threads.keys()[email_num-1]
            else:
                print "Invalid number entered."
                return
    if servers_and_threads[email]["Server"].currently_spamming == True:
        print "%s is already spamming or threw an error. Look in the log file at %s/output.log if an error was thrown, as the same error may occur again. If the error does not cease, delete and set up %s again. Spamming with %s will restart." % (email, servers_and_threads[email]["Server"].data_path, email, email)
        #Exits old thread
        servers_and_threads[email]["Thread"].exitFlag = 1
        #Initialize new thread object to replace old one, which will quit after the time.sleep is over and the exit flag is checked
        servers_and_threads[email]["Thread"] = server.ServerThread(servers_and_threads[email]["Server"])
    servers_and_threads[email]["Thread"].start()
    print "Spamming with %s..." % (email)
    print #Line break

command_object = command.Command("spam", "Begin spamming with a specific email", " <email>", 1, method) # " <email>" needs space at the beginning to be printed correctly in documentation
