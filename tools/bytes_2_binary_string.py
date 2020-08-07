__version__ = "$Version: 2.0.0"

from unittest import TestCase

from .bytes_2_bits_iterative import Bytes_2_bits_iterative


class Bytes_2_binary_string(Bytes_2_bits_iterative):
    def bytes_2_binary_string(
        self,
        bytes_parameter: bytes,
        max_number_bits: int = 0,
        block_size: int = 0,
    ):
        """Run a Byte data set bit by bit"""
        if max_number_bits == 0:
            max_number_bits = len(bytes_parameter) * 8
            
        if block_size == 0:
            block_size = len(bytes_parameter) * 8

        output = ''
        cnt = 0
        
        for state in self.bytes_2_bits_iterative(bytes_parameter, max_number_bits):
            output += ' ' if cnt % block_size == 0 else ''
            output += f'{state}'
            cnt += 1
            
        return output.strip()


class Bytes_2_binary_string_Test(TestCase):

    def setUp(self):
        self.test_object = Bytes_2_binary_string()

    def test_bytes_2_binary_string(self):
        test_value = b'@ABC'
        validation_value = [
            '01000000010000010100001001000011',
            '01000000 01000001 01000010 01000011',
            '0100 0000 0100 0001 0100 0010 0100 0011',
        ]
        self.assertEqual(validation_value[0], self.test_object.bytes_2_binary_string(test_value))
        self.assertEqual(validation_value[1], self.test_object.bytes_2_binary_string(test_value, block_size=8))
        self.assertEqual(validation_value[2], self.test_object.bytes_2_binary_string(test_value, block_size=4))
        