from classes import *
from helper_functions import *
import os

def email_is_valid(email):
    """
    Check if email is valid
    """
    at_pos = email.find("@")
    dot_pos = email.find(".")
    if at_pos == -1 or dot_pos == -1 or dot_pos == len(email) - 1 or dot_pos == at_pos + 1: #Various email conditions
        print "That is not a valid email. Please try again."
        return False
    elif email[at_pos+1:dot_pos] != "gmail":
        print "Currently this spammer only supports Gmail. Please enter a Gmail email address."
        return False
    return True

def method(servers_and_threads):
    print # Line break
    while True:
        email = raw_input("What is your new spam email? ")
        if email_is_valid(email):
            break
    data_path = ".emails/%s" % (email)
    if os.path.exists(data_path):
        print "This email has already been set up as a spam email. If you would like to delete it or edit it, please use those respective commands."
    else:
        os.mkdir(data_path)
        password = raw_input("What is the passwor for this spam email? ")
        with open("%s/password.txt", "w") as password_file:
            password_file.write(password)
        #I am here right now




command_object = command.Command("new_email", "Set up a new spam email", method)
