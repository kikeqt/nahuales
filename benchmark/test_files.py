__version__ = "$Version: 1.0.4"

import json

from .files import Files
from tools import Integer2Bytes


class Test_Files(object):
    __current_file = 0
    __test_files = []
    __truncated_path = "benchmark/truncated_folder/"
    __my_test_files = ()

    def __init__(self):
        self.__load_from_JSON()

        for item in self.__my_test_files:
            self.__test_files.append(Files(**item))

        self.__truncate_files()

    def __load_from_JSON(self):
        with open('benchmark/config_benchmark.json', 'r') as file:
            self.__my_test_files = file.read()

        self.__my_test_files = json.loads(self.__my_test_files)
        self.__my_test_files = tuple(self.__my_test_files)

    def __truncate_files(self):
        for item in range(len(self.__test_files)):
            self.__test_files[item].truncated_path = self.__truncated_path
            self.__test_files[item].generate_truncated_file()

    def get_files_iterative(self):
        for item in self.__test_files:
            yield item

    def get_keys_iterative(self):
        integer_2_bytes = Integer2Bytes()

        for key in range(256):
            yield integer_2_bytes.integer_2_bytes(key)
