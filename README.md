# recursivedd
Recursive 'defaultdict from collections'


```python
def factory(firestKey, secondKey, thirdKey, *args, **kwargs):
	return {
		'firestKey' : firestKey,
		'secondKey' : secondKey,
		'thirdKey'  : thirdKey,
		'args'      : args,
		'kwargs'    : kwargs
	}

d = rdd(factory, dimension=3, args=[999], kwargs={'number' : 42})

print(d[1][2][3])
# {
# 	'firestKey': 1,
# 	'secondKey': 2,
# 	'thirdKey': 3,
# 	'args': (999,),
# 	'kwargs': {
# 		'number': 42
# 	}
# }

print(d['a']['b']['c'])
# {
# 	'firestKey': 'a',
# 	'secondKey': 'b',
# 	'thirdKey' : 'c',
# 	'args'     : (999,),
# 	'kwargs'   : {
# 		'number': 42
# 	}
# }

print(d[factory][True][False])
# {
# 	'firestKey': <function factory at 0x0000000123456789>,
# 	'secondKey': False,
# 	'thirdKey' : None,
# 	'args'     : (999,),
# 	'kwargs'   : {
# 		'number': 42
# 	}
# }
```
