import os
from commands import *

def list_of_commands():
    commands = []
    #Loops through every python file name without the .py extension
    for module in [file_name[:file_name.find(".py")] for file_name in os.listdir("../commands") if file_name[-2:] == ".py"]:
        print module
        commands.append(getattr(module, "var"))
    print commands
list_of_commands()
