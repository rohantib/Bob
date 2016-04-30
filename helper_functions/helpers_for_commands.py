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

def email_is_valid(email):
    """
    Check if email is a valid one
    """
    at_pos = email.find("@")
    dot_pos = email.find(".")
    if at_pos == -1 or dot_pos == -1 or dot_pos == len(email) - 1 or dot_pos == at_pos + 1: #Various email format checks
        return False
    return True
