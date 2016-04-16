from classes import *
from helper_functions import *

def method(self, servers_and_threads):
    commands_list = helpers_for_commands.get_commands_list()
    for key in commands_list:
        print '"%s" - %s' % (key, commands_list[key].docstring)

command_object = command.Command("help", "Lists available commands", method)
