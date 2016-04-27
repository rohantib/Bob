from classes import *
from helper_functions import *
import os
#How do these helper functions still work?

#Helper functions
def email_is_valid(email):
    """
    Check if email is valid
    """
    at_pos = email.find("@")
    dot_pos = email.find(".")
    if at_pos == -1 or dot_pos == -1 or dot_pos == len(email) - 1 or dot_pos == at_pos + 1: #Various email conditions
        print "That is not a valid email. Please try again."
        return False
    return True

def get_email():
    while True:
        email = raw_input("What is your new spam email? ")
        if email_is_valid(email):
            break
    return email

def get_and_write_password():
    password = raw_input("What is the password for this spam email? ")
    with open("%s/.password.txt" % (data_path), "w") as password_file:
        password_file.write(password)

def get_and_write_message():
    message = raw_input("Enter one message for this spam email to send to targets. Use //n for any linebreaks. Hit ENTER when you are done. Do not worry if you make a mistake or anything, you can always add, edit, and delete messages later. \n")
    with open("%s/.messages.txt" % (data_path), "w") as messages_file:
        messages_file.write(message)

def get_and_write_target():
    while True:
        print "Enter one target email for this spam email. You can always edit this later"
        target = raw_input("Enter target: ")
        if email_is_valid(target):
            break
    with open("%s/.targets.txt" % (data_path), "w") as targets_file:
        targets_file.write(target)

#Main method
def method(servers_and_threads):
    print "Setup for a new email will begin. If you quit during setup, the spammer will be broken, as it has not been made to handle that yet."
    email = get_email
    data_path = ".emails/%s" % (email)
    if os.path.exists(data_path):
        print "This email has already been set up as a spam email. If you would like to delete it or edit it, please use those respective commands."
    else:
        os.mkdir(data_path)
        get_and_write_password()
        print # Line break
        get_and_write_message()
        print # Line break
        get_and_write_target()
        #Make messages_sent file
        with open("%s/.messages_sent.txt" % (data_path), "w") as messages_sent_file:
            messages_sent_file.write("0")
        #Make log file
        with open("%s/output.log" % (data_path), "w") as log_file:
            log_file.write("")
        #Set up server and thread
        email_server = server.Server(email)
        servers_and_threads[email] = {"Server": email_server, "Thread": server.ServerThread(email_server)

        print # Line break
        #Output to user
        print 'Ok! %s is now ready to spam, provided all credentials were entered correctly. If any error was made, you can edit the email with the "edit_email" command, or you can set it up again by deleting and seteting it up again.' % (email)



command_object = command.Command("add_email", "Set up an additional spam email", method)
