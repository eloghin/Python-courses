"""
Write a program which can compute the factorial of a given number.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320
"""


n = int(input())

#**************
# Using for loop
#**************

# def createDict(x):
#   d = dict()
#   for i in range(1, x+1):
#     d[i] = i**2
#   return d

# print(createDict(n))

#**************
# Using dict comprehension
#**************

d = {i:i**2 for i in range(1, n+1)}
  
print(d)