__version__ = "$Version: 3.0.0"


class RotateOnRight4Bytes(object):
    @staticmethod
    def rotate_on_right_4_bytes(bytes_parameter: bytes, shift: int = 1):
        """Circular shift to the right"""
        shift %= len(bytes_parameter)

        if isinstance(bytes_parameter, bytes):
            return bytes_parameter[-shift:] + bytes_parameter[:-shift]

        print('Fatal error (rol4Bytes): The argument must be a byte type')
        exit()
