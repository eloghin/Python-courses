"""
Task:
You are given a text of N lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:

    && → and      || → or

Both && and || should have a space " " on both sides.

Input Format:
The first line contains the integer, N.
The next N lines each contain a line of the text.

Constraints:
Neither && nor || occur in the start or end of each line.

Output Format:
Output the modified text."""


# *************
# *** SOl 1****
# *************
import re
N = int(input())

for _ in range(N):
    text = input()
    text = re.sub(" && ", " and ", text)
    text = re.sub(" \|\| ", " or ", text)
    print(text)


# *************
# *** SOl 2 ***
# *************
for _ in range(int(input())):
    line = input()
    
    while ' && ' in line or ' || ' in line:
        line = line.replace(" && ", " and ").replace(" || ", " or ")
    
    print(line)


# *************
# *** SOl 3 ***
# *************
import re

N = int(input())

pattern1 = re.compile(r'(?<= )(&&)(?= )')
pattern2 = re.compile(r'(?<= )(\|\|)(?= )')

for i in range(N):
      print(pattern2.sub('or', pattern1.sub('and', input())))