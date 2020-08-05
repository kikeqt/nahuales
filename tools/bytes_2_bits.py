__version__ = "$Version: 2.0.0"

from unittest import TestCase

from .bytes_2_bits_iterative import Bytes_2_bits_iterative


class Bytes_2_bits(Bytes_2_bits_iterative):
    def bytes_2_bits(
        self,
        bytes_parameter: bytes,
        max_number_bits: int = 0
    ):
        """Run a Byte data set bit by bit"""
        if max_number_bits == 0:
            max_number_bits = len(bytes_parameter) * 8

        return [state for state in self.bytes_2_bits_iterative(bytes_parameter, max_number_bits)]


class Bytes_2_bits_Test(TestCase):

    def setUp(self):
        self.test_object = Get_byte()

    def test_count_active_bits(self):
        test_value = b'@ABC'
        self.assertEqual(b'@', self.test_object.get_byte(b'@ABC', 0))
        self.assertEqual(b'A', self.test_object.get_byte(b'@ABC', 1))
        self.assertEqual(b'B', self.test_object.get_byte(b'@ABC', 2))
        self.assertEqual(b'C', self.test_object.get_byte(b'@ABC', 3))
