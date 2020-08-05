__version__ = "$Version: 2.0.0"

from .bytes_2_integer import Bytes_2_integer


class Active_bits_iterable(Bytes_2_integer):
    
	def active_bits_iterable(self, bytes_parameter: bytes):
		"""Generator with the positions of active bits in notation little endian

		Note:
		|   [  0   ] [  1   ] [  2   ] [  3   ]  Read order block
		|   01234567 89012345 67890123 45678901  Intuitive indexes
		|   10987654 32109876 54321098 76543210  Real indexes
		|   -------- -------- -------- --------
		|0b 01000000 01000001 01000010 01000011
		|   64 or @  65 or A  66 or B  66 or C

		Intuitive index = [1,9,15,17,22,25,30,31]
		Real index = [0,1,6,9,14,16,22,30]
		"""
		block = 0

		if isinstance(bytes_parameter, bytes):
			block = self.bytes_2_integer(bytes_parameter)

		else:
			print('Fatal error: The argument must be a byte type')
			exit()

		sizeBlock = len(bytes_parameter)

		for bit in range(sizeBlock * 8):
			if block >> bit & 0b1 == 1:
				yield bit
