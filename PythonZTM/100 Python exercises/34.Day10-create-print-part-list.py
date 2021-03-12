
"""
Define a function which can generate a list where 
the values are square of numbers between 1 and 20 (both included). Then the function 
needs to print the first 5 elements in the list.
"""

def create_list(n):
  d = [k**2 for k in range(1,n+1)]
  print(d[:5])

create_list(20)


