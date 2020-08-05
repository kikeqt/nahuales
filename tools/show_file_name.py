__version__ = "$Version: 0.0.1"

from .split_path_file_extension import split_path_file_extension


def show_file_name(full_file_name: str, show_path=False, show_extension=False):
    """Show the filename, and optionaly path and extension"""
    path, file_name, extension = split_path_file_extension(full_file_name)
    
    output = f"{path}{filename}" if show_path else file_name
    output += extension if show_extension else ""
    return output
