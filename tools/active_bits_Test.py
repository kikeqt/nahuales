__version__ = "$Version: 0.0.1"

from unittest import TestCase

from .active_bits import Active_bits


class Active_bits_Test(TestCase):
    def setUp(self):
        self.test_object = Active_bits()

    def test_count_active_bits(self):
        test_value = b'@ABC'
        self.assertEqual(
            [0, 1, 6, 9, 14, 16, 22, 30],
            self.test_object.active_bits(test_value)
        )
