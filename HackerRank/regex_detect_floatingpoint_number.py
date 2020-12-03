"""
You are given a string N.
Your task is to verify that is a floating point number. 

Input Format: 
The first line contains an integer T, the number of test cases.
The next T line(s) contains a string N.

Output Format: 
Output True or False for each test case.
"""

import re

T = int(input())

for _ in range (T):
    N = input()
    if bool(re.search(r"[.]", N)): 
        try:
            float(N)
            print(True)
        except ValueError:
            print(False)
    else:
        print("False") 