__version__ = "$Version: 2.0.0"

import unittest

from .active_bits_iterable import Active_bits_iterable



class Active_bits(Active_bits_iterable):
    
    def active_bits(self, bytes_parameter: bytes):
        """Vector with the positions of active bits in notation little endian

        Note:  Please see active_bits_iterable
        """
        block = 0

        if isinstance(bytes_parameter, bytes):
            block = self.bytes_2_integer(bytes_parameter)

        else:
            print('Fatal error (active_bits): The argument must be a byte type not {}'.format(type(argBytes)))
            exit()

        if block == 0:
            return []

        else:
            vActive_bits = []

            for aBits in self.active_bits_iterable(bytes_parameter):
                vActive_bits.append(aBits)

            return vActive_bits
        

class Active_bits_Test(unittest.TestCase):
    def setUp(self):
        self.active_bits = Active_bits()
        
    def test_count_active_bits(self):
        test_value = b'@ABC'
        self.assertEqual([0, 1, 6, 9, 14, 16, 22, 30], self.active_bits.active_bits(test_value))
