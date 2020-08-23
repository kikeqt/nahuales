__version__ = "$Version: 2.0.0"

from tools.show_file_name import show_file_name
from .bytes_2_integer import Bytes2Integer


class CountActiveBits(Bytes2Integer):

    def count_active_bits(self, bytes_parameter: bytes, max_number_bits: int = 0):
        """Count active bits

        Note:
        |   [  0   ] [  1   ] [  2   ] [  3   ]  Read order block
        |   01234567 89012345 67890123 45678901  Intuitive indexes
        |   10987654 32109876 54321098 76543210  Real indexes
        |   -------- -------- -------- --------
        |0b 01000000 01000001 01000010 01000011
        |   64 or @  65 or A  66 or B  66 or C

        Intuitive index for active bits = [1,9,15,17,22,25,30,31]
        Real index for active bits = [0,1,6,9,14,16,22,30]
        """
        block = 0

        if isinstance(bytes_parameter, bytes):
            block = self.bytes_2_integer(bytes_parameter)

        else:
            print('Fatal error: The argument must be a byte type')
            exit()

        if block == 0:
            return 0

        else:
            size_block = max_number_bits

            if max_number_bits == 0:
                size_block = len(bytes_parameter)

            counter_ones = 0

            for bit in reversed(range(size_block * 8)):
                if block >> bit & 0b1 == 1:
                    counter_ones += 1

            return counter_ones
