# TODO for all commands: don't use os.path.exists to check if email exists, use try-except when pulling from dictionary
import os
# Magical one-liner that sets __all__ variable to all files in directory without the dot extension, excluding __init__
__all__ = [file_name[:file_name.find(".py")] for file_name in os.listdir("commands") if file_name[-3:] == ".py" and file_name != "__init__.py"]
