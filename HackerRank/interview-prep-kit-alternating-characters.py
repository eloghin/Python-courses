""" 
    You are given a string containing characters A and B only. 
    Your task is to change it into a string such that there are 
    no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

	Your task is to find the minimum number of required deletions.

	https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    l = len(set(s))
    if l == 1:
        return (len(s)-1)
    
    s_list = list(s)
    i, count = 0, 0
    
    while i != len(s_list)-1:
        if s_list[i] == s_list[i+1]:
            s_list.remove(s_list[i])
            count += 1
        else:
            i += 1    
            
    return(count)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()