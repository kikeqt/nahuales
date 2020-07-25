# -*- coding: utf-8 -*-
from math import ceil
from struct import pack

myByteOrder = "big"
myByteOrderStruct = ">f"


def activeBits(argBytes: bytes):
	"""Vector with the positions of active bits in notation little endian

	Note:  Please see activeBitsIterable
	"""
	block = 0

	if isinstance(argBytes, bytes):
		block = bytes2int(argBytes)

	else:
		print('Fatal error (activeBits): The argument must be a byte type not {}'.format(type(argBytes)))
		exit()

	if block == 0:
		return []

	else:
		vActiveBits = []

		for aBits in activeBitsIterable(argBytes):
			vActiveBits.append(aBits)

		return vActiveBits


def activeBitsIterable(argBytes: bytes):
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

	if isinstance(argBytes, bytes):
		block = bytes2int(argBytes)

	else:
		print('Fatal error: The argument must be a byte type')
		exit()

	sizeBlock = len(argBytes)

	for bit in range(sizeBlock * 8):
		if block >> bit & 0b1 == 1:
			yield bit


def bin2Str(argData: int, argWidth: int=0):
	"""Convert a number to binary representation"""
	if argWidth == 0:
		argWidth = (argData.bit_length() + 7) // 8 * 8

	fmt = '{:0%sb}' % argWidth
	return fmt.format(argData)


def binStr2Bytes(argData: str, argSize: int=0):
	"""Translate a string of ones and zeros to bytes"""
	myOutputBytes = b''
	argData = argData.strip()
	argData = argData.replace(' ', '')

	if argSize == 0:
		argSize = len(argData)

	for block in range(argSize // 8):
		myByte = 0b0

		for myBit in reversed(range(8)):
			pos = block * 8 + myBit

			if pos < argSize:
				if int(argData[pos: pos + 1]) == 1:
					myByte |= 0b1 << 7 - myBit

		myOutputBytes += int2bytes(myByte)

	return myOutputBytes


def bytes2DecimalPart(argBytes: bytes):
	"""Convert a set of bytes to the decimal part of a number"""
	if isinstance(argBytes, int):
		argBytes = int2bytes(argBytes)

	if isinstance(argBytes, bytes):
		sum = 0

		for bit in activeBitsIterable(argBytes):
			sum += 1 / (2 ** (bit + 1))

		return sum

	else:
		print('Fatal error: I do not know how to process the type', type(argBytes))
		return None


def bytes2int(argBytes: bytes):
	"""Translate a data type data "bytes" to an integer"""
	return int.from_bytes(argBytes, myByteOrder)


def bytes2BitIter(argBytes: bytes, argMaxReading: int=0):
	"""Run a Byte data set bit by bit"""
	if argMaxReading == 0:
		argMaxReading = len(argBytes) * 8

	cntRead = 0

	for cByte in argBytes:
		for cBit in reversed(range(8)):
			cntRead += 1

			if (cntRead <= argMaxReading):
				yield cByte >> cBit & 0b1


def countActiveBits(argBytes: bytes, argSize: int=0):
	"""Count active bits

	Note:
	|   [  0   ] [  1   ] [  2   ] [  3   ]  Read order block
	|   01234567 89012345 67890123 45678901  Intuitive indexes
	|   10987654 32109876 54321098 76543210  Real indexes
	|   -------- -------- -------- --------
	|0b 01000000 01000001 01000010 01000011
	|   64 or @  65 or A  66 or B  66 or C

	Intuitive index for active bits = [1,9,15,17,22,25,30,31]
	"""
	block = 0

	if isinstance(argBytes, bytes):
		block = bytes2int(argBytes)

	else:
		print('Fatal error: The argument must be a byte type')
		exit()

	if block == 0:
		return 0

	else:
		sizeBlock = argSize

		if argSize == 0:
			sizeBlock = len(argBytes)

		cntOnes = 0

		for bit in reversed(range(sizeBlock * 8)):
			if block >> bit & 0b1 == 1:
				cntOnes += 1

		return cntOnes


def countUnActiveBits(argBytes: bytes, argSize: int=0):
	"""Count un-active bits

	Note:
	|   [  0   ] [  1   ] [  2   ] [  3   ]  Read order block
	|   01234567 89012345 67890123 45678901  Intuitive indexes
	|   10987654 32109876 54321098 76543210  Real indexes
	|   -------- -------- -------- --------
	|0b 01000000 01000001 01000010 01000011
	|   64 or @  65 or A  66 or B  66 or C

	Intuitive index for active bits = [1,9,15,17,22,25,30,31]
	"""
	if argSize == 0:
		argSize = len(argBytes)

	return argSize - countActiveBits(argBytes, argSize)
	

def int2bytes(argInt: int, argTrim: int=0):
	"""Translate an integer to data type bytes format"""
	localLength = argTrim

	if argTrim == 0:
		localLength = ceil(argInt.bit_length() / 8)

	if localLength == 0:
		localLength = 1

	return argInt.to_bytes(localLength, byteorder=myByteOrder)


def float2bytes(argFloat: float):
	"""Translate a floating number to the data type bytes"""
	# TODO(find how to represent sign, int part and mantissa, that python does
	# not necessarily represent large float numbers in the same way that other
	# languages)
	return bytearray(pack(myByteOrderStruct, argFloat))


def getByte(argBytes:bytes, argPos: int):
	"""Get a byte of a group of bytes"""
	return argBytes[argPos: argPos + 1]


def readBit(argBytes: bytes, argPos: int):
	"""Read a bit of the indicated position"""
	#argPos %= len(argBytes) * 8
	return bytes2int(argBytes) >> argPos & 0b1


def replaceByte(argBytes: bytes, argByte: bytes, argPos:int):
	"""Replaces a byte, in a sequence of bytes, in the indicated position"""
	output = b''

	if argPos == 0:
		output = argByte + argBytes[argPos+1:]

	elif (0 < argPos < len(argBytes)):
		output = argBytes[:argPos] + argByte + argBytes[argPos+1:]

	elif argPos == len(argBytes) - 1 :
		output = argBytes[: argPos-1] + argByte

	else:
		print('Fatal error (replaceByte): The indicated position is outside the set of bytes')
		output = b''

	if len(output) != len(argBytes):
		print('The size changed: origin: {} vs new: {}, pos: {}'.format(
			len(output), len(argBytes), argPos))
	
	return output


def rol(argBytes: bytes, argShift: int=1):
	"""Circular shift to the left"""
	block = 0
	sizeBlock = len(argBytes)
	argShift %= sizeBlock * 8
	compShift = sizeBlock * 8 - argShift

	if isinstance(argBytes, bytes):
		block = bytes2int(argBytes)
		mask = 0x0

		for byte in range(sizeBlock):
			mask |= 0xff << byte * 8

		output = int2bytes(block >> argShift | block << compShift & mask)
		sizeOutput = len(output)

		if sizeOutput != sizeBlock:
			for _ in range(sizeBlock - sizeOutput):
				output += bytes((0,))

		return output

	else:
		print('Fatal error (rol): The argument must be a byte type')
		exit()


def rol4Bytes(argBytes: bytes, argShift: int = 1):
	"""Circular shift to the left"""
	argShift %= len(argBytes)

	if isinstance(argBytes, bytes):
		return argBytes[argShift:] + argBytes[:argShift]

	else:
		print('Fatal error (rol4Bytes): The argument must be a byte type')
		exit()


def ror(argBytes: bytes, argShift: int=1):
	"""Circular shift to the right"""
	block = 0
	sizeBlock = len(argBytes)
	argShift %= sizeBlock * 8
	compShift = sizeBlock * 8 - argShift

	if isinstance(argBytes, bytes):
		block = bytes2int(argBytes)
		mask = 0x0

		for byte in range(sizeBlock):
			mask |= 0xff << byte * 8

		output = int2bytes(block << compShift & mask | block >> argShift)
		sizeOutput = len(output)

		if sizeOutput != sizeBlock:
			for _ in range(sizeBlock - sizeOutput):
				output += bytes((0,))

		return output

	else:
		print('Fatal error (ror): The argument must be a byte type')
		exit()


def ror4Bytes(argBytes: bytes, argShift: int = 1):
	"""Circular shift to the right"""
	argShift %= len(argBytes)

	if isinstance(argBytes, bytes):
		return argBytes[-argShift:] + argBytes[:-argShift]

	else:
		print('Fatal error (ror4Bytes): The argument must be a byte type')
		exit()


def xor4bytes(argMsg: bytes, argMask: bytes):
	"""Does the XOR operation on two bytes"""
	output = bytes(m ^ x for m, x in zip(argMsg, argMask[:len(argMsg)]))

	if len(output) != len(argMask):
		print('\tFatal error (xor4bytes): data was lost in the conversion {} vs {}, {}'.format(
			len(output), len(argMsg), len(argMask)))
		return output

	else:
		return output


if __name__ == '__main__':
	from myTools import show_example_of_use

	show_example_of_use(__file__)
	
	varTest = b'1234567890'

	print(activeBits(b'123'))
	
	for i in range(0,256):
		print(bin2Str(i,8), bytes2DecimalPart(i))
	print()
	
	for i in range(20*8 + 1):
		print(f'ror: {i} {ror(varTest, i)}')
	print()

	for i in range(20 + 1):
		print(f'ror4Bytes: {i} {ror4Bytes(varTest, i)}')
	print()

	for i in range(20*8 + 1):
		print(f'rol: {i} {rol(varTest, i)}')
	print()

	for i in range(20 + 1):
		print(f'rol4Bytes: {i} {rol4Bytes(varTest, i)}')
	print()

	print('\ngetByte(varTest,4): {}, type():{}'.format(
		getByte(varTest, 4), type(getByte(varTest, 4))))
	print()

	for i in range(9+1):
		print('replaceByte', i, replaceByte(varTest, b'X', i))
	print()
