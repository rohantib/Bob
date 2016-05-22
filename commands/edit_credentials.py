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
    print "The current credentials are: \n"
    print "Email: %s" % (servers_and_threads[email]["Server"].email)
    print "Password: %s" % (servers_and_threads[email]["Server"].password)
    print # Line break
    while True:
        option = raw_input("Would you like to change the email or the password? ").lower()
        if option == "email":
            change_email(email, servers_and_threads)
            break
        elif option == "password":
            change_pass(email, servers_and_threads)
            break
        else:
            print 'Invalid option selected. Please enter either "email" or "password" as your choice.'
    print # Line break


command_object = command.Command("edit_credentials", "Edit the credentials of a spam email", " <email>", 1, method) # " <email>" needs space at the beginning to be printed correctly in documentation
