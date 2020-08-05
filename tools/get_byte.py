__version__ = "$Version: 2.0.0"

from unittest import TestCase


class Get_byte(object):
    def get_byte(self, bytes_parameter: bytes, position: int):
        """Get a byte of a group of bytes"""
        return bytes_parameter[position: position + 1]


class Get_byte_Test(TestCase):
    def setUp(self):
        self.test_object = Get_byte()

    def test_count_active_bits(self):
        test_value = b'@ABC'
        self.assertEqual(b'@', self.test_object.get_byte(b'@ABC', 0))
        self.assertEqual(b'A', self.test_object.get_byte(b'@ABC', 1))
        self.assertEqual(b'B', self.test_object.get_byte(b'@ABC', 2))
        self.assertEqual(b'C', self.test_object.get_byte(b'@ABC', 3))
