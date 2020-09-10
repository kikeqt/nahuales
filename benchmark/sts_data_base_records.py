__version__ = "$Version: 0.0.2"

from typing import Dict
from typing import List
from typing import Union

from .sts_value import STSValue
from .db_tc_files import DBTCFiles
from .db_tc_sts_records import DBTCSTSRecords
from .db_maker import DBMaker


class STSDataBaseRecords(DBMaker):
    """Manage the data base interaction

    Methods
    -------
    register_file(details: List[Dict[str, Union[str, int, float]]])
        Register the data in data base

    is_the_file_registered(file_name: str) -> bool
        Answer the question, are there STS file records?

    put_sts_records(file_name: str, results: Dict[str, List[STSValue]]) -> bool
        Register the file name in the catalog and saves or replaces the STS records

    get_sts_records(file_name: str) -> Union[Dict[str: List[List[any]]], None]
        Delete STS records from the file
    """
    __tc_files: DBTCFiles
    __tc_sts_records: DBTCSTSRecords

    def __init__(self, data_base_name: str):
        super().__init__(data_base_name)

        self.__tc_files = DBTCFiles(data_base_name)
        self.__tc_sts_records = DBTCSTSRecords(data_base_name)

    def register_file(self, details: Dict[str, Union[str, int, float]]):
        self.__tc_files.put(details)

    def is_the_file_registered(self, file_name: str) -> bool:
        return self.__tc_files.is_the_file_registered(file_name)

    def put_sts_records(self, file_name: str, details: Dict[str, List[STSValue]]):
        self.__tc_sts_records.put(file_name, details)

    def get_sts_records(self, file_name: str) -> Union[Dict[str: List[List[any]]], None]:
        return self.__tc_sts_records.get(file_name)
