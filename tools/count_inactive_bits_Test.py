__version__ = "$Version: 0.0.1"

from unittest import TestCase

from .count_inactive_bits import Count_inactive_bits


class Count_inactive_bits_Test(TestCase):
    def setUp(self):
        self.test_object = Count_inactive_bits()

    def test_count_inactive_bits(self):
        test_value = b'@ABC'
        self.assertEqual(
            24,
            self.test_object.count_inactive_bits(test_value)
        )
