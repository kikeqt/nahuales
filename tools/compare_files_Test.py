__version__ = "$Version: 0.0.1"

from unittest import TestCase

from .compare_files import compare_files


class Compare_Files_Tests(TestCase):
    def test_compare_files(self):
        self.assertEqual(True, compare_files(
            'tools/compare_files.py', 'tools/compare_files.py'))
