"""
Input Format: 
The first line contains an integer N, the number of inputs.
N lines follow, each containing some string.

Output Format:

For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.
"""
import re

n = int(input())

for _ in range(n):
    m = re.match(r'^[789][\d]{9,9}$', input())
    if m:
        print("YES")
    else:
        print("NO")