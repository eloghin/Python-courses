"""
	Check password:
		- at least 8 char long
		- contain anu sort of letters, numbers, $%#@
		- has to end with a number
"""

import re

pattern = re.compile(r"[a-zA-Z0-9$%#@]{7,}\d$")

password = input('What\'s your password?')

if pattern.search(password):
	print('Good password!')
else:
	print('Password does not meet all the criteria')
