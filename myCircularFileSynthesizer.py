# -*- coding: utf-8 -*-
"""Circular file handling class"""

__author__ = 'M. en C. Carlos Enrique Quijano Tapia (kike.qt@gmail.com)'
__copyright__ = "(c) Carlos Enrique Quijano Tapia 2018"
__credits__ = ""

__licence__ = "GPLv3"
__version__ = "$Version: 0 Revision: 4 Since: 08/06/2020"
__maintainer__ = "Carlos Enrique Quijano Tapia"
__email__ = "kike.qt@gmail.com"
__status__ = "Developing"

# $Source$
from Crypto.Cipher import AES
from hashlib import sha512 as defaultHash
from hashlib import sha256 as cryptHash
from os import path

from myBytesTools import bytes2int
from myBytesTools import int2bytes


class Circular_File_Synthesizer(object):
	"""Circular files synthesizer

	This class will take care of traversing the whole set of files indicated as a
	ring, for it will load the content of said files in the memory.
	"""

	__skipped_positions = 0
	__data_raw = b''
	__file_list = []
	__flag_periodical_makeover = False  # Only for test
	__flag_make_XOR = False
	__len_data = None
	__position_in_data = 0
	__previous_data = 0
	__seed = defaultHash()

	def __init__(self, argFilesList: list):
		"""Build the object and receive the list of circular files"""
		self.__set_data(argFilesList[:])

	def __periodical_makeover(self) -> None:
		"""Flag to encrypt in each cycle"""
		if self.__flag_periodical_makeover:
			if self.__skipped_positions > self.__len_data:
				self.__skipped_positions = 0
				self.makeover()

	def __set_data(self, argFilesList) -> None:
		if f"{type(argFilesList)}" in ["<class 'list'>", "<class 'tuple'>"]:
			self.__file_list = argFilesList[:]
			self.__pos = 0

			# Sizes of files
			for fn in argFilesList:
				with open(fn, mode='rb') as file:
					self.__data_raw += file.read(path.getsize(fn))

			self.__len_data = len(self.__data_raw)

		else:
			print('Fatal error: A list or tuple of files must be provided')
			print(f'{type(argFilesList)} <{argFilesList}>')


	def __XORize(self, argBytes: bytes) -> bytes:
		"""Execute the XOR operation between argBytes and __previous_data if
		__flag_make_XOR is active, otherwise return the original value
		"""
		if self.__flag_make_XOR:
			newBytes = []

			for cByte in argBytes:
				self.__previous_data ^= cByte
				newBytes.append(self.__previous_data)
			
			return bytes(newBytes)
		
		else:
			return argBytes

	def __read_hash_like_integer(self):
		"""Same as readInt but first get the hash"""
		self.__seed.update(self.readInBytes(4))
		integer_value = bytes2int(self.__seed.digest()) % 2 ** 32

		return integer_value

	def makeover(self) -> None:
		"""Encrypt data
		
		Note: This method is only public for testing purposes, in a final
		implementation it should be private.
		"""
		self.__seed.update(self.readInBytes(4))
		key = cryptHash(self.__seed.digest())
		nonce = self.__seed.digest()[:15]

		cipher = AES.new(key.digest(), AES.MODE_OCB, nonce=nonce)

		self.__data_raw = cipher.encrypt(self.__data_raw)

	def jumpPositions(self, argJumpPositions: int=1) -> None:
		"""Skip the positions indicated in the parameter

		If you skip a position, a negative number will indicate a setback
		"""
		if argJumpPositions < 0:
			self.__position_in_data += argJumpPositions

			while self.__position_in_data < 0:
				self.__position_in_data += self.__len_data

		else:
			self.__position_in_data = (self.__position_in_data + argJumpPositions) % self.__len_data

	def readInBytes(self, argSize: int=1) -> bytes:
		"""readInBytes

		Read the indicated amount of data, if it is omitted it will only read one
		byte, a negative number indicates the reading of previous data
		"""
		myBytesReturn = b''
		self.__periodical_makeover()

		if argSize < 0:
			# If negative, move the position pointer back
			self.jumpPositions(argSize)
			argSize *= -1

		if self.__position_in_data + argSize <= self.__len_data:
			# The current reading does NOT reach the end of __data_raw
			myBytesReturn = self.__data_raw[self.__position_in_data: self.__position_in_data + argSize]
			self.__position_in_data += argSize

		else:
			# The current reading reaches the end of __data_raw
			myBytesReturn += self.__data_raw[self.__position_in_data:]
			self.__position_in_data += argSize - self.__len_data

			# We read by parts
			while self.__position_in_data >= self.__len_data:
				myBytesReturn += self.__data_raw[:]
				self.__position_in_data -= self.__len_data

			myBytesReturn += self.__data_raw[0: self.__position_in_data]

		self.__skipped_positions += argSize

		return self.__XORize(myBytesReturn)

	@property
	def readInt(self) -> int:
		"""Read 4 bytes of the circular file and return an integer"""
		return bytes2int(self.readInBytes(4))

	@property
	def readHashLikeInteger(self) -> int:
		"""Same as readInt but first get the hash"""
		return self.__read_hash_like_integer()

	def periodicalMakeover(self, argStatus = True) -> None:
		"""Enable encrypt by cycle

		Note: This method is only for testing purposes, in a final
		implementation it should be deleted.
		"""
		self.__flag_periodical_makeover = argStatus

		if argStatus:
			self.__skipped_positions = 0

	@property
	def seed(self):
		return self.__seed.digest()

	@seed.setter
	def seed(self, argBytesSeed: bytes) -> None:
		"""Fix or update the seed with the bytes it receives"""
		self.__seed.update(argBytesSeed)
		self.__seed.update(self.__data_raw)
		self.jumpPositions(self.__read_hash_like_integer() % len(self.__data_raw))

	def turnXORize(self) -> None:
		"""Inverts the value of the variable __flag_make_XOR, that is, it turns it on
		if it is turned off and vice versa
		"""
		self.__flag_make_XOR = not self.__flag_make_XOR

	def turnOnXORize(self) -> None:
		"""Turn ON the mode XOR"""
		self.__flag_make_XOR = True

	def turnOffXORize(self) -> None:
		"""Turn OFF the mode XOR"""
		self.__flag_make_XOR = False
		

if __name__ == '__main__':
	"""Example of use"""
	from os import system

	system('cls')

	cfs = Circular_File_Synthesizer(['myCircularFileSynthesizer.py'])
	key = b'12345678'

	print(f"key:                    {key}")
	cfs.seed = key

	# print(f'cfs.files:            {cfs.files}')
	print(f'cfs.readInBytes(10):    {cfs.readInBytes(10)}')
	cfs.jumpPositions(-10)
	print('cfs.jumpPositions(-10)')
	print(f'cfs.readInBytes(10):    {cfs.readInBytes(10)}')
	print(f'cfs.readInBytes(-10):   {cfs.readInBytes(-10)}\n')
	cfs.jumpPositions(-10)

	print('cfs.turnXORize():       ON')
	cfs.turnXORize()
	print(f'cfs.readInBytes(10):    {cfs.readInBytes(10)}')
	print('cfs.jumpPositions(-10)')
	cfs.jumpPositions(-10)
	print('cfs.turnXORize():       OFF')
	cfs.turnXORize()
	print(f'cfs.readInBytes(10):    {cfs.readInBytes(10)}\n')
	cfs.jumpPositions(-10)

	print(f'cfs.readInt:            {cfs.readInt}')
	print('cfs.jumpPositions(-4)')
	cfs.jumpPositions(-4)
	print(f'cfs.readHashLikeInteger {cfs.readHashLikeInteger}\n')
	cfs.jumpPositions(-4)

	# print('Raw')
	# print(f'cfs.data[:20]:          {cfs.data[:20]}')
	# print(f'cfs.data[:20].hex():    {cfs.data[:20].hex()}\n')

	# cfs.makeover()
	# print('cfs.makeover()')
	# cfs.jumpPositions(-50)
	# print(f'cfs.data[:20]:          {cfs.data[:20]}')
	# cfs.jumpPositions(-50)
	# print(f'cfs.data[:20].hex():    {cfs.data[:20].hex()}')

	# validation = defaultHash()
	# validation.update(cfs.data)
	# print(f'hash(cfs.data)[:40]:    {validation.digest().hex()[:40]}\n')
