from classes import *
from helper_functions import *

def method(servers_and_threads): #Why don't I need self?
    commands = command.Command.list_of_commands
    for key in commands:
        print '"%s" - %s' % (key, commands[key].docstring)

command_object = command.Command("help", "Lists available commands", method)
