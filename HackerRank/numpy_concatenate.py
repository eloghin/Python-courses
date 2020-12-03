"""
Task: You are given two integer arrays of size NxP and MxP (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.

Input Format: 
The first line contains space separated integers N, M and P.
The next N lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.

Output Format: Print the concatenated array of size (N+M)xP.
"""

import numpy

n, m, p = map(int, input().split())

array_np = numpy.array([input().split() for _ in range(n)], int)
array_mp = numpy.array([input().split() for _ in range(m)], int)

print(numpy.concatenate((array_np, array_mp), axis =0))