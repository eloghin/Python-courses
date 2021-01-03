"""
You are given a string S.
Your task is to find the indices of the start and end of string k in S.
(find all the appearances of k, also overlapping)
Print (-1,-1) if no match is found
Print the start and the end positions of every match. 
"""
# ***********
# ***SOL 1***
# ***********
import re

S = input()

k = input()

matches = list(re.finditer("(?=(%s))"%k,S))

if not matches:
    print((-1,-1))
else:
    for m in matches:
        print((m.start(), m.start()+len(k)-1))

        

# ***********
# ***SOL 2***
# ***********
import re

S = input()

k = input()

matches = list(re.finditer("(?=(%s))"%k,S))

if not matches:
    print((-1,-1))
else:
    for m in matches:
        print((m.start(1), m.end(1))