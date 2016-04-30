from classes import *
from helper_functions import *
import os

# Helper functions
def add_message(email, servers_and_threads):
    new_message = raw_input("What is the new message you would like to add? Use \\n for linebreaks; if you hit \"Enter\", whatever you have typed will be entered as the new message. \n")
    servers_and_threads[email]["Server"].messages.append(new_message)
    print "Successfully added the message for spam email %s." % (email)

def del_message(email, servers_and_threads):
    while True:
        try:
            message_num = int(raw_input("What is the number of the message you would like to delete? "))
        except ValueError:
            print "Please enter a number."
        else:
            if message_num > 0 and message_num <= len(servers_and_threads[email]["Server"].messages): # Checks if number entered is in correct range
                break
            else:
                print "Please enter a valid number that corresponds to a message above."
    message_index = message_num - 1 # Makes it zero-based index number
    del servers_and_threads[email]["Server"].messages[message_index]
    print "Successfully deleted message #%d from spam email %s." % (message_num, email)

def change_message(email, servers_and_threads):
    while True:
        try:
            message_num = int(raw_input("What is the number of the message you would like to change? "))
        except ValueError:
            print "Please enter a number."
        else:
            if message_num > 0 and message_num <= len(servers_and_threads[email]["Server"].messages): # Checks if number entered is in correct range
                break
            else:
                print "Please enter a valid number that corresponds to a message above."
    message_index = message_num - 1 # Makes it zero-based index number
    new_message = raw_input("What is the new message to replace message #%d with? Use \\n for linebreaks; if you hit \"Enter\", whatever you have typed will be entered as the new message. \n" % (message_num))
    servers_and_threads[email]["Server"].messages[message_index] = new_message
    print "Successfully changed message #%d from spam email %s." % (message_num, email)

def write_messages_to_file(email, servers_and_threads):
    # Escape all linebreaks in the messages
    one_line_messages = [message.replace("\n", "\\n") for message in servers_and_threads[email]["Server"].messages]
    with open("%s/.messages.txt" % (servers_and_threads[email]["Server"].data_path), "w") as messages_file:
        messages_file.write('\n'.join(one_line_messages))

def method(servers_and_threads):
    print # Line break
    print "Existing emails:"
    for email_key in servers_and_threads:
        print email_key
    print # Line break
    email = raw_input("Which email would you like to edit the messages of? ")
    if os.path.exists(".emails/%s" % (email)):
        print "Current messages for this email are:"
        for index, message in enumerate(servers_and_threads[email]["Server"].messages):
            print "[%d] \n%s" % (index+1, message)
        print # Line break
        # Get action (add, delete, or change) from user
        while True:
            action = raw_input("Would you like to add, change, or delete one of these messages? ").lower()
            if action == "add":
                add_message(email, servers_and_threads)
                break
            elif action == "delete":
                del_message(email, servers_and_threads)
                break
            elif action == "change":
                change_message(email, servers_and_threads)
                break
            else:
                print 'That is an invalid option. Please enter either "add", "change", or "delete".'
        # Writes the edits to storage
        write_messages_to_file(email, servers_and_threads)
    else:
        print "%s does not exist as an available spam email." % (email)

command_object = command.Command("edit_messages", "Edit the messages of a certain spam email", method)
