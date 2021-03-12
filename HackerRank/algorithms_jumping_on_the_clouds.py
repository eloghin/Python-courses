"""https://www.hackerrank.com/challenges/jumping-on-the-clouds/copy-from/203203898
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0
    steps = 0
    
    while i+2 < len(c):
        i = i+1 if c[i+2] else i+2
        steps += 1
        
    if i == len(c)-2:
        steps += 1
        
    return(steps)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()