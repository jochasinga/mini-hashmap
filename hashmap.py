import hashlib
from collections import deque


class HashMap(object):

	def __init__(self, size = 100):
		"""

		Create a HashMap object. size default to 100. Anywhere less
		than that is very likely to get high collisions.

		"""
		if size is not None:
			self._array = [deque() for x in range(size)]
		else:
			raise ValueError('size cannot be None (default = 100)')

		self.size = size


	def _keytoindex(self, key):
		"""

		Compute the index of the array based on the modulo of the 
		md5 digest of the key and the hashmap's array's length.

		"""
		m = hashlib.md5()
		m.update(key)
		long_number = int(m.hexdigest(), 16)
		print('long_number {}'.format(long_number))
		index = long_number % len(self._array)
		print('index {}'.format(index))

		return index


	def put(self, key, val):
		"""

		Save the value into the hashmap entry and delete
		the value with a duplicate key.

		TODO: Create a sub list of the past versions of values
		with duplicate keys instead of deleting them.

		"""
		i = self._keytoindex(key)

		# This will never happen
		# if i > len(self._array):
		# 	new_arr = [deque() for x in range(self.size)]
		# 	old_arr = self._array
		# 	self._array = old_arr + new_arr

		q = self._array[i]

		# check if there's duplicate key and delete the data
		index_to_del = None
		for i, item in enumerate(q):
			if key in item:
				index_to_del = i

		if index_to_del is not None:
			del q[index_to_del]

		# key can probably be hashed as string
		q.appendleft((key, val))

	def get(self, key):
		index = self._keytoindex(key)

		if index > len(self._array):
			raise IndexError
		else:
			q = self._array[index]
			for item in q:
				if item[0] == key:
					return item[1]
		
		return None					