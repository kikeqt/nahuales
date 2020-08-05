__version__ = "$Version: 2.0.0"

from unittest import TestCase

from tools.show_file_name import show_file_name


class Read_bit(object):
    def read_bit(self, bytes_parameter: bytes, position: int):
        """Read a bit of the indicated position

        Note:
        |   [  0   ] [  1   ] [  2   ] [  3   ]  Read order block
        |   01234567 89012345 67890123 45678901  Intuitive indexes
        |   10987654 32109876 54321098 76543210  Real indexes
        |   -------- -------- -------- --------
        |0b 01000000 01000001 01000010 01000011
        |   64 or @  65 or A  66 or B  66 or C

        Intuitive index for active bits = [1,9,15,17,22,25,30,31]
        Intuitive index for unactive bits = [2,3,4,5,7,8,10,11,12,13,15,17,18,19,20,21,23,24,26,27,28,29]]
        Real index for active bits = [0,1,6,9,14,16,22,30]
        """
        return (bytes_parameter[len(bytes_parameter) - 1 - position // 8]) >> (position % 8) & 0b1


class Read_bit_Test(TestCase):
    def setUp(self):
        self.read_bit = Read_bit()

    def test_read_bit(self):
        test_value = b'@ABC'

        for item in [0, 1, 6, 9, 14, 16, 22, 30]:
            self.assertEqual(1, self.read_bit.read_bit(test_value, item))

        for item in [2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 23, 24, 26, 27, 28, 29]:
            self.assertEqual(0, self.read_bit.read_bit(test_value, item))
