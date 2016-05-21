"""
Contains class Command as a template to make new commands, along with a static function for other scripts,
especially the main script, to run commands.
"""

#How does this still work?
class Command():
    list_of_commands = {}
    def __init__(self, keyword, docstring, args_docstring, max_args, method):
        self.name = keyword
        self.docstring = docstring
        self.args_docstring = args_docstring
        self.max_args = max_args
        self.method = method
        #Adds the newly initialized command object to a static list in the Command class to be accessed by the static method run_command
        Command.list_of_commands[keyword] = self

    @staticmethod
    def run_command(servers_and_threads, user_input_raw):
        """
        Run a command given the user input
        """
        # Gets all data into list data type by separating at spaces, then removes first index as that is the name of the command.
        arguments = user_input_raw.strip().split(" ")
        command = arguments.pop(0)
        try:
            command_object = Command.list_of_commands[command]
            if len(arguments) <= command_object.max_args:
                command_object.method(servers_and_threads, arguments)
            else:
                print 'Invalid usage of "%s". Please check how to use the command with "help".' % (command)
        except KeyError:
            print 'Command "%s" does not exist' % (command)
