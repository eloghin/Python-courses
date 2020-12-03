"""
Task: Your task is to print an array of size nxm with its main diagonal elements as 1's and 0's everywhere else.

Note: In order to get alignment correct, please insert the line numpy.set_printoptions(legacy='1.13') below the numpy import.

Input Format: A single line containing the space separated values of n and m.
n denotes the rows.
m denotes the columns.

Output Format: Print the desired nxm array.
"""

import numpy
numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())

print(numpy.eye(n,m))