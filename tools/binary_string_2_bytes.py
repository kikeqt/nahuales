__version__ = "$Version: 2.0.1"

from .integer_2_bytes import Integer_2_bytes


class Binary_string_2_bytes(Integer_2_bytes):

    def binary_string_2_bytes(self, data: str, max_number_bits: int = 0):
        """Translate a string of ones and zeros to bytes"""
        myOutputBytes = b''
        data = data.strip()
        data = data.replace(' ', '')

        if max_number_bits == 0:
            max_number_bits = len(data)

        for block in range(max_number_bits // 8):
            myByte = 0b0

            for myBit in reversed(range(8)):
                pos = block * 8 + myBit

                if pos < max_number_bits:
                    if int(data[pos: pos + 1]) == 1:
                        myByte |= 0b1 << 7 - myBit

            myOutputBytes += self.integer_2_bytes(myByte)

        return myOutputBytes
