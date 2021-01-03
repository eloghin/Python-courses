"""
A valid email address meets the following criteria:

    It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
    The username starts with an English alphabetical character, and any subsequent characters consist of one 
    or more of the following: alphanumeric characters, -,., and _.
    The domain and extension contain only English alphabetical characters.
    The extension is 1,2 or 3 characters in length.

Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.
"""

import re

pattern = re.compile(r"<[a-z][-._0-9a-z]*@[a-z]+\.[a-z]{1,3}>")

n = int(input())

for _ in range(n):
    S = input()
    if pattern.search(S):
        print(S)
