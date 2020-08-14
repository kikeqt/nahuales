__version__ = "$Version: 0.0.1"

from unittest import TestCase

from .count_active_bits import Count_active_bits

class Count_active_bits_Test(TestCase):
    def setUp(self):
        self.count_active_bits = Count_active_bits()

    def test_count_active_bits(self):
        test_value = b'@ABC'
        self.assertEqual(
            8,
            self.count_active_bits.count_active_bits(test_value)
        )
