__version__ = "$Version: 2.0.0"

from struct import pack

from .constants import Constants


class Float_2_bytes(Constants):

    def float_2_bytes(self, float_number: float):
        """Translate a floating number to the data type bytes"""
        # TODO(find how to represent sign, int part and mantissa, that python does
        # not necessarily represent large float numbers in the same way that other
        # languages)
        return bytes(pack(self._bytes_order_structure, float_number))
