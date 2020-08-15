__version__ = "$Version: 0.0.1"

from os import chdir
from os import getcwd
from os import system
from time import time

from .fast_nist_sts_maker import Fast_NIST_STS_Maker


class Fast_NIST_STS(Fast_NIST_STS_Maker):
    def __init__(self, version_sts: str = "v6.0.1"):
        super().__init__(version_sts)

    def eval(self, file: str, maximum_size_in_bits: int = 1000000):

        cmd = f'NIST.exe -fast -file {file} '
        cmd += '-streams 1 -tests 111111111111111 -defaultpar -fileoutput '
        cmd += f'-binary {maximum_size_in_bits}'
        
        print(cmd)

        current_path = getcwd()
        chdir(self._environment_location)

        startTime = time()
        system(cmd)
        spendTime2Eval = time() - startTime
        
        chdir(current_path)
            
        print(f'Spend time: {spendTime2Eval}')
