import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    arr.sort(key=lambda x: x[k])
    
    for item in arr:
        # print(" ".join(map(str, item))) 
        print(*item, sep=" ")
        """
        * written in front of apples causes apples to be unpacked in items 
        and converted into a string, then these items are combined with value 
        which is specified in the sep keyword.
        
        If you just want to separate the items and print a list without the brackets
        and single quotes, then you don’t need to specify the value of sep because 
        it has a default value of whitespace.
