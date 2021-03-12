
"""
Define a function which can print a 
dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
"""

def create_dict(n):
  d = {k:k**2 for k in range(1,n+1)}
  print(d)

create_dict(20)
