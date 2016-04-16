import os
__all__ = [file_name[:file_name.find(".py")] for file_name in os.listdir("classes") if file_name[-3:] == ".py" and file_name != "__init__.py"]
