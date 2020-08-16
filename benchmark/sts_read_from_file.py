__version__ = "$Version: 0.0.1"

import errno
from os import strerror
from os.path import exists
import re
from typing import Union, Tuple, List


class STS_read_from_file(object):
    """Read the STS statistics files

    Methods
    -------
    read_from_file(file_name: str):
        Read each line for SUCCESS or FAILURE

    read_line_from_file(file_name: str, number_line: int):
        Reads each line after the marked line to find the last element in the 
        column, as long as there is data
    """
    _file_name = ''

    def __extract_p_value(self, line):
        assignment: Union[str, None]
        p_value = None
        regEx: int

        if 'SUCCESS' in line:
            assignment = 'SUCCESS'

        elif 'FAILURE' in line:
            assignment = 'FAILURE'

        else:
            assignment = None

        if ('p_value1' in line or 'p_value2' in line):
            regEx = r"p_value[12] = ([\d\.]+)"

        elif ('p_value' in line or 'p-value' in line):
            regEx = r"p[_-]value = ([\d\.]+)"

        elif ('SUCCESS' in line or 'FAILURE' in line):
            regEx = r" ([\d\.]{8}) [SF]"

        elif len(line) == 54:
            p_value = float(line[46:-1])

            return [p_value, assignment]

        else:
            print(len(line))
            print(line)
            print('Unsupported case')

        pattern = re.compile(regEx)
        search = pattern.search(line)

        if search:
            p_value = float(search.group(1))

        else:
            raise ValueError('P-Value not found')

        return [p_value, assignment]

    def read_from_file(self, file_name: str):
        """read_from_file(self, file_name: str) -> List[Tuple[str, float]]:

        Read each line for SUCCESS or FAILURE

        PARAMETERS
        ----------
        file_name: str
            Name of the file to be read

        RETURNS
        -------
        List[Tuple[str, float]]
            Return a list of tuples (assignment, p-value)
        """
        results_outputs = []

        if exists(file_name):
            with open(file_name, 'r') as file_sts:
                while line := file_sts.readline():
                    if 'SUCCESS' in line or 'FAILURE' in line:
                        results_outputs.append(self.__extract_p_value(line))

        else:
            raise FileNotFoundError(
                errno.ENOENT, strerror(errno.ENOENT), file_name)

        return results_outputs

    def read_line_from_file(self, file_name: str, number_line: int):
        """read_line_from_file(self, file_name: str) -> List[Tuple[str, float]]:

        Read each line for SUCCESS or FAILURE

        PARAMETERS
        ----------
        file_name: str
            Name of the file to be read

        number_line
            Indicates the marked line to find the last element in the column,
            as long as there is data

        RETURNS
        -------
        List[Tuple[str, float]]
            Return a list of tuples (assignment, p-value)
        """
        results_outputs = []

        if exists(file_name):
            with open(file_name, 'r') as file_sts:
                _ = [file_sts.readline() for item in range(number_line)]
                while line := file_sts.readline():
                    results_outputs.append(self.__extract_p_value(line))
                    
        else:
            raise FileNotFoundError(
                errno.ENOENT, strerror(errno.ENOENT), file_name)

        return results_outputs
