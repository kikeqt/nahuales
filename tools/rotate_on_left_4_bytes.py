__version__ = "$Version: 2.0.2"


class Rotate_on_left_4_bytes(object):
    def rotate_on_left_4_bytes(self, bytes_parameter: bytes, shift: int = 1):
        """Circular shift to the left"""
        shift %= len(bytes_parameter)

        if isinstance(bytes_parameter, bytes):
            return bytes_parameter[shift:] + bytes_parameter[:shift]

        print('Fatal error (rol4Bytes): The argument must be a byte type')
        exit()
