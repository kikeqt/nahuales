__version__ = "$Version: 2.0.2"

from .constants import Constants


class Bytes_2_integer(Constants):

    def bytes_2_integer(self, bytes_parameter: bytes):
        """Translate a data type "bytes" to an integer"""
        return int.from_bytes(bytes_parameter, self._bytes_order)
