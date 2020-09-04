__version__ = "$Version: 0.0.1"

import sqlite3
from os.path import exists

from .db import DataBase


class DBMaker(DataBase):

    def __init__(self, data_base_name: str):
        self._data_base_name = data_base_name

        self._post()

    def _post(self):
        """_post()

        Create the database and its tables, if necessary
        """
        if not exists(self._data_base_name):
            print(
                f'The database {self._data_base_name} does not exist, it will be created.')

            sql_create = [
                '''
                CREATE TABLE "tc_files" (
                    "id_file"	INTEGER NOT NULL,
                    "file_name"	REAL NOT NULL UNIQUE,
                    "size_in_bytes"	INTEGER NOT NULL,
                    "processing_time"	REAL NOT NULL,
                    "category"	TEXT,
                    "notes"	TEXT,
                    PRIMARY KEY("id_file" AUTOINCREMENT)
                )
                ''',
                '''
                CREATE TABLE "tc_sts_records" (
                    "id_file"	INTEGER NOT NULL,
                    "id_test"	INTEGER NOT NULL,
                    "id_result"	INTEGER NOT NULL,
                    "p_value"	REAL NOT NULL,
                    "assignment"	INTEGER NOT NULL CHECK("assignment" IN (0, 1)),
                    "category"	INTEGER NOT NULL,
                    FOREIGN KEY("id_file") REFERENCES "tc_files"("id_file")
                )
                ''',
                '''
                CREATE TABLE "tc_sts_tests" (
                    "id_test"	INTEGER NOT NULL UNIQUE,
                    "test_name"	TEXT NOT NULL UNIQUE,
                    PRIMARY KEY("id_test")
                )
                ''',
            ]

            test_name = (
                ('ApproximateEntropy',),
                ('BlockFrequency',),
                ('CumulativeSums',),
                ('FFT',),
                ('Frequency',),
                ('LinearComplexity',),
                ('LongestRun',),
                ('NonOverlappingTemplate',),
                ('OverlappingTemplate',),
                ('RandomExcursions',),
                ('RandomExcursionsVariant',),
                ('Rank',),
                ('Runs',),
                ('Serial',),
                ('Universal',), )

            self._connection = sqlite3.connect(self._data_base_name)
            self._cursor = self._connection.cursor()

            for sql_query in sql_create:
                self._cursor.execute(sql_query)

            self._cursor.executemany(
                "INSERT INTO tc_sts_tests (test_name) VALUES (?)", test_name)

            self._connection.commit()
            self._connection.close()

            print('Successfully created')
