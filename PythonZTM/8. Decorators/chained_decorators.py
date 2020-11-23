from time import time
from functools import wraps

def performance(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		t1 = time()
		result = func(*args, **kwargs)
		t2 = time()
		print(f'{func.__name__} ran in {t2-t1} sec')
		return result
	return wrapper


def my_logger(func):
	import logging
	logging.basicConfig(filename='{}.log'.format(func.__name__), level= logging.INFO)

	@wraps(func)
	def wrapper(*args, **kwargs):
		logging.info(
			'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
		return func(*args, **kwargs)
		
	return wrapper

@my_logger
@performance
def display_info(name, age):
	print(f'display_info ran with arguments ({name}, {age})')

display_info('Anna', 20)	