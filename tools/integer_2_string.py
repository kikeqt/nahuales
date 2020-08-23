__version__ = "$Version: 3.0.0"


class Integer2String(object):

    def integer_2_string(self, data: int, width: int = 0):
        """Convert a number to binary representation"""
        if width == 0:
            width = (data.bit_length() + 7) // 8 * 8

        fmt = '{:0%sb}' % width
        return fmt.format(data)
