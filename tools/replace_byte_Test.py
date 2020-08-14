__version__ = "$Version: 0.0.1"

from unittest import TestCase

from .replace_byte import Replace_byte


class Replace_byte_Test(TestCase):
    def setUp(self):
        self.test_object = Replace_byte()

    def test_count_active_bits(self):
        test_value = b'@ABC'
        self.assertEqual(
            b'XABC', self.test_object.replace_byte(b'@ABC', b'X', 0))
        self.assertEqual(
            b'@XBC', self.test_object.replace_byte(b'@ABC', b'X', 1))
        self.assertEqual(
            b'@AXC', self.test_object.replace_byte(b'@ABC', b'X', 2))
        self.assertEqual(
            b'@ABX', self.test_object.replace_byte(b'@ABC', b'X', 3))
