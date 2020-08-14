__version__ = "$Version: 0.0.1"

from unittest import TestCase

from .bytes_2_bits import Bytes_2_bits


class Bytes_2_bits_Test(TestCase):

    def setUp(self):
        self.test_object = Bytes_2_bits()

    def test_count_active_bits(self):
        test_value = b'@ABC'
        validation_value = [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
                            0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1]
        self.assertEqual(validation_value,
                         self.test_object.bytes_2_bits(test_value))
