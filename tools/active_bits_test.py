__version__ = "$Version: 1.0.0"

from unittest import TestCase

from .active_bits import ActiveBits


class ActiveBitsTest(TestCase):
    def setUp(self):
        self.test_object = ActiveBits()

    def test_count_active_bits(self):
        test_value = b'@ABC'
        self.assertEqual(
            [0, 1, 6, 9, 14, 16, 22, 30],
            self.test_object.active_bits(test_value)
        )
