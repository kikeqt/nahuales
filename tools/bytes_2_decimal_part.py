__version__ = "$Version: 2.0.0"

from math import ceil

from .active_bits_iterable import Active_bits_iterable
from .integer_2_bytes import Integer_2_bytes

class Bytes_2_decimal_part(Active_bits_iterable, Integer_2_bytes):
    
    def bytes_2_decimal_part(self, bytes_parameter: bytes):
        """Convert a set of bytes to the decimal part of a number"""
        if isinstance(bytes_parameter, int):
            bytes_parameter = self.integer_2_bytes(bytes_parameter)

        if isinstance(bytes_parameter, bytes):
            sum = 0

            for bit in self.active_bits_iterable(bytes_parameter):
                sum += 1 / (2 ** (bit + 1))

            return sum

        else:
            print('Fatal error: I do not know how to process the type', type(bytes_parameter))
            return None