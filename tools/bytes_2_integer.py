__version__ = "$Version: 2.0.1"

from unittest import TestCase

from .constants import Constants


class Bytes_2_integer(Constants):

    def bytes_2_integer(self, bytes_parameter: bytes):
        """Translate a data type "bytes" to an integer"""
        return int.from_bytes(bytes_parameter, self._bytes_order)


class Bytes_2_integer_Test(TestCase):
    def setUp(self):
        self.test_object = Bytes_2_integer()

    def test_binary_2_string(self):
        test_values = (
            b'\x00',
            b'\x01',
            b'\x02',
            b'\x03',
            b'\x04',
            b'\x05',
            b'\x06',
            b'\x07',
            b'\x08',
            b'\t',
            b'\n',
            b'\x0b',
            b'\x0c',
            b'\r',
            b'\x0e',
            b'\x0f',
            b'\x10',
            b'\x11',
            b'\x12',
            b'\x13',
            b'\x14',
            b'\x15',
            b'\x16',
            b'\x17',
            b'\x18',
            b'\x19',
            b'\x1a',
            b'\x1b',
            b'\x1c',
            b'\x1d',
            b'\x1e',
            b'\x1f',
            b' ',
            b'!',
            b'"',
            b'#',
            b'$',
            b'%',
            b'&',
            b"'",
            b'(',
            b')',
            b'*',
            b'+',
            b',',
            b'-',
            b'.',
            b'/',
            b'0',
            b'1',
            b'2',
            b'3',
            b'4',
            b'5',
            b'6',
            b'7',
            b'8',
            b'9',
            b':',
            b';',
            b'<',
            b'=',
            b'>',
            b'?',
            b'@',
            b'A',
            b'B',
            b'C',
            b'D',
            b'E',
            b'F',
            b'G',
            b'H',
            b'I',
            b'J',
            b'K',
            b'L',
            b'M',
            b'N',
            b'O',
            b'P',
            b'Q',
            b'R',
            b'S',
            b'T',
            b'U',
            b'V',
            b'W',
            b'X',
            b'Y',
            b'Z',
            b'[',
            b'\\',
            b']',
            b'^',
            b'_',
            b'`',
            b'a',
            b'b',
            b'c',
            b'd',
            b'e',
            b'f',
            b'g',
            b'h',
            b'i',
            b'j',
            b'k',
            b'l',
            b'm',
            b'n',
            b'o',
            b'p',
            b'q',
            b'r',
            b's',
            b't',
            b'u',
            b'v',
            b'w',
            b'x',
            b'y',
            b'z',
            b'{',
            b'|',
            b'}',
            b'~',
            b'\x7f',
            b'\x80',
            b'\x81',
            b'\x82',
            b'\x83',
            b'\x84',
            b'\x85',
            b'\x86',
            b'\x87',
            b'\x88',
            b'\x89',
            b'\x8a',
            b'\x8b',
            b'\x8c',
            b'\x8d',
            b'\x8e',
            b'\x8f',
            b'\x90',
            b'\x91',
            b'\x92',
            b'\x93',
            b'\x94',
            b'\x95',
            b'\x96',
            b'\x97',
            b'\x98',
            b'\x99',
            b'\x9a',
            b'\x9b',
            b'\x9c',
            b'\x9d',
            b'\x9e',
            b'\x9f',
            b'\xa0',
            b'\xa1',
            b'\xa2',
            b'\xa3',
            b'\xa4',
            b'\xa5',
            b'\xa6',
            b'\xa7',
            b'\xa8',
            b'\xa9',
            b'\xaa',
            b'\xab',
            b'\xac',
            b'\xad',
            b'\xae',
            b'\xaf',
            b'\xb0',
            b'\xb1',
            b'\xb2',
            b'\xb3',
            b'\xb4',
            b'\xb5',
            b'\xb6',
            b'\xb7',
            b'\xb8',
            b'\xb9',
            b'\xba',
            b'\xbb',
            b'\xbc',
            b'\xbd',
            b'\xbe',
            b'\xbf',
            b'\xc0',
            b'\xc1',
            b'\xc2',
            b'\xc3',
            b'\xc4',
            b'\xc5',
            b'\xc6',
            b'\xc7',
            b'\xc8',
            b'\xc9',
            b'\xca',
            b'\xcb',
            b'\xcc',
            b'\xcd',
            b'\xce',
            b'\xcf',
            b'\xd0',
            b'\xd1',
            b'\xd2',
            b'\xd3',
            b'\xd4',
            b'\xd5',
            b'\xd6',
            b'\xd7',
            b'\xd8',
            b'\xd9',
            b'\xda',
            b'\xdb',
            b'\xdc',
            b'\xdd',
            b'\xde',
            b'\xdf',
            b'\xe0',
            b'\xe1',
            b'\xe2',
            b'\xe3',
            b'\xe4',
            b'\xe5',
            b'\xe6',
            b'\xe7',
            b'\xe8',
            b'\xe9',
            b'\xea',
            b'\xeb',
            b'\xec',
            b'\xed',
            b'\xee',
            b'\xef',
            b'\xf0',
            b'\xf1',
            b'\xf2',
            b'\xf3',
            b'\xf4',
            b'\xf5',
            b'\xf6',
            b'\xf7',
            b'\xf8',
            b'\xf9',
            b'\xfa',
            b'\xfb',
            b'\xfc',
            b'\xfd',
            b'\xfe',
            b'\xff',
        )

        for item in range(len(test_values)):
            self.assertEqual(
                item,
                self.test_object.bytes_2_integer(test_values[item])
            )
