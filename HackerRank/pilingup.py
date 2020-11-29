# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical 
pile of cubes. The new pile should follow these directions: if cubei is on top of cubej then sideLengthj>=sideLengthi. 

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. 
Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

Input Format

The first line contains a single integer, T, the number of test cases.
For each test case, there are lines.
The first line of each test case contains , the number of cubes.
The second line contains space separated integers, denoting the sideLengths of each cube in that order. 
"""

from collections import deque

T = int(input())

for _ in range(T):

    n = int(input())
    d = deque(map(int, input().split()))
    top_of_pile = max(d[0],d[len(d)-1])
    print(len(d))

    while len(d) > 0 and top_of_pile >= max(d[0],d[len(d)-1]):

        if d[0] >= d[len(d)-1]:
            top_of_pile = d[0]
            d.popleft()
            print(f'd.popleft:{d}')

        else:
            top_of_pile = d[len(d)-1]
            d.pop()
            print(f'd.pop:{d}')


    if len(d) == 0:
        print("Yes")
    else:
        print("No")
