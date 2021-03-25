""" 
    Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

    Example: If the following n is given as input to the program:

    100

   Then, the output of the program should be:

    0,35,70

"""

n = int(input('n='))

def div5and7(n):
  m = n//35
  for i in range(m+1):
    yield i*35

for value in div5and7(n):
    print(value)