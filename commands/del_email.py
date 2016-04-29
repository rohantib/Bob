from classes import *
from helper_functions import *
import os, shutil

def method(servers_and_threads):
    # TODO: move to helper function list_emails and email_exists
    print # Line break
    print "Existing emails:"
    for email in servers_and_threads:
        print email
    print # Line break
    email = raw_input("What is the email you would like to delete? ")
    if os.path.exists(".emails/%s" % (email)):
        shutil.rmtree(".emails/%s" % (email))
        del servers_and_threads[email]
        print "Successfully deleted %s" % (email)
    else:
        print "%s has not been set up or has already been deleted." % (email)
    print # Line break


command_object = command.Command("del_email", "Remove a spam email", method)
