__version__ = "$Version: 0.0.1"

from os.path import exists


class STS_read_final_analysis_report(object):
    """STS_read_final_analysis_report
    
    Methods
    -------
    read_from_file(file_name: str) -> dict
        Get the results of the final analisys report.
    """
    def read_from_file(self, file_name: str) -> dict:
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
        results_outputs = []

        if exists(file_name):
            with open(file_name, 'r') as file_report:
                for item in range(7):
                    _ = file_report.readline()
                    
                output = {}

                while line := file_report.readline():
                    if len(line) == 1:
                        break

                    line = line[:-1].replace('  ', ' ')
                    line = line.replace('  ', ' ')
                    line = line.replace('  ', ' ')
                    line = line[1:].split(' ')
                    test = line[-1]
                    
                    if test not in output:
                        output[test] = []
                        
                    category = 0

                    for item in range(10):
                        if line[item] == '1':
                            category = item + 1
                            
                    output[test].append(category)

            return output
