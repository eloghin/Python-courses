"""
	Check email address format
"""

import re

pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

email = input('What\'s your email address?')

if pattern.search(email):
	print('Good email!')
else:
	print('Wrong email format. Please check again!')
