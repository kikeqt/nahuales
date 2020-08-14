__version__ = "$Version: 2.0.2"

from .bytes_2_bits_iterative import Bytes_2_bits_iterative


class Bytes_2_binary_string(Bytes_2_bits_iterative):
    def bytes_2_binary_string(
        self,
        bytes_parameter: bytes,
        max_number_bits: int = 0,
        block_size: int = 0,
    ):
        """Run a Byte data set bit by bit"""
        if max_number_bits == 0:
            max_number_bits = len(bytes_parameter) * 8

        if block_size == 0:
            block_size = len(bytes_parameter) * 8

        output = ''
        cnt = 0

        for state in self.bytes_2_bits_iterative(bytes_parameter, max_number_bits):
            output += ' ' if cnt % block_size == 0 else ''
            output += f'{state}'
            cnt += 1

        return output.strip()
