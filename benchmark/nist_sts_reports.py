__version__ = "$Version: 0.0.1"

from os import listdir

from .sts_read_final_analysis_report import STS_read_final_analysis_report


class NIST_STS_Reports(object):
    """Extracts the results of all NIST STS tests

    Methods
    -------
    get_file_reports(environment_location: str, show_messages: bool = False) -> dict:
        Extracts the results of all NIST STS tests and the final analysis report.
    """

    def get_file_reports(self, environment_location: str, show_messages: bool = False):
        """get_file_reports(environment_location: str, show_messages: bool = False) -> dict:
        Extracts the results of all NIST STS tests and the final analysis report.

        PARAMETERS
        ----------
        environment_location: str
            Directory of reports.

        show_messages: bool = False
            Indicates if the messages will be displayed.

        RETURNS
        -------
        Dict
            Results dictionary
        """
        base_path = f'{environment_location}/experiments/AlgorithmTesting/'

        data_reader = STS_read_final_analysis_report()
        dict_results = {}

        for folder in listdir(base_path):
            if '.txt' not in folder:
                if show_messages:
                    print(folder)

                if folder in ['LinearComplexity', ]:
                    dict_results[folder] = data_reader.read_line_from_file(
                        base_path + folder + '/stats.txt', 11)

                else:
                    dict_results[folder] = data_reader.read_from_file(
                        base_path + folder + '/stats.txt')

                if show_messages:
                    print(f'\t{dict_results[folder]}')

        dict_results = data_reader.read_from_final_report_file(
            dict_results, base_path + 'finalAnalysisReport.txt')

        return dict_results
