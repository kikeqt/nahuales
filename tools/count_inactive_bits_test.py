__version__ = "$Version: 1.0.0"

from unittest import TestCase

from .count_inactive_bits import CountInactiveBits


class CountInactiveBitsTest(TestCase):
    def setUp(self):
        self.test_object = CountInactiveBits()

    def test_count_inactive_bits(self):
        test_value = b'@ABC'
        self.assertEqual(
            24,
            self.test_object.count_inactive_bits(test_value)
        )
