"""https://www.hackerrank.com/challenges/cut-the-sticks/copy-from/203196359
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    result = []
    while arr:
        result.append(len(arr))
        m = min(arr)
        arr = [i-m for i in arr if i>m]
        
    return(result)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()