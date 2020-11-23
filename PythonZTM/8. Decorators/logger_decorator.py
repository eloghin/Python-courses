def my_logger(func):
	import logging
	logging.basicConfig(filename='{}.log'.format(func.__name__), level= logging.INFO)

	def wrapper(*args, **kwargs):
		logging.info(
			'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
		return func(*args, **kwargs)
		
	return wrapper

@my_logger
def display_info(name, age):
	print(f'display_info ran with arguments ({name}, {age})')

display_info('Anna', 20)	