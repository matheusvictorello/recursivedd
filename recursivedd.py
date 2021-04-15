from functools import partial
from collections import defaultdict
from collections.abc import Callable

class recursivedd(defaultdict):
	def __init__(self, default_factory, dimension, args=[], kwargs={}):
		if not isinstance(default_factory, Callable):
			raise ValueError('first argument must be callable')

		if not isinstance(dimension, int):
			raise ValueError('dimension must be an integer greater or equal to 1')

		if dimension <= 0:
			raise ValueError('dimention must be greater or equal to 1')

		if not isinstance(args, list):
			raise ValueError('args must be a list')

		if not isinstance(kwargs, dict):
			raise ValueError('kwargs must be a dict')

		self.default_factory = default_factory
		self.dimension       = dimension
		self.args            = args
		self.kwargs          = kwargs

	def __missing__(self, key):
		if self.dimension == 1:
			# Builds the final value using the default_factory.
			# The last key, args and kwargs are passed as parameters.
			value = self[key] = self.default_factory(key, *self.args, **self.kwargs)
		else:
			# Creates a recursivedd for that key.
			# His default_factory is a partial with the key, so the key is fixed in place when the default_factory is called.
			default_factory = partial(self.default_factory, key)
			value = self[key] = recursivedd(default_factory, self.dimension - 1, args=self.args, kwargs=self.kwargs)

		return value

rdd = recursivedd