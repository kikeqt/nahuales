__version__ = "$Version: 2.0.0"

from unittest import TestCase


class Rotate_on_left_4_bytes(object):
    def rotate_on_left_4_bytes(self, bytes_parameter: bytes, shift: int = 1):
        """Circular shift to the left"""
        shift %= len(bytes_parameter)

        if isinstance(bytes_parameter, bytes):
            return bytes_parameter[shift:] + bytes_parameter[:shift]

        print('Fatal error (rol4Bytes): The argument must be a byte type')
        exit()
        
class Rotate_on_left_4_bytes_Test(TestCase):
    def setUp(self):
        self.test_object = Rotate_on_left_4_bytes()

    def test_rotate_on_left_4_bytes(self):
        test_value = b'@ABC'
        self.assertEqual(b'ABC@', self.test_object.rotate_on_left_4_bytes(test_value, 1))
        self.assertEqual(b'BC@A', self.test_object.rotate_on_left_4_bytes(test_value, 2))
        self.assertEqual(b'C@AB', self.test_object.rotate_on_left_4_bytes(test_value, 3))
        self.assertEqual(b'@ABC', self.test_object.rotate_on_left_4_bytes(test_value, 4))
