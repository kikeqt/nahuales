__version__ = "$Version: 0.0.1"

import sqlite3
from typing import Dict
from typing import List
from typing import Union


class DataBase(object):
    _data_base_name: str
    _connection: sqlite3.Connection
    _cursor: sqlite3.Cursor
    _dictionary_of_test: Dict[str, int]
    
    def __init__(self, data_base_name: str):
        self._data_base_name = data_base_name

    def _get_dictionary_test(self):
        connection: sqlite3.Connection
        cursor: sqlite3.Cursor
        
        connection = sqlite3.connect(self._data_base_name)
        cursor = connection.cursor()

        query = 'SELECT * FROM tc_sts_tests'
        cursor.execute(query)
        records = cursor.fetchall()

        connection.close()

        records = [(key, value) for value, key in records]
        records = dict(records)

        self._dictionary_of_test = records
        
    def _get_test_id(self, test_name: str):
        query = f"SELECT id_test FROM tc_sts_tests WHERE test_name = '{test_name}'"
        self._cursor.execute(query)
        records = self._cursor.fetchone()

        if len(records) > 0:
            return records[0]

        else:
            raise ValueError('{test_name} is not register in tc_sts_tests')
    
    def _query_boolean(self, query: str):
        connection = sqlite3.connect(self._data_base_name)
        cursor = connection.cursor()

        cursor.execute(query)
        records = cursor.fetchone()[0]

        connection.close()

        return True if records > 0 else False

    def _put(
            self,
            dict_data: Dict[str, Union[float, int, str]],
            query_content: str,
            exists_function,
            check_differences_function,
            insert_function,
            update_function
    ):
        self._connection = sqlite3.connect(self._data_base_name)
        self._cursor = self._connection.cursor()

        if exists_function():
            differences = check_differences_function(query_content, dict_data)

            if len(differences) > 0:
                update_function(differences)

        else:
            insert_function(dict_data)

        self._connection.commit()
        self._connection.close()

    @staticmethod
    def _make_where(list_of_column_names: List[str], list_of_values: List[Union[str, int, float]]):
        where = list(zip(list_of_column_names, list_of_values))
        where = [str(item)[1:-1].replace(',', ' =') for item in where]
        where = str(where)[1:-1].replace('"', '').replace(',', ' AND')

        for item in list_of_column_names:
            where = where.replace(f"'{item}'", f'{item}')

        return where
