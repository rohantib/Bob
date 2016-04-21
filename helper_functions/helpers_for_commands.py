"""
Helper functions to be used in commands
"""

def confirmation(inp):
    inp = inp.lower()
    if inp == "yes":
        return True
    return False
