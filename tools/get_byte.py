__version__ = "$Version: 2.0.1"


class Get_byte(object):
    def get_byte(self, bytes_parameter: bytes, position: int):
        """Get a byte of a group of bytes"""
        return bytes_parameter[position: position + 1]
