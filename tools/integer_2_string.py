__version__ = "$Version: 2.0.1"


class Integer_2_string(object):

    def integer_2_string(self, data: int, width: int = 0):
        """Convert a number to binary representation"""
        if width == 0:
            width = (data.bit_length() + 7) // 8 * 8

        fmt = '{:0%sb}' % width
        return fmt.format(data)
