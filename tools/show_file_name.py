__version__ = "$Version: 0.0.3"

from .split_path_file_extension import split_path_file_extension


def show_file_name(full_file_name: str, show_path=False, show_extension=False):
    """Show the file name, and optionally path and extension"""
    path, file_name, extension = split_path_file_extension(full_file_name)

    output = f"{path}{file_name}" if show_path else file_name
    output += extension if show_extension else ""

    return output
