
"""
Define a function which can generate and print 
a tuple where the value are 
square of numbers between 1 and 20 (both included).
"""

def create_tuple(n):
  d = (k**2 for k in range(1,n+1))
  print(d)

create_tuple(20)


