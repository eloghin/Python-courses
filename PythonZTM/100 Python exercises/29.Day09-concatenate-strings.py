
"""
Define a function that can accept two strings as input and concatenate them and then print it in console.
"""

def concat_string(a, b):
  print(a+b)

concat_string('I am ', 'king')

concat_string2 = lambda a,b: a + b
print(concat_string2('hello','pisi'))
