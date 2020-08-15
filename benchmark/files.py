__version__ = "$Version: 0.0.1"

from os import mkdir
from os.path import exists
from os.path import getsize
from os.path import split as split_path
from os.path import splitext
import requests

from tools import split_path_file_extension


class Files(object):
    __path = ""
    __file_name = ""
    __extension = ""
    __full_path = ""
    __truncated_path = ""
    __category = ""

    def __init__(self, file_location: str, category: str = "", url_file: str = ""):
        path, file_name, extension = split_path_file_extension(file_location)

        self.__path = path
        self.__file_name = file_name
        self.__extension = extension
        self.__full_path = file_location
        self.__category = category

        if not exists(file_location):
            print("Missing file: I need download the file " +
                  "{file_name}{extension}")
            resource = requests.get(url_file)

            with open(f'{file_location}', 'wb') as outfile:
                outfile.write(resource.content)

            print('Download completed')

    @property
    def get_path(self):
        return self.__path

    @property
    def get_file_name(self):
        return self.__file_name

    @property
    def get_extension(self):
        return self.__extension

    @property
    def get_file_name_with_extension(self):
        return self.__file_name + self.__extension

    @property
    def get_full_file_name(self):
        return self.__full_path

    @property
    def get_category(self):
        return self.__category

    @property
    def get_size_in_bytes(self):
        return getsize(self.__full_path)

    @property
    def get_size_in_bits(self):
        return self.get_size_in_bytes * 8

    @property
    def truncated_path(self):
        return self.__truncated_path

    @truncated_path.setter
    def truncated_path(self, path: str):
        if not exists(path):
            mkdir(path)

        self.__truncated_path = path

    @property
    def get_truncated_file(self):
        return f'{self.__truncated_path}{self.get_file_name_with_extension}'

    def generate_truncated_file(self, maximun_size: int = 125000):
        if not exists(self.get_truncated_file):
            content = b''

            with open(self.__full_path, 'rb') as file:
                content = file.read()

            content = content[:maximun_size]

            print(f'truncated file: {self.get_truncated_file}')
            with open(self.get_truncated_file, 'wb') as file:
                file.write(content)
