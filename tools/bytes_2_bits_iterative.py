__version__ = "$Version: 2.0.1"


class Bytes2BitsIterative(object):
    @staticmethod
    def bytes_2_bits_iterative(
        bytes_parameter: bytes,
        max_number_bits: int = 0
    ):
        """Run a Byte data set bit by bit"""
        if max_number_bits == 0:
            max_number_bits = len(bytes_parameter) * 8

        read_counter = 0

        for current_byte in bytes_parameter:
            for current_bit in reversed(range(8)):
                read_counter += 1

                if read_counter <= max_number_bits:
                    yield current_byte >> current_bit & 0b1
