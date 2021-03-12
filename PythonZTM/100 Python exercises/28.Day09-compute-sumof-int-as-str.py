
"""
Define a function that can receive two integer numbers in string form and compute their sum 
and then print it in console.
"""

def sum_string_to_int(a, b):
  return(int(a)+int(b))

print(sum_string_to_int('1', '3'))


convert_and_sum = lambda a,b: int(a) + int(b)
print(convert_and_sum('45','20'))
