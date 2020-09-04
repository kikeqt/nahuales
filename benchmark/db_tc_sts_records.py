__version__ = "$Version: 0.0.1"

import sqlite3
from typing import List
from typing import Dict
from typing import Union

from .db import DataBase
from .db_tc_files import DBTCFiles
from .sts_value import STSValue


class DBTCSTSRecords(DataBase):
    _list_of_sts_columns: List[str]
    __tc_files: DBTCFiles
    __id_file: int
    __id_test: int
    __id_result: int

    def __init__(self, data_base_name: str):
        super().__init__(data_base_name)

        self._list_of_sts_columns = [
            'id_file',
            'id_test',
            'id_result',
            'p_value',
            'assignment',
            'category',
        ]

        self._get_dictionary_test()

    def exist(self, file_name: str):
        """exist(file_name: str) -> bool

        Answer the question, are there STS file records?

        PARAMETERS
        ----------
        file_name: str
            Name of analyzed file
        """
        id_file = self._get_id_file(file_name)

        query = f"SELECT COUNT(id_file) FROM tc_sts_records WHERE id_file = '{id_file}'"
        query += f" AND id_test = {self.__id_test} AND id_result = {self.__id_result}"
        return self._query_boolean(query)

    def _check_differences(
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

    def put(self, file_name: str, details: Dict[str, List[STSValue]]):
        """put(file_name: str, results: Dict[str, List[STS_Value]]) -> bool

        Register the file name in the catalog and saves or replaces the STS records

        PARAMETERS
        ----------
        file_name: str
            Name of analyzed file

        details: Dict[str, List[STSValue]]
            Dictionary with the records to put
        """
        if not self.is_the_file_registered(file_name):
            raise KeyError(
                f'You must record the file first, before the STS results.')

        values_dictionary_list = self._decode_sts_results(file_name, details)

        for values in values_dictionary_list:
            self.__id_test = values['id_test']
            self.__id_result = values['id_result']

            query = f"SELECT * FROM tc_sts_records WHERE id_file = \'{self.__id_file}\'"
            query += f" AND id_test = {self.__id_test} AND id_result = {self.__id_result}"

            self._put(
                file_name,
                values,
                query,
                self.exist,
                self._check_differences,
                self._insert,
                self._update
            )

    def _decode_sts_results(self, file_name: str, details: Dict[str, List[STSValue]]):
        self.__id_file = self._get_id_file(file_name)

        values_dictionary_list = []

        for key_test in details:
            id_test = self._dictionary_of_test[key_test]

            for id_result in range(len(details[key_test])):
                sts_value = details[key_test][id_result]

                p_value = sts_value[0]
                assignment = 1 if sts_value[1] == 'SUCCESS' else 0
                category = sts_value[2]

                insert_tuple = {
                    'id_file': self.__id_file,
                    'id_test': id_test,
                    'id_result': id_result,
                    'p_value': p_value,
                    'assignment': assignment,
                    'category': category
                }

                values_dictionary_list.append(insert_tuple)

        return values_dictionary_list

    def _get_id_file(self, file_name: str):
        connection = sqlite3.connect(self._data_base_name)
        cursor = connection.cursor()

        query = f"SELECT id_file FROM tc_files WHERE file_name = \'{file_name}\'"
        cursor.execute(query)
        records = cursor.fetchone()

        connection.close()

        if records:
            return records[0]

        else:
            raise ValueError(
                f'The {file_name} file is not registered.  Please check.')

    def _insert(self, file_name: str, values_dictionary_list: Dict[str, Union[str, int, float]]):
        _ = file_name

        list_of_values = [values_dictionary_list[key]
                          for key in self._list_of_sts_columns]

        where = self._make_where(self._list_of_sts_columns, list_of_values)
        column_names = str(self._list_of_sts_columns)[
            1:-1].replace("'", '')
        str_values = str(list_of_values)[1:-1]

        query = f'SELECT {column_names} FROM tc_sts_records WHERE {where}'
        self._cursor.execute(query)
        records = self._cursor.fetchone()

        if records:
            print(f"{str_values} is already recorded in tc_sts_records")

        else:
            query = f'INSERT INTO tc_sts_records ({column_names}) VALUES ({str_values})'
            self._cursor.execute(query)

    def _update(self, file_name: str, differences: Dict[str, Union[str, int, float]]):
        _ = file_name
        update_string = []

        for key in differences:
            update_string.append(f'{key} = {differences[key]}')

        update_string = ', '.join(update_string)

        query = f"UPDATE tc_sts_records SET {update_string} WHERE id_file = '{self.__id_file}'"
        query += f" AND id_test = {self.__id_test} AND id_result = {self.__id_result}"
        self._cursor.execute(query)

    def get(self, file_name: str):
        """get(file_name: str) -> Dict[str, List[STS_Value]]

        Obtains the STS records from the indicated file

        PARAMETERS
        ----------
        file_name: str
            Name of analyzed file

        RETURNS
        -------
        Dict[str, List[STSValue]]
            Dictionary of results
        """
        output_results = {}

        id_file = self._get_id_file(file_name)

        connection = sqlite3.connect(self._data_base_name)
        cursor = connection.cursor()

        query = "SELECT test.test_name, sts.p_value,"
        query += "CASE WHEN sts.assignment = 1 THEN 'SUCCESS' ELSE 'FAILURE' END AS assignment, sts.category "
        query += "FROM tc_sts_records sts INNER JOIN tc_sts_tests test ON sts.id_test = test.id_test "
        query += f"WHERE id_file = {id_file} ORDER BY sts.id_test, sts.id_result;"
        cursor.execute(query)
        records = cursor.fetchall()

        connection.close()

        for item in records:
            key = item[0]
            p_value = item[1]
            assignment = item[2]
            category = item[3]

            if key not in output_results:
                output_results[key] = []

            output_results[key].append([p_value, assignment, category])

        return output_results

    def delete(self, file_name: str):
        """delete(file_name: str) -> bool

        Delete STS records from the file

        PARAMETERS
        ----------
        file_name: str
            Name of analyzed file
        """
        id_file = self._get_id_file(file_name)

        connection = sqlite3.connect(self._data_base_name)
        cursor = connection.cursor()

        query = f"DELETE FROM tc_sts_records WHERE id_file = {id_file};"
        cursor.execute(query)

        connection.close()
