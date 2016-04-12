import os
__all__ = [file_name[:file_name.find(".py")] for file_name in os.listdir("classes")]
