"""
You are given a string N.
Your task is to verify that N is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

Number can start with +, - or . symbol.
    For example:
    ✔+4.50
    ✔-1.0
    ✔.5
    ✔-.7
    ✔+.4
    ✖ -+4.5

Number must contain at least 1 decimal value.
    For example:
    ✖ 12.
    ✔12.0  

Number must have exactly one . symbol.
Number must not give any exceptions when converted using float(N).
"""

import re

T = int(input())

pattern = re.compile(r"^[-+]?[0-9]*\.[0-9]+$")

for _ in range(T):
    num = input()
    print(bool(pattern.match(num)))
