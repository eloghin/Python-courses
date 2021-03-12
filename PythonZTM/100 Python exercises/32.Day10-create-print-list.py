
"""
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
"""
def create_list(n):
  d = [k**2 for k in range(1,n+1)]
  print(d)

create_list(20)
