from classes import *
from helper_functions import *
import os

#Helper functions
def get_email():
    while True:
        email = raw_input("What is your new spam email? ")
        if helpers_for_commands.email_is_valid(email) == True:
            break
        else:
            print "That is not a valid email. Please try again."
    return email

def get_and_write_password(data_path):
    password = raw_input("What is the password for this spam email? ")
    with open("%s/.password.txt" % (data_path), "w") as password_file:
        password_file.write(password)

def get_and_write_message(data_path):
    message = raw_input("Enter one message for this spam email to send to targets. Use \\n for any linebreaks. Hit ENTER when you are done. Do not worry if you make a mistake or anything, you can always add, edit, and delete messages later. \n")
    with open("%s/.messages.txt" % (data_path), "w") as messages_file:
        messages_file.write(message)

def get_and_write_target(data_path):
    while True:
        print "Enter one target email for this spam email. You can always edit this later."
        target = raw_input("Enter target: ")
        if helpers_for_commands.email_is_valid(target):
            break
    with open("%s/.targets.txt" % (data_path), "w") as targets_file:
        targets_file.write(target)

#Main method
def method(servers_and_threads, arguments):
    print # Line break
    email = get_email()
    data_path = ".emails/%s" % (email)
    if os.path.exists(data_path):
        print "This email has already been set up as a spam email. If you would like to delete it or edit it, please use those respective commands."
    else:
        os.mkdir(data_path)
        get_and_write_password(data_path)
        print # Line break
        get_and_write_message(data_path)
        print # Line break
        get_and_write_target(data_path)
        #Make messages_sent file
        with open("%s/.messages_sent.txt" % (data_path), "w") as messages_sent_file:
            messages_sent_file.write("0")
        #Make log file
        with open("%s/output.log" % (data_path), "w") as log_file:
            log_file.write("")
        #Set up server and thread
        email_server = server.Server(email)
        servers_and_threads[email] = {"Server": email_server, "Thread": server.ServerThread(email_server)}
        print #Line break
        #Output to user
        print 'Ok! %s is now ready to spam, provided all credentials were entered correctly. If any error was made, you can edit the email with the "edit_email" command, or you can set it up again by deleting and setting it up again.' % (email)



command_object = command.Command("add_email", "Set up an additional spam email", "", 0, method)
