__version__ = "$Version: 0.0.1"

from unittest import TestCase

from .bytes_2_binary_string import Bytes_2_binary_string


class Bytes_2_binary_string_Test(TestCase):

    def setUp(self):
        self.test_object = Bytes_2_binary_string()

    def test_bytes_2_binary_string(self):
        test_value = b'@ABC'
        validation_value = [
            '01000000010000010100001001000011',
            '01000000 01000001 01000010 01000011',
            '0100 0000 0100 0001 0100 0010 0100 0011',
        ]
        self.assertEqual(
            validation_value[0], self.test_object.bytes_2_binary_string(test_value))
        self.assertEqual(validation_value[1], self.test_object.bytes_2_binary_string(
            test_value, block_size=8))
        self.assertEqual(validation_value[2], self.test_object.bytes_2_binary_string(
            test_value, block_size=4))
