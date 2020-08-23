__version__ = "$Version: 3.0.0"

from .integer_2_bytes import Integer2Bytes


class BinaryString2Bytes(Integer2Bytes):

    def binary_string_2_bytes(self, data: str, max_number_bits: int = 0):
        """Translate a string of ones and zeros to bytes"""
        my_output_bytes = b''
        data = data.strip()
        data = data.replace(' ', '')

        if max_number_bits == 0:
            max_number_bits = len(data)

        for block in range(max_number_bits // 8):
            my_byte = 0b0

            for my_bit in reversed(range(8)):
                pos = block * 8 + my_bit

                if pos < max_number_bits:
                    if int(data[pos: pos + 1]) == 1:
                        my_byte |= 0b1 << 7 - my_bit

            my_output_bytes += self.integer_2_bytes(my_byte)

        return my_output_bytes
