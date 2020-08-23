__version__ = "$Version: 1.0.0"

from unittest import TestCase

from .xor_4_bytes import XOR4Bytes


class XOR4BytesTest(TestCase):
    
    def setUp(self):
        self.test_object = XOR4Bytes()

    def test_rotate_on_left_4_bits(self):
        test_value = b'1234567890'

        test_values = (
            b'1234567890',
            b'0123456789',
            b'9012345678',
            b'9901234567',
            b'7990123456',
            b'6990123456',
            b'5699012345',
            b'4569901234',
            b'3456990123',
            b'2345699012',
            b'1234569901',
        )

        for item in test_values:
            xor_result = self.test_object.xor_4_bytes(test_value, item)

            self.assertEqual(
                test_value,
                self.test_object.xor_4_bytes(item, xor_result)
            )
