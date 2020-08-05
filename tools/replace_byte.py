__version__ = "$Version: 2.0.0"

from unittest import TestCase


class Replace_byte(object):

    def replace_byte(self, bytes_parameter: bytes, substitute: bytes, position: int):
        """Replaces a byte, in a sequence of bytes, in the indicated position"""
        output = b''

        if position == 0:
            output = substitute + bytes_parameter[position+1:]

        elif (0 < position < len(bytes_parameter)):
            output = bytes_parameter[:position] + \
                substitute + bytes_parameter[position+1:]

        elif position == len(bytes_parameter) - 1:
            output = bytes_parameter[: position-1] + substitute

        else:
            print(
                'Fatal error (replaceByte): The indicated position is outside the set of bytes')
            output = b''

        if len(output) != len(bytes_parameter):
            print('The size changed: origin: {} vs new: {}, pos: {}'.format(
                len(output), len(bytes_parameter), position))

        return output


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
