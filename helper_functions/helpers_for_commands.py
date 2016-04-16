import os, importlib

def get_commands_list():
    """
    Helper function to obtain list of commands, used in this script and in others
    """
    commands = {}
    for file_name in [mod for mod in os.listdir("commands") if mod[-3:] == ".py"]:
        module = importlib.import_module("commands.%s" % (file_name))
        commands[module.command_object.name.lower()] = module.command_object
    return commands

commands = get_commands_list()

def run_command(command, servers_and_threads):
    """
    Using get_commands_list, runs a command given the name
    """
    try:
        commands[command](servers_and_threads)
    except KeyError:
        print 'Command "%s" does not exist' % (command)

def yes_no(inp):
    inp = inp.lower()
    if inp == "yes":
        return True
    return False
