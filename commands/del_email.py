from classes import *
from helper_functions import *
import shutil

def method(servers_and_threads, arguments):
    # TODO: move to helper function list_emails and email_exists
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
            email_num = int(raw_input("What is the number of the email you would like to delete? "))
        except ValueError:
            print "You did not enter a number."
        else:
            if email_num > 0 and email_num <= len(servers_and_threads):
                email = servers_and_threads.keys()[email_num-1]
            else:
                print "Invalid number entered."
                return
    # Remove email from memory
    del servers_and_threads[email]
    # Remove email from storage
    shutil.rmtree(".emails/%s" % (email))
    print "Successfully deleted %s" % (email)
    print # Line break


command_object = command.Command("del_email", "Remove a spam email", " <email>", 1, method) # " <email>" needs space at the beginning to be printed correctly in documentation
