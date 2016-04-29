from classes import *
from helper_functions import *

def change_email(email):
    pass
def change_pass(email):
    pass

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
                change_email(email)
            elif option == "password":
                change_pass(email)
            else:
                print 'Invalid option selected. Please enter either "email" or "password" as your choice.'
    else:
        print "%s does not exist as an available spam email." % (email)
    print # Line break


command_object = command.Command("edit_credentials", "Edit the credentials of a spam email", method)
