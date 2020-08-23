__version__ = "$Version: 3.0.0"

from math import ceil

from .active_bits_iterable import ActiveBitsIterable
from .integer_2_bytes import Integer2Bytes


class Bytes2DecimalPart(ActiveBitsIterable, Integer2Bytes):
    def bytes_2_decimal_part(self, bytes_parameter: bytes):
        """Convert a set of bytes to the decimal part of a number"""
        if isinstance(bytes_parameter, int):
            bytes_parameter = self.integer_2_bytes(bytes_parameter)

        if isinstance(bytes_parameter, bytes):
            amount = 0

            for bit in self.active_bits_iterable(bytes_parameter):
                amount += 1 / (2 ** (bit + 1))

            return amount

        else:
            print('Fatal error: I do not know how to process the type',
                  type(bytes_parameter))

            return None
