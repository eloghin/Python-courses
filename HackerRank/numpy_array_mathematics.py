"""
Task: You are given two integer arrays, A and B of dimensions nxm.
Your task is to perform the following operations:

1. Add (A+B)
2. Subtract (A-B)
3. Multiply (A*B)
4. Integer Division (A/B)
5. Mod (A%B)
6. Power (A**B)

Note: There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.

Input Format: 
The first line contains two space separated integers, n and m.
The next lines contains space separated integers of array A.
The following lines contains space separated integers of array B.

Output Format: Print the result of each operation in the given order under Task.
"""

import numpy

n, m = map(int, input().split())

A = numpy.array([input().split() for _ in range(n)], int)
B = numpy.array([input().split() for _ in range(n)], int)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)