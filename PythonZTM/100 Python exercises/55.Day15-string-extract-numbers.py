"""
    Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

    Example: If the following words is given as input to the program:

    2 cats and 3 dogs.

    Then, the output of the program should be:

    ['2', '3']

"""

import re

words = '2 cats and 3 dogs'

# SOLUTION 1
pattern = "\d+"
ans = re.findall(pattern,words)
print(ans)

# SOLUTION 2
w = words.split()
ans = []
for word in words:
    if word.isdigit():     # can also use isnumeric() / isdecimal() function instead
       ans.append(word)
print(ans)

# SOLUTION 3
ans = [word for word in w if word.isdigit()]
print(ans)