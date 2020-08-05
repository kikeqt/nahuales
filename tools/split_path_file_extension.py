__version__ = "$Version: 1.0.0"

from os.path import split as split_path
from os.path import splitext

def split_path_file_extension(full_path):
    path, file = split_path(full_path)
    file, extension = splitext(file)
    return path, file, extension
