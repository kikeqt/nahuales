__version__ = "$Version: 3.0.0"

from math import ceil

from .constants import Constants


class Integer2Bytes(Constants):

    def integer_2_bytes(self, integer_parameter: int, trim: int = 0):
        """Translate an integer to data type bytes format"""
        local_length = trim

        if trim == 0:
            local_length = ceil(integer_parameter.bit_length() / 8)

        if local_length == 0:
            local_length = 1

        return integer_parameter.to_bytes(local_length, byteorder=self._bytes_order)
