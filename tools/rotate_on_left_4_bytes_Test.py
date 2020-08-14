__version__ = "$Version: 0.0.1"

from unittest import TestCase

from .rotate_on_left_4_bytes import Rotate_on_left_4_bytes


class Rotate_on_left_4_bytes_Test(TestCase):
    def setUp(self):
        self.test_object = Rotate_on_left_4_bytes()

    def test_rotate_on_left_4_bytes(self):
        test_value = b'@ABC'
        self.assertEqual(
            b'ABC@',
            self.test_object.rotate_on_left_4_bytes(test_value, 1)
        )
        self.assertEqual(
            b'BC@A',
            self.test_object.rotate_on_left_4_bytes(test_value, 2)
        )
        self.assertEqual(
            b'C@AB',
            self.test_object.rotate_on_left_4_bytes(test_value, 3)
        )
        self.assertEqual(
            b'@ABC',
            self.test_object.rotate_on_left_4_bytes(test_value, 4)
        )
        self.assertEqual(
            b'ABC@',
            self.test_object.rotate_on_left_4_bytes(test_value, 5)
        )
        self.assertEqual(
            b'BC@A',
            self.test_object.rotate_on_left_4_bytes(test_value, 6)
        )
        self.assertEqual(
            b'C@AB',
            self.test_object.rotate_on_left_4_bytes(test_value, 7)
        )
        self.assertEqual(
            b'@ABC',
            self.test_object.rotate_on_left_4_bytes(test_value, 8)
        )
