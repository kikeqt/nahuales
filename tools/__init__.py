__version__ = "$Version: 1.0.0"

# For bytes
from .active_bits import ActiveBits
from .active_bits_iterable import ActiveBitsIterable
from .integer_2_string import Integer2String
from .binary_string_2_bytes import BinaryString2Bytes
from .bytes_2_binary_string import Bytes2BinaryString

from .bytes_2_bits import Bytes2Bits
from .bytes_2_bits_iterative import Bytes2BitsIterative
from .bytes_2_decimal_part import Bytes2DecimalPart
from .bytes_2_integer import Bytes2Integer
from .count_active_bits import CountActiveBits

from .count_inactive_bits import CountInactiveBits
from .integer_2_bytes import Integer2Bytes
from .float_2_bytes import Float2Bytes
from .get_byte import GetByte
from .read_bit import ReadBit

from .replace_byte import ReplaceByte
from .rotate_on_left_4_bits import RotateOnLeft4Bits
from .rotate_on_left_4_bytes import RotateOnLeft4Bytes
from .rotate_on_right_4_bits import RotateOnRight4Bits
from .rotate_on_right_4_bytes import RotateOnRight4Bytes

from .xor_4_bytes import XOR4Bytes


import colorama
colorama.init(autoreset=True)

# Many things
from .clear_console import clear_console
from .compare_files import compare_files
from .print_color import print_color
from .show_example_of_use import show_example_of_use
from .split_path_file_extension import split_path_file_extension

from .sync_files import sync_files
