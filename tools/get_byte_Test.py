__version__ = "$Version: 0.0.1"

from unittest import TestCase

from .get_byte import Get_byte


class Get_byte_Test(TestCase):
    def setUp(self):
        self.test_object = Get_byte()

    def test_count_active_bits(self):
        test_value = b'@ABC'
        self.assertEqual(b'@', self.test_object.get_byte(test_value, 0))
        self.assertEqual(b'A', self.test_object.get_byte(test_value, 1))
        self.assertEqual(b'B', self.test_object.get_byte(test_value, 2))
        self.assertEqual(b'C', self.test_object.get_byte(test_value, 3))
