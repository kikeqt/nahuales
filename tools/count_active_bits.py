__version__ = "$Version: 1.0.0"

from unittest import TestCase

from tools.show_file_name import show_file_name
from .bytes_2_integer import Bytes_2_integer


class Count_active_bits(Bytes_2_integer):

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
            sizeBlock = max_number_bits

            if max_number_bits == 0:
                sizeBlock = len(bytes_parameter)

            cntOnes = 0

            for bit in reversed(range(sizeBlock * 8)):
                if block >> bit & 0b1 == 1:
                    cntOnes += 1

            return cntOnes


class Count_active_bits_Test(TestCase):
    def setUp(self):
        self.count_active_bits = Count_active_bits()

    def test_count_active_bits(self):
        test_value = b'@ABC'
        self.assertEqual(
            8,
            self.count_active_bits.count_active_bits(test_value)
        )
