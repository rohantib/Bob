from classes import *
from helper_functions import *

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
            email_num = int(raw_input("What is the number of the email you would like to edit the messages of? "))
        except ValueError:
            print "You did not enter a number."
        else:
            if email_num > 0 and email_num <= len(servers_and_threads):
                email = servers_and_threads.keys()[email_num-1]
            else:
                print "Invalid number entered."
                return
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
    print # Line break

command_object = command.Command("edit_messages", "Edit the messages of a certain spam email", " <email>", 1, method) # " <email>" needs space at the beginning to be printed correctly in documentation
