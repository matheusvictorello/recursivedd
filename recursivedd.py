from collections import defaultdict
from collections.abc import Callable

class recursivedd(defaultdict):
	def __init__(self, default_factory, dimention=1, args=[]):
		if not isinstance(default_factory, Callable):
			raise ValueError('first argument must be callable')

		if dimention <= 0:
			raise ValueError('dimention must be 1 or greater')

		if not isinstance(args, list):
			raise ValueError('args must be a list')

		self.default_factory = default_factory
		self.dimention = dimention
		self.args = args.copy()

	def __missing__(self, key):
		if self.dimention == 1:
			if self.default_factory:
				ret = self[key] = self.default_factory(*self.args, key)
			else:
				raise KeyError(key)
		else:
			ret = self[key] = recursivedd(self.default_factory, self.dimention-1, [*self.args, key])
		
		return ret

	def __repr__(self):
		dict_repr = ', '.join([f"{repr(key)} : {repr(item)}" for key, item in self.items()])
		return f"recursivedd({self.default_factory}, dimention={self.dimention}, args={self.args}, {{{dict_repr}}})"

rdd = recursivedd