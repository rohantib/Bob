from classes import *
from helper_functions import *

def method(servers_and_threads):
    currently_spamming_emails = []
    for email in servers_and_threads:
        if servers_and_threads[email]["Server"].currently_spamming == True:
            currently_spamming_emails.append(email)
    if len(currently_spamming_emails) == 0:
        print "No emails are currently spamming."
    else:
        print "Which email would you like to halt spamming with? \n"
        for email in currently_spamming_emails:
            print email
        print #Line Break
        email = raw_input("Enter email: ").strip()
        print #Line break
        try:
            if servers_and_threads[email]["Server"].currently_spamming == False:
                print "%s is not currently spamming." % (email)
            else:
                servers_and_threads[email]["Thread"].exitFlag = 1
                #Initialize new thread object to replace old one, which will quit after the time.sleep is over and the exit flag is checked
                servers_and_threads[email]["Thread"] = server.ServerThread(servers_and_threads[email]["Server"])
                print "Spamming with %s has been stopped." % (email)
        except KeyError:
            print "Email %s is not set up as a spam email yet." % (email)

command_object = command.Command("stop_spamming", "Stop spamming with a specified email", method)
