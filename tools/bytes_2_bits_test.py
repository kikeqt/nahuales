__version__ = "$Version: 1.0.0"

from unittest import TestCase

from .bytes_2_bits import Bytes2Bits


class Bytes2BitsTest(TestCase):

    def setUp(self):
        self.test_object = Bytes2Bits()

    def test_count_active_bits(self):
        test_value = b'@ABC'
        validation_value = [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
                            0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1]
        self.assertEqual(validation_value,
                         self.test_object.bytes_2_bits(test_value))
