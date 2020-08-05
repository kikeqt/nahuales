__version__ = "$Version: 1.0.0"

from unittest import TestCase

from tools.show_file_name import show_file_name
from .count_active_bits import Count_active_bits


class Count_inactive_bits(Count_active_bits):

    def count_inactive_bits(self, bytes_parameter: bytes, max_number_bits: int = 0):
        """Count un-active bits

        Note:
        |   [  0   ] [  1   ] [  2   ] [  3   ]  Read order block
        |   01234567 89012345 67890123 45678901  Intuitive indexes
        |   10987654 32109876 54321098 76543210  Real indexes
        |   -------- -------- -------- --------
        |0b 01000000 01000001 01000010 01000011
        |   64 or @  65 or A  66 or B  66 or C

        Intuitive index for active bits = [1,9,15,17,22,25,30,31]
        Real index for active bits = [0,1,6,9,14,16,22,30]
        Real index for unactive bits = [2,3,4,5,7,8,10,11,12,13,15,17,18,19,20,21,23,24,26,27,28,29]]
        """
        if max_number_bits == 0:
            max_number_bits = len(bytes_parameter) * 8

        return max_number_bits - self.count_active_bits(bytes_parameter, max_number_bits)


class Count_inactive_bits_Test(TestCase):
    def setUp(self):
        self.test_object = Count_inactive_bits()

    def test_count_inactive_bits(self):
        test_value = b'@ABC'
        self.assertEqual(
            24,
            self.test_object.count_unactive_bits(test_value)
        )
