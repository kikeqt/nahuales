__version__ = "$Version: 1.0.0"

from unittest import TestCase

from .read_bit import ReadBit


class ReadBitTest(TestCase):
    def setUp(self):
        self.read_bit = ReadBit()

    def test_read_bit(self):
        test_value = b'@ABC'

        for item in [0, 1, 6, 9, 14, 16, 22, 30]:
            self.assertEqual(1, self.read_bit.read_bit(test_value, item))

        for item in [2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 23, 24, 26, 27, 28, 29]:
            self.assertEqual(0, self.read_bit.read_bit(test_value, item))
