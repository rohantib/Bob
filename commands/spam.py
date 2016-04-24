from classes import *
from helper_functions import *

def method(servers_and_threads):
    print "Which email would you like to spam with? \n"
    for email in servers_and_threads:
        print email
    print #Line Break
    email = raw_input("Enter email: ").strip()
    try:
        if servers_and_threads[email]["Server"].currently_spamming == True:
            print "%s is already spamming or threw an error. Look in the log file at %s/output.log if an error was thrown, as the same error may occur again. If the error does not cease, delete and set up %s again. Spamming with %s will restart." % (email, servers_and_threads[email]["Server"].data_path, email, email)
            #Exits old thread
            servers_and_threads[email]["Thread"].exitFlag = 1
            #Initialize new thread object to replace old one, which will quit after the time.sleep is over and the exit flag is checked
            servers_and_threads[email]["Thread"] = server.ServerThread(servers_and_threads[email]["Server"])
        servers_and_threads[email]["Thread"].start()
        print "Spamming with %s..." % (email)
    except KeyError:
        print "Email %s is not set up." % (email)
    print #Line break

command_object = command.Command("spam", "Begin spamming with a specific email", method)
