from classes import *
from helper_functions import *
import os

#Helpers for the command
def change_email(email, servers_and_threads):
    while True:
        new_email = raw_input("What is the new email? ")
        if helpers_for_commands.email_is_valid(new_email):
            break
        else:
            print "That is not a valid email. Please try again."
    os.rename(".emails/%s" % (email), ".emails/%s" % (new_email))
    servers_and_threads[new_email] = servers_and_threads.pop(email)
    print "Successfully changed email %s to %s" % (email, new_email)

def change_pass(email, servers_and_threads):
    new_pass = raw_input("What is the new password? ")
    with open("%s/.password.txt" % (servers_and_threads[email]["Server"].data_path), "w") as pass_file:
        pass_file.write(new_pass)
    servers_and_threads[email]["Server"].password = new_pass

def method(servers_and_threads):
    print # Line break
    print "Existing emails:"
    for email in servers_and_threads:
        print email
    print # Line break
    print "Which email would you like to edit the credentials of?"
    if os.path.exists(".emails/%s" % (email)):
        print "The current credentials are: \n"
        print "Email: %s" % (servers_and_threads[email]["Server"].email)
        print "Password: %s" % (servers_and_threads[email]["Server"].password)
        while True:
            option = raw_input("Would you like to change the email or the password? ").lower()
            if option == "email":
                change_email(email, servers_and_threads)
            elif option == "password":
                change_pass(email, servers_and_threads)
            else:
                print 'Invalid option selected. Please enter either "email" or "password" as your choice.'
    else:
        print "%s does not exist as an available spam email." % (email)
    print # Line break


command_object = command.Command("edit_credentials", "Edit the credentials of a spam email", method)
