from classes import *

def method(servers_and_threads, arguments): #Why do n't I need self?
    commands = command.Command.list_of_commands
    print #Line break
    for key in commands:
        print '"%s%s" - %s' % (key, commands[key].args_docstring, commands[key].docstring)
    print #Line break

command_object = command.Command("help", "Lists available commands", "", 0, method)
