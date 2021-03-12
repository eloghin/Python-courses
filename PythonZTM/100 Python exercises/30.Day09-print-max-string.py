
"""
Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print all strings line by line.
"""

def max_string(a, b):
  if len(a) > len(b):
  	print(a)
  elif len(b > len(a)):
  	print(b)
  else:
  	print(a)
  	print(b)

max_string('Bucuresti', 'Iasi')

func = lambda a,b: print(max((a,b),key=len)) if len(a)!=len(b) else print(a+'\n'+b)

func('Roma', 'Iasi')
