# Spambot
A nice little bot that spams people you don't like.
Currently in development, developing a terminal interface and multithreading capabilities.
Not functional as of now.

I apologize for the illegibility of parts of the code. In the process of making a simple framework
to make writing new commands a very simple process that anyone can do, I had to cleverly and illegibly mess
with Python to avoid many difficult issues such as an infinite loop of module imports.

The documentation for writing new commands, if you are interested in doing so, is contained in template.txt within the commands folder. Be careful when making new commands, though, as if any error exists in the code, the spammer will be broken and will throw an error at startup.

NOTE: There is a framework set up to make your own commands (generally shortcuts for other commands),
along with documentation, but nothing of the like is set up for the classes or helper_functions package.
Any new files in helper_functions or classes made by you will be ignored by the code unless you include it in the code.
DO NOT CHANGE ANY PREINSTALLED FILES OR RISK BREAKING THE SPAMMER!

This spammer currently only works with Gmail accounts. Support for Yahoo will be coming soon.

# Dependencies
This program is written in Python 2.7, and therefore requires that you have a Python 2.7 interpreter installed. To install Python, go to https://www.python.org/downloads/release/python-2711/ in your web browser, download the appropriate file for your operating system, and run the installer. For Linux, Python should be preinstalled. If not, it is available in the default repositories of your package manager.

To run the program, open a terminal, change your working directory to the directory of the spammer, and type './run.sh' to run it. If this doesn't work for some reason, just run main.py with the Python interpreter manually. The program does not modify any files existing outside its own directory.
