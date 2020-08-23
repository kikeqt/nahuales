__version__ = "$Version: 1.0.0"

from unittest import TestCase

from .get_byte import GetByte


class GetByteTest(TestCase):
    def setUp(self):
        self.test_object = GetByte()

    def test_count_active_bits(self):
        test_value = b'@ABC'
        self.assertEqual(b'@', self.test_object.get_byte(test_value, 0))
        self.assertEqual(b'A', self.test_object.get_byte(test_value, 1))
        self.assertEqual(b'B', self.test_object.get_byte(test_value, 2))
        self.assertEqual(b'C', self.test_object.get_byte(test_value, 3))
