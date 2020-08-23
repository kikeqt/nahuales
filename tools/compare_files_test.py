__version__ = "$Version: 1.0.0"

from unittest import TestCase

from .compare_files import compare_files


class CompareFilesTests(TestCase):
    def test_compare_files(self):
        self.assertEqual(True, compare_files(
            'tools/compare_files.py', 'tools/compare_files.py'))
