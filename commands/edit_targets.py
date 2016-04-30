from classes import *
from helper_functions import *
import os

# Helper functions
def add_target(email, servers_and_threads):
    while True:
        new_target = raw_input("What is the new target you would like to add? ")
        if helpers_for_commands.email_is_valid(new_target):
            break
        else:
            print "That is not a valid email. Please try again."
    servers_and_threads[email]["Server"].targets.append(new_target)
    print "Successfully added %s as a target for spam email %s." % (new_target, email)

def del_target(email, servers_and_threads):
    while True:
        try:
            target_num = int(raw_input("What is the number of the target you would like to delete? "))
        except ValueError:
            print "Please enter a number."
        else:
            if target_num > 0 and target_num <= len(servers_and_threads[email]["Server"].targets): # Checks if number entered is in correct range
                break
            else:
                print "Please enter a valid number that corresponds to a target above."
    target_index = target_num - 1 # Makes it zero-based index number
    target = servers_and_threads[email]["Server"].targets[target_index]
    del servers_and_threads[email]["Server"].targets[target_index]
    print "Successfully deleted target %s from spam email %s." % (target, email)

def change_target(email, servers_and_threads):
    while True:
        try:
            target_num = int(raw_input("What is the number of the target you would like to change? "))
        except ValueError:
            print "Please enter a number."
        else:
            if target_num > 0 and target_num <= len(servers_and_threads[email]["Server"].targets): # Checks if number entered is in correct range
                break
            else:
                print "Please enter a valid number that corresponds to a target above."
    target_index = target_num - 1 # Makes it zero-based index number
    target = servers_and_threads[email]["Server"].targets[target_index]
    while True:
        new_email = raw_input("What is the new target you would like to replace %s with? " % (target))
        if helpers_for_commands.email_is_valid(new_email):
            break
        else:
            print "That is not a valid email. Please try again."
    servers_and_threads[email]["Server"].targets[target_index] = new_target
    print "Successfully replaced target %s from spam email %s." % (target, new_target)

def write_targets_to_file(email, servers_and_threads):
    with open("%s/.targets.txt" % (servers_and_threads[email]["Server"].data_path), "w") as targets_file:
        targets_file.write('\n'.join(servers_and_threads[email]["Server"].targets))

def method(servers_and_threads):
    print # Line break
    print "Existing emails:"
    for email_key in servers_and_threads:
        print email_key
    print # Line break
    email = raw_input("Which email would you like to edit the targets of? ")
    if os.path.exists(".emails/%s" % (email)):
        print "Current targets for this email are:"
        for index, target in enumerate(servers_and_threads[email]["Server"].targets):
            print "[%d] %s" % (index+1, target)
        print # Line break
        # Get action (add, delete, or change) from user
        while True:
            action = raw_input("Would you like to add, change, or delete one of these targets? ").lower()
            if action == "add":
                add_target(email, servers_and_threads)
                break
            elif action == "delete":
                del_target(email, servers_and_threads)
                break
            elif action == "change":
                change_target(email, servers_and_threads)
                break
            else:
                print 'That is an invalid option. Please enter either "add", "change", or "delete".'
        # Writes the edits to storage
        write_targets_to_file(email, servers_and_threads)
    else:
        print "%s does not exist as an available spam email." % (email)

command_object = command.Command("edit_targets", "Edit the targets of a certain spam email", method)
