__version__ = "$Version: 3.0.0"

from tools.bytes_2_integer import Bytes2Integer
from tools.integer_2_bytes import Integer2Bytes


class RotateOnRight4Bits(Bytes2Integer, Integer2Bytes):

    def rotate_on_right_4_bits(self, bytes_parameter: bytes, shift: int = 1):
        """Circular shift to the right"""
        block: int
        size_block = len(bytes_parameter)
        shift %= size_block * 8
        complement_of_shift = size_block * 8 - shift

        if isinstance(bytes_parameter, bytes):
            block = self.bytes_2_integer(bytes_parameter)
            mask = 0x0

            for byte in range(size_block):
                mask |= 0xff << byte * 8

            output = self.integer_2_bytes(
                block << complement_of_shift & mask | block >> shift
            )
            size_output = len(output)

            if size_output != size_block:
                for _ in range(size_block - size_output):
                    output += bytes((0,))

            return output

        else:
            raise ValueError('Fatal error (rol): The argument must be a byte type')
