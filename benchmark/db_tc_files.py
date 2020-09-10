__version__ = "$Version: 0.0.2"

from typing import Dict
from typing import Union

from .db_register import DBRegister


class DBTCFiles(DBRegister):
    def __init__(self, data_base_name: str):
        super().__init__(data_base_name)

        self._get_dictionary_test()

    def put(self, details: Dict[str, Union[str, int, float]]):
        """put(details: Dict[str, Union[str,int,float]]) -> str

        Write or update the results of the file indicated in the dictionary, in
        the table tc_files.

        PARAMETERS
        ----------
        details: Dict[str, Union[str,int,float]]
            The dictionary should have the following mandatory keys: 'file_name',
            'size_in_bytes' and 'processing_time'.  It might also contain:
            'category' or 'notes'
        """
        self._set_file_name(details['file_name'])

        query = f"SELECT * FROM tc_files WHERE file_name = \'{self._file_name}\'"

        self._put(
            details,
            query,
            self.is_the_file_registered,
            self.__check_differences,
            self.__insert_file,
            self.__update_registered_file
        )

    def __check_differences(
            self,
            query_content: str,
            dict_data: Dict[str, Union[float, int, str]]
    ):
        # Checking differences
        self._cursor.execute(query_content)

        current_record = self._cursor.fetchone()

        headers = (item[0] for item in self._cursor.description)
        data_stored = dict(zip(headers, current_record))
        differences = {}

        for key in dict_data:
            if data_stored[key] != dict_data[key]:
                differences[key] = dict_data[key]

        return differences

    def __insert_file(self, details: Dict[str, Union[str, int, float]]):
        for item in ['file_name', 'size_in_bytes', 'processing_time']:
            if item not in details:
                self._connection.close()
                raise KeyError(
                    f'{item} is a mandatory field to insert in tc_files')

        list_of_column_names = [item for item in details]
        list_of_values = [details[item] for item in details]

        where = self._make_where(list_of_column_names, list_of_values)
        column_names = str(list_of_column_names)[1:-1].replace("'", '')
        str_values = str(list_of_values)[1:-1]

        query = f'SELECT {column_names} FROM tc_files WHERE {where}'
        self._cursor.execute(query)
        records = self._cursor.fetchone()

        if records:
            print(self._file_name)
            print(f"{self._file_name} is already recorded in tc_files.")

        else:
            query = f'INSERT INTO tc_files ({column_names}) VALUES ({str_values})'
            self._cursor.execute(query)

    def __update_registered_file(self, differences: Dict[str, Union[str, int, float]]):
        update_string = []

        for key in differences:
            update_string.append(f'{key} = {differences[key]}')

        update_string = ', '.join(update_string)

        query = f'UPDATE tc_files SET {update_string} WHERE file_name = \'{self._file_name}\''
        self._cursor.execute(query)
