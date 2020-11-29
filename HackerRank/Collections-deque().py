"""
Perform append, pop, popleft and appendleft methods on an empty deque.

Input Format:
    The first line contains an integer, n, the number of operations.
    The next n lines contains the space separated names of methods and their values.

Print the space separated elements of deque
"""


from collections import deque

d = deque()
n = int(input())

def deque_update(d, method, *args):
    if method == 'append':
        d.append(*args)
        
    elif method == 'pop':
        d.pop()
        
    elif method == 'popleft':
        d.popleft()
        
    elif method == 'appendleft':
        d.appendleft(*args)
        
        
for _ in range(n):
    method, *value = map(str, input().split())
    deque_update(d, method, *value)

print(*d)