from classes import *

def method(servers_and_threads, arguments):
    print #Line break
    spamming_emails = []
    for email in servers_and_threads:
        if servers_and_threads[email]["Server"].currently_spamming == True:
            spamming_emails.append(email)
    if len(spamming_emails) == 0:
        print "No emails are currently spamming."
    else:
        print "Emails that are currently spamming:"
        print #Line break
        for email in spamming_emails:
            print email
    print #Line break


command_object = command.Command("currently_spamming", "Lists all emails that are currently spamming", "", 0, method)
