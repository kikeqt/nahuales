__version__ = "$Version: 0.0.1"

from .db import DataBase


class DBRegister(DataBase):
    _file_name: str

    def __init__(self, data_base_name: str):
        super().__init__(data_base_name)

    def _set_file_name(self, file_name: str):
        self._file_name = file_name

    def is_the_file_registered(self, file_name: str = ''):
        """is_the_file_registered(file_name: str) -> bool

        Answer the question, are there file performance results?

        PARAMETERS
        ----------
        file_name: str
            Name of analyzed file
        """
        if file_name == '':
            file_name = self._file_name

        query = f"SELECT COUNT(id_file) FROM tc_files WHERE file_name = '{file_name}'"

        return self._query_boolean(query)
