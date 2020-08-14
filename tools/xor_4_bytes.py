__version__ = "$Version: 2.0.2"


class XOR_4_bytes(object):
    def xor_4_bytes(self, data: bytes, mask: bytes):
        """Does the XOR operation on two bytes"""
        output = bytes(m ^ x for m, x in zip(data, mask[:len(data)]))

        if isinstance(data, bytes):
            return output

        print(
            f'\tFatal error (xor4bytes): The argument mut be a byte type')
        exit()
