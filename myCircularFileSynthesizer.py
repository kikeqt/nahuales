__version__ = "$Version: 1.1.0"

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
	_skipped_positions = 0
	_data_raw = b''
	_file_list = []
	_flag_periodical_makeover = None
	_flag_make_XOR = None
	_len_data = None
	_position_in_data = 0
	_previous_data = 0
	_seed = defaultHash()

	def __init__(self, file_list: list, key:str, xorize=True, makeover=True,
				periodical_makeover=True,):
		"""Build the object and receive the list of circular files"""
		self._flag_make_XOR = xorize
		self._flag_periodical_makeover = periodical_makeover

		self._set_data(file_list[:])

		self._seed.update(key)

		if makeover:
			self.makeover()

	def _periodical_makeover(self):
		"""Flag to encrypt in each cycle"""
		if self._flag_periodical_makeover:
			if self._skipped_positions > self._len_data:
				self._skipped_positions = 0
				self.makeover()

	def _set_data(self, files_list):
		if f"{type(files_list)}" in ["<class 'list'>", "<class 'tuple'>"]:
			self._file_list = files_list[:]
			self._pos = 0

			# Sizes of files
			for fn in files_list:
				with open(fn, mode='rb') as file:
					self._data_raw += file.read(path.getsize(fn))

			self._len_data = len(self._data_raw)

		else:
			print('Fatal error: A list or tuple of files must be provided')
			print(f'{type(files_list)} <{files_list}>')


	def _XORize(self, byte_data: bytes):
		"""Execute the XOR operation between byte_data and _previous_data if
		_flag_make_XOR is active, otherwise return the original value
		"""
		if self._flag_make_XOR:
			newBytes = []

			for cByte in byte_data:
				self._previous_data ^= cByte
				newBytes.append(self._previous_data)
			
			return bytes(newBytes)
		
		else:
			return byte_data

	@property
	def data(self):
		return self._data_raw

	def _read_hash_like_integer(self):
		"""Same as readInt but first get the hash"""
		self._seed.update(self.readInBytes(4))
		integer_value = bytes2int(self._seed.digest()) % 2 ** 32

		return integer_value

	def makeover(self):
		"""Encrypt data
		
		Note: This method is only public for testing purposes, in a final
		implementation it should be private.
		"""
		self._seed.update(self.readInBytes(4))
		key = cryptHash(self._seed.digest())
		nonce = self._seed.digest()[:15]

		# This configuration was arbitrarily chosen, but nothing prevents choosing another
		# There is still a solution to be implemented to alternate the configuration
		cipher = AES.new(key.digest(), AES.MODE_OCB, nonce=nonce)

		self._data_raw = cipher.encrypt(self._data_raw)
  
  		# It could be reduced by the configuration of the block cipher
		if self._len_data == len(self._data_raw):
			self._len_data = len(self._data_raw)

	def jumpPositions(self, jump_positions: int=1):
		"""Skip the positions indicated in the parameter

		If you skip a position, a negative number will indicate a setback
		"""
		if jump_positions < 0:
			self._position_in_data += jump_positions

			while self._position_in_data < 0:
				self._position_in_data += self._len_data

		else:
			self._position_in_data = (self._position_in_data + jump_positions) % self._len_data

	def readInBytes(self, required_bytes: int = 1):
		"""readInBytes

		Read the indicated amount of data, if it is omitted it will only read one
		byte, a negative number indicates the reading of previous data
		"""
		delivery_bytes = b''
		self._periodical_makeover()

		if required_bytes < 0:
			# If negative, move the position pointer back
			self.jumpPositions(required_bytes)
			required_bytes *= -1

		if self._position_in_data + required_bytes <= self._len_data:
			# The current reading does NOT reach the end of _data_raw
			delivery_bytes = self._data_raw[self._position_in_data :
                                  self._position_in_data + required_bytes]
			self._position_in_data += required_bytes

		else:
			# The current reading reaches the end of _data_raw
			delivery_bytes += self._data_raw[self._position_in_data:]
			self._position_in_data += required_bytes - self._len_data

			# We read by parts
			while self._position_in_data >= self._len_data:
				delivery_bytes += self._data_raw[:]
				self._position_in_data -= self._len_data

			delivery_bytes += self._data_raw[0:self._position_in_data]

		self._skipped_positions += required_bytes

		return self._XORize(delivery_bytes)

	@property
	def readInt(self):
		"""Read 4 bytes of the circular file and return an integer"""
		return bytes2int(self.readInBytes(4))

	def readIntInterval(self, minimum_number: int=0, maximum_number: int=2**32-1):
		return self.readInt % (maximum_number - minimum_number) + minimum_number 

	@property
	def readHashLikeInteger(self):
		"""Same as readInt but first get the hash"""
		return self._read_hash_like_integer()

	def readHaskLikeIntegerInterval(self, minimum_number: int=0, maximum_number: int=2**32-1):
		return self._read_hash_like_integer() % (maximum_number - minimum_number) + minimum_number 

	@property
	def seed(self):
		return self._seed.digest()

	@seed.setter
	def seed(self, seed_bytes: bytes):
		"""Fix or update the seed with the bytes it receives"""
		self._seed.update(seed_bytes)
		self._seed.update(self._data_raw)
		self.jumpPositions(self._read_hash_like_integer() % len(self._data_raw))
		

if __name__ == '__main__':
	"""Example of use"""
	from myTools import show_example_of_use

	show_example_of_use(__file__)

	key = b'12345678'
	file_list = ['myCircularFileSynthesizer.py']
	print(f'key:                             {key}\n')
	jump_size = 25
 
	cfs = Circular_File_Synthesizer(file_list, key)
	print(f'cfs.readInBytes({jump_size}):    {cfs.readInBytes(jump_size)}')
	print(f'cfs.jumpPositions(-{jump_size})'); cfs.jumpPositions(-jump_size)
	print(f'cfs.readInBytes({jump_size}):    {cfs.readInBytes(jump_size)}')
	print(f'cfs.readInBytes(-{jump_size}):   {cfs.readInBytes(-jump_size)}')
	print(f'cfs.readIntInterval(10,99): {cfs.readIntInterval(10,99)}')
	print(f'cfs.readHaskLikeIntegerInterval(10,99): {cfs.readHaskLikeIntegerInterval(10,99)}\n')
 
	cfs = Circular_File_Synthesizer(file_list, key, makeover=False, periodical_makeover=False)
	print(f'cfs.readInBytes({jump_size}):    {cfs.readInBytes(jump_size)}')
	print(f'cfs.jumpPositions(-{jump_size})'); cfs.jumpPositions(-jump_size)
	print(f'cfs.readInBytes({jump_size}):    {cfs.readInBytes(jump_size)}')
	print(f'cfs.readInBytes(-{jump_size}):   {cfs.readInBytes(-jump_size)}')
	print(f'cfs.readIntInterval(10,99): {cfs.readIntInterval(10,99)}')
	print(f'cfs.readHaskLikeIntegerInterval(10,99): {cfs.readHaskLikeIntegerInterval(10,99)}\n')
 
	cfs = Circular_File_Synthesizer(file_list, key, xorize=False, makeover=False, periodical_makeover=False)
	print(f'cfs.readInBytes({jump_size}):    {cfs.readInBytes(jump_size)}')
	print(f'cfs.jumpPositions(-{jump_size})'); cfs.jumpPositions(-jump_size)
	print(f'cfs.readInBytes({jump_size}):    {cfs.readInBytes(jump_size)}')
	print(f'cfs.readInBytes(-{jump_size}):   {cfs.readInBytes(-jump_size)}')
	print(f'cfs.readIntInterval(10,99): {cfs.readIntInterval(10,99)}')
	print(f'cfs.readHaskLikeIntegerInterval(10,99): {cfs.readHaskLikeIntegerInterval(10,99)}\n')

	print('Raw')
	print(f'cfs.data[:{jump_size}]:          {cfs.data[:jump_size]}')
	print(f'cfs.data[:{jump_size}].hex():    {cfs.data[:jump_size].hex()}\n')

	validation = defaultHash()
	validation.update(cfs.data)
	print(f'hash(cfs.data)[:{jump_size}]:    {validation.digest().hex()[:jump_size]}\n')
