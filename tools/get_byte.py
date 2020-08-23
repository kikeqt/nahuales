__version__ = "$Version: 3.0.0"


class GetByte(object):
    @staticmethod
    def get_byte(bytes_parameter: bytes, position: int):
        """Get a byte of a group of bytes"""
        return bytes_parameter[position: position + 1]
