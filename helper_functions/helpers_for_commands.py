"""
Helper functions to be used in commands
"""

def confirmation(query):
    while True:
        inp = raw_input(query).lower()
        if inp == "yes":
            return True
        elif inp == "no":
            return False
        else:
            print "You entered an invalid input. Please enter yes or no."
