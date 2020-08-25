__version__ = "$Version: 1.0.1"

import errno
from os import strerror
from os.path import exists
import re
from typing import Union
from typing import Tuple
from typing import List

from .sts_results_collection import STS_Results_Collection
from .sts_value import STSValue


class STS_read_from_file(STS_Results_Collection):
    """Read the STS statistics files

    Methods
    -------
    obtain_name_of_analyzed_file() -> str:
        Obtain name of analyzed file


    """
    __base_path: str

    def __extract_p_value(self, line_content: str):
        assignment: Union[str, None]
        p_value = None
        regEx: str

        if 'SUCCESS' in line_content:
            assignment = 'SUCCESS'

        elif 'FAILURE' in line_content:
            assignment = 'FAILURE'

        else:
            assignment = None

        if ('p_value1' in line_content or 'p_value2' in line_content):
            regEx = r"p_value[12] = ([\d\.]+)"

        elif ('p_value' in line_content or 'p-value' in line_content):
            regEx = r"p[_-]value = ([\d\.]+)"

        elif ('SUCCESS' in line_content or 'FAILURE' in line_content):
            regEx = r" ([\d\.]{8}) [SF]"

        elif len(line_content) == 54:
            p_value = float(line_content[46:-1])

            return p_value, assignment

        else:
            print(len(line_content))
            print(line_content)
            print('Unsupported case')

        pattern = re.compile(regEx)
        search = pattern.search(line_content)

        if search:
            p_value = float(search.group(1))

        else:
            raise ValueError('P-Value not found')

        return p_value, assignment

    def _read_from_file(self, test_name: str):
        """read_from_file(self, file_name: str):

        Read each line for SUCCESS or FAILURE

        PARAMETERS
        ----------
        file_name: str
            Name of the file to be read
        """
        item = 0

        if test_name not in self._dictionary_results:
            self._dictionary_results[test_name]: List[STSValue] = []

        file_name = self.__base_path + test_name + '/stats.txt'

        if exists(file_name):
            with open(file_name, 'r') as file_sts:
                while line := file_sts.readline():
                    if 'SUCCESS' in line or 'FAILURE' in line:
                        p_value, assignment = self.__extract_p_value(line)

                        if len(self._dictionary_results[test_name]) <= item:
                            sts_value = STSValue(test_name)
                            self._dictionary_results[test_name].append(
                                sts_value)

                        self._dictionary_results[test_name][item].p_value = p_value
                        self._dictionary_results[test_name][item].assignment = assignment

                        item += 1

        else:
            raise FileNotFoundError(
                errno.ENOENT, strerror(errno.ENOENT), file_name)

    def _read_line_from_file(self, test_name: str, number_line: int):
        """read_line_from_file(self, file_name: str):

        Read each line for SUCCESS or FAILURE

        PARAMETERS
        ----------
        file_name: str
            Name of the file to be read

        number_line
            Indicates the marked line to find the last element in the column,
            as long as there is data
        """
        item = 0

        if test_name not in self._dictionary_results:
            self._dictionary_results[test_name]: List[STSValue] = []

        file_name = self.__base_path + test_name + '/stats.txt'

        if exists(file_name):
            with open(file_name, 'r') as file_sts:
                _ = [file_sts.readline() for item in range(number_line)]
                while line := file_sts.readline():
                    p_value, assignment = self.__extract_p_value(line)

                    if len(self._dictionary_results[test_name]) <= item:
                        sts_value = STSValue(test_name)
                        self._dictionary_results[test_name].append(sts_value)

                    self._dictionary_results[test_name][item].p_value = p_value
                    self._dictionary_results[test_name][item].assignment = assignment

                    item += 1

        else:
            raise FileNotFoundError(
                errno.ENOENT, strerror(errno.ENOENT), file_name)

    def _read_from_final_report_file(self):
        """read_from_file(final_report_file: str) -> dict

        Get the results of the final report file.

        PARAMETERS
        ----------
        final_report_file: str
            Name of the file to be read
        """
        final_report_file = self.__base_path + 'finalAnalysisReport.txt'

        if exists(final_report_file):
            with open(final_report_file, 'r') as file_report:
                for item in range(7):
                    _ = file_report.readline()

                test_name: str = ""
                counter: int

                while line := file_report.readline():
                    if len(line) == 1:
                        break

                    # Clear eval string
                    line = line[:-1].replace('  ', ' ')
                    line = line.replace('  ', ' ')
                    line = line.replace('  ', ' ')
                    line = line[1:].split(' ')

                    if line[-1] != test_name:
                        counter = 0
                        test_name = line[-1]

                    # Search for the category to which the evaluation belongs
                    category = 0

                    for item in range(10):
                        if line[item] == '1':
                            category = item + 1

                    self._dictionary_results[test_name][counter].category = category

                    counter += 1

    def obtain_name_of_analyzed_file(self):
        """obtain_name_of_analyzed_file() -> str:

        Obtain name of analyzed file

        PARAMETERS
        ----------
        final_report_file: str
            Name of the file to be read and it contains the final report

        RETURNS
        -------
        str
            Name of the analyzed file
        """
        final_report_file = self.__base_path + 'finalAnalysisReport.txt'

        if exists(final_report_file):
            with open(final_report_file, 'r') as file_report:
                for item in range(3):
                    _ = file_report.readline()

                content = file_report.readline()

                regEx = r'<([^>]+)>'
                pattern = re.compile(regEx)
                search = pattern.search(content)

                if search:
                    return search.group(1)

                else:
                    raise ValueError('FileName not found')
                    return None
        else:
            return ''

    def set_base_path(self, base_path: str):
        self.__base_path = base_path
