"""
You are given N lines of CSS code. 
Your task is to print all valid Hex Color Codes, 
in order of their occurrence from top to bottom. 
"""

import re
pattern = re.compile(r"[#]([0-9A-Fa-f]{3}){1,2}[;,\)]")

N = int(input())

for _ in range(N):
    line = input()
    
    for match in re.finditer(pattern, line):
        s = match.start()
        e = match.end()-1
        print(line[s:e])