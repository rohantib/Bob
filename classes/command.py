class Command():
    list_of_commands = {}
    def __init__(self, keyword, docstring, method):
        self.name = keyword
        self.docstring = docstring
        self.method = method
        Command.list_of_commands[keyword] = self

    @staticmethod
    def run_command(servers_and_threads, command):
        """
        Run a command given the name
        """
        try:
            Command.list_of_commands[command].method(servers_and_threads)
        except KeyError:
            print 'Command "%s" does not exist' % (command)
