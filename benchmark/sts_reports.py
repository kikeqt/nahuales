__version__ = "$Version: 0.0.2"

from os import listdir
from typing import Dict
from typing import List

from .sts_read_from_file import STSReadFromFile
from .sts_data_base_records import STSDataBaseRecords
from .sts_value import STSValue


class STSReports(STSReadFromFile):
    """Extracts the results of all NIST STS tests

    Methods
    -------
    get_file_reports(environment_location: str) -> dict:
        Extracts the results of all NIST STS tests and the final analysis report.

    set_environment_location(environment_location: str)
        Set the environment location
    """
    __environment_location: str
    __data_base_results: STSDataBaseRecords

    def __init__(self, environment_location: str, data_base: STSDataBaseRecords):
        self.__environment_location = environment_location
        self.__base_path = f'{self.__environment_location}/experiments/AlgorithmTesting/'
        self.__data_base_results = data_base

    def __get_reports_of_file(self):
        """get_file_reports(environment_location: str) -> dict:
        Extracts the results of all NIST STS tests and the final analysis report.

        RETURNS
        -------
        Dict
            Results dictionary
        """
        for folder in listdir(self.__base_path):
            if '.txt' not in folder:

                if folder in ['LinearComplexity', ]:
                    self._read_line_from_file(folder, 11)

                else:
                    self._read_from_file(folder)

        self._read_from_final_report_file()

        return self._dictionary_results

    def __get_reports_of_data_base(self, file_name: str):
        return self.__data_base_results.get_sts_records(file_name)

    @staticmethod
    def __encode_results_as_a_dictionary(reports: Dict[str, List[STSValue]]):
        return {
            key: [
                [item.p_value, item.assignment, item.category] for item in reports[key]
            ] for key in reports
        }

    def get_reports(self, file_name: str):
        self.set_base_path(self.__base_path)

        if file_name.replace('/', '\\') == self.obtain_name_of_analyzed_file():
            results = self.__get_reports_of_file()

            results = self.__encode_results_as_a_dictionary(results)

            self.__data_base_results.put_sts_records(file_name, results)

            return results

        else:
            return self.__get_reports_of_data_base(file_name)
