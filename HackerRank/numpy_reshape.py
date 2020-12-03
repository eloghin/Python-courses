"""
Task: You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.

Input Format: A single line of input containing space separated integers.

Output Format: Print the 3X3 NumPy array.
"""

import numpy

arr = list(map(int, input().split()))

numpy_array = numpy.array(arr, int)

print(numpy.reshape(numpy_array,(3,3)))