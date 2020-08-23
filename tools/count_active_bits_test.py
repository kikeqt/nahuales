__version__ = "$Version: 1.0.0"

from unittest import TestCase

from .count_active_bits import CountActiveBits


class CountActiveBitsTest(TestCase):
    def setUp(self):
        self.count_active_bits = CountActiveBits()

    def test_count_active_bits(self):
        test_value = b'@ABC'
        self.assertEqual(
            8,
            self.count_active_bits.count_active_bits(test_value)
        )
