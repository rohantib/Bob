import os
"""
This is the code for initially setting up the spammer. Since it is initial setup, all helper functions are included
in this file, and nothing is imported from the outside except built-in Python modules.
"""
#Helper functions
def email_is_valid(email):
    """
    Check if email is a valid one
    """
    at_pos = email.find("@")
    dot_pos = email.find(".")
    if at_pos == -1 or dot_pos == -1 or dot_pos == len(email) - 1 or dot_pos == at_pos + 1: #Various email format checks
        return False
    return True

def get_email():
    while True:
        email = raw_input("What is your spam email? ")
        if email_is_valid(email) == True:
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

def setup():
    print "Hi! I'm Bob, a lovely little assistant for you to get back at anyone you don't like - the techy way."
    print "Give me an email to spam with, and I'll wreak havoc in their inbox!"
    print "Before you start using me, I need a spam email to start with. I will guide you through setting up everything right now so that we will be spamming ASAP!"
    print "DO NOT GIVE ME YOUR ACTUAL EMAIL! Provide a spam email you have made specifically for me."
    print "You can easily make a new spam email on Gmail by going to the webpage, clicking \"Create an Email\", and entering a random name, username, password, birthday, and gender."
    print "Once you have done so, follow the instructions to add it so that I can use it."
    print # Line break
    # Make .emails directory
    os.mkdir(".emails")
    # Get the email address
    email = get_email()
    # Make the directory for the spam email
    data_path = ".emails/%s" % (email)
    os.mkdir(data_path)
    # Get the password for the email
    get_and_write_password(data_path)
    print # Line break
    # Get a message to start with for the email
    get_and_write_message(data_path)
    print # Line break
    # Get a target to start with for the email
    get_and_write_target(data_path)
    #Make messages_sent file
    with open("%s/.messages_sent.txt" % (data_path), "w") as messages_sent_file:
        messages_sent_file.write("0")
    #Make log file
    with open("%s/output.log" % (data_path), "w") as log_file:
        log_file.write("")
    print # Line break
    # Output to user
    print "That's it! I'm now ready to get going and start spamming. If you made any errors in setting up the email, you can always fix it later."
    print "To get started, type \"help\" for a list of commands, and then type in whatever command you wish to run."
