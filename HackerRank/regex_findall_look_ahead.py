"""
Task
You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only.

Note :
Vowels are defined as: AEIOU and aeiou.
Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

Input Format:

A single line of input containing string S.

Output Format:

Print the matched substrings in their order of occurrence on separate lines.
If no match is found, print -1.

Sample Input:

    rabcdeefgyYhFjkIoomnpOeorteeeeet

Sample Output:

    ee
    Ioo
    Oeo
    eeeee

"""

import re

S = input()

p = re.compile(r'(?=[bcdfghjklmnpqrstvwxyzBCDFGJKLMNPQRSTVWXYZ]([aeiouAEIOU]{2,})[bcdfghjklmnpqrstvwxyzBCDFGJKLMNPQRSTVWXYZ])')

m = p.findall(S)

if m:
    print(*m, sep="\n")
else:
    print("-1")