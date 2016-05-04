# Bob
A nice little bot that spams people you don't like.

Now fully functional with a very primitive terminal interface! Upgrades to the terminal interface will be coming soon, as it is
quite irritating to use currently. I do not think I will be making a graphical interface for Bob, though. Sorry!
There are also a couple errors that could very likely occur that do not have a try-except set up yet. That will be definitely set up soon.

Certain parts are still untested, so there may be bugs. Please do report them in Github's Issues section if you use this and find a bug.

I apologize for the illegibility of parts of the code. In the process of making a simple framework
to make writing new commands a very simple process that anyone can do, I had to cleverly and illegibly mess
with Python to avoid many difficult issues such as an infinite loop of module imports. This is also my first larger-sized project,
and I am just learning good coding practices.

The documentation for writing new commands, if you are interested in doing so, is contained in commands/template.txt. Be careful when making new commands, though, as if any error exists in the code, the spammer will be broken and will throw an error at startup.

NOTE: There is a framework set up to make your own commands (generally shortcuts for other commands),
along with documentation, but nothing of the like is set up for the classes or helper_functions package.
Any new files in helper_functions or classes made by you will be ignored by the code unless you include it in the code,
and if there is an error in your new code, the spammer will throw an error at startup.
DO NOT CHANGE ANY EXISTING FILES OR RISK BREAKING THE SPAMMER!

This spammer currently only works with Gmail accounts. Support for Yahoo and other emails will be coming soon.

# Installation and Dependencies
This program is written in Python 2.7, and therefore requires that you have a Python 2.7 interpreter installed. To install Python, go to https://www.python.org/downloads/release/python-2711/ in your web browser, download the appropriate file for your operating system, and run the installer. For Linux, Python should be preinstalled. If not, it is available in the default repositories of your package manager.

To install Bob, click Download Zip on the Github repository page, then extract the zip to wherever you want it to be.

To run the program, open a terminal, change your working directory to Bob's directory, and type 'python main.py' to run it. The program does not modify any files existing outside its own directory.
