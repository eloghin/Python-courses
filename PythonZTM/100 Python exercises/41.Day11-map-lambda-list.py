"""
Write a program which can map() to make a list whose elements are square of 
elements in [1,2,3,4,5,6,7,8,9,10].
"""

def map_func(l):
  m = map(lambda x:x*x, l)
  return list(m)

print(map_func([1,2,3,4,5,6,7,8,9,10]))
