__version__ = "$Version: 2.0.0"


class Bytes_2_bits_iterative(object):

    def bytes_2_bits_iterative(
        self,
        bytes_parameter: bytes,
        max_number_bits: int = 0
    ):
        """Run a Byte data set bit by bit"""
        if max_number_bits == 0:
            max_number_bits = len(bytes_parameter) * 8

        read_counter = 0

        for cByte in bytes_parameter:
            for cBit in reversed(range(8)):
                read_counter += 1

                if (read_counter <= max_number_bits):
                    yield cByte >> cBit & 0b1
