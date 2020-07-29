__version__ = "$Version: 1.0.0"

from math import ceil

from myBytesTools import activeBits
from myBytesTools import bytes2int
from myBytesTools import int2bytes
from myBytesTools import ror4Bytes
from myBytesTools import xor4bytes
from myCircularFileSynthesizer import Circular_File_Synthesizer


def xcr4Bytes(
	cfs: Circular_File_Synthesizer,
	required_bytes: int
):
	"""XOR in rotating cycles for bytes"""

	#### BEGIN Config ####
	maximum_size = 128
	minimum_size = 1
 
	maximum_local_size = len(cfs.data) if len(cfs.data) > maximum_size else maximum_size
	
	size_in_bytes = cfs.readInt % maximum_local_size
	size_in_bytes = size_in_bytes if size_in_bytes >= minimum_size else minimum_size
	
	total_rounds = ceil(required_bytes / size_in_bytes)
	#### END Config ####

	previous_data = cfs.readInBytes(size_in_bytes)
	
	for rounds in range(total_rounds):
		offset = cfs.readInt % size_in_bytes

		delivery_data = cfs.readInBytes(size_in_bytes)
		delivery_data = xor4bytes(ror4Bytes(delivery_data, offset), previous_data)

		previous_data = delivery_data

		# delivery data
		if len(delivery_data) > required_bytes:
			yield delivery_data[:required_bytes]

		else:
			required_bytes -= len(delivery_data)
			yield delivery_data


if __name__ == '__main__':
	"""Example of use"""

	# External libraries
	from myCircularFileSynthesizer import Circular_File_Synthesizer
	from myTools import printOK
	from myTools import show_example_of_use
	from myBenchmarkTools import benchmark
	from myBenchmarkTools import batch_benchmark

	show_example_of_use(__file__)

	# Parameters
	function = xcr4Bytes
	files = (__file__, )
	key = b'pass'
	requiredInBytes = 32

	cfs = Circular_File_Synthesizer(files, key)

	cfs.jumpPositions(cfs.readHashLikeInteger % len(cfs.data))

	for data in function(cfs, requiredInBytes):
		print(f'size(data): {len(data)}, data: {data}')

	# Reports
	batch_benchmark(function,__file__)
 