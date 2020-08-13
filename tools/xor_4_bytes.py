__version__ = "$Version: 2.0.1"

from unittest import TestCase


class XOR_4_bytes(object):
    def xor_4_bytes(self, data: bytes, mask: bytes):
        """Does the XOR operation on two bytes"""
        output = bytes(m ^ x for m, x in zip(data, mask[:len(data)]))

        if isinstance(data, bytes):
            return output

        print(
            f'\tFatal error (xor4bytes): The argument mut be a byte type')
        exit()


class XOR_4_bytes_Test(TestCase):

    def setUp(self):
        self.test_object = XOR_4_bytes()

    def test_rotate_on_left_4_bits(self):
        test_value = b'abcdefghij'
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
