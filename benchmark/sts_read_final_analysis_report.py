__version__ = "$Version: 1.0.0"

from os.path import exists

from .sts_read_from_file import STS_read_from_file


class STS_read_final_analysis_report(STS_read_from_file):
    """Read the STS final analysis report

    Methods
    -------
    read_from_file(file_name: str) -> dict
        Get the results of the final analisys report.
    """

    def read_from_final_report_file(self, dict_results: dict, file_name: str) -> dict:
        """read_from_file(file_name: str) -> dict

        Get the results of the final analisys report.

        PARAMETERS
        ----------
        file_name: str
            Name of the file to be read

        RETURNS
        -------
        Dict
            Results dictionary.
        """

        if exists(file_name):
            with open(file_name, 'r') as file_report:
                for item in range(7):
                    _ = file_report.readline()

                test: str = ""
                counter: int

                while line := file_report.readline():
                    if len(line) == 1:
                        break

                    # Clear eval string
                    line = line[:-1].replace('  ', ' ')
                    line = line.replace('  ', ' ')
                    line = line.replace('  ', ' ')
                    line = line[1:].split(' ')

                    if line[-1] != test:
                        counter = 0
                        test = line[-1]

                    # Search for the category to which the evaluation belongs
                    category = 0

                    for item in range(10):
                        if line[item] == '1':
                            category = item + 1

                    dict_results[test][counter].append(category)

                    counter += 1

            return dict_results
