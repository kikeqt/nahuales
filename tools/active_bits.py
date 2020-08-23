__version__ = "$Version: 3.0.0"

from .active_bits_iterable import ActiveBitsIterable


class ActiveBits(ActiveBitsIterable):

    def active_bits(self, bytes_parameter: bytes):
        """Vector with the positions of active bits in notation little endian

        Note:  Please see active_bits_iterable
        """
        block = 0

        if isinstance(bytes_parameter, bytes):
            block = self.bytes_2_integer(bytes_parameter)

        else:
            print('Fatal error (active_bits): The argument must be a byte type not {}'.format(
                type(bytes_parameter)))
            exit()

        if block == 0:
            return []

        else:
            vActive_bits = []

            for aBits in self.active_bits_iterable(bytes_parameter):
                vActive_bits.append(aBits)

            return vActive_bits
