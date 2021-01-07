"""
Louise joined a social networking site to stay in touch with her friends. 
The signup page required her to input a name and a password. However, the password must be strong. 
The website considers a password to be strong if it satisfies the following criteria:

    Its length is at least 6.
    It contains at least one digit.
    It contains at least one lowercase English character.
    It contains at least one uppercase English character.
    It contains at least one special character. The special characters are: !@#$%^&*()-+

She typed a random string of length n in the password field but wasn't sure if it was strong. 
Given the string she typed, can you find the minimum number of characters she must add to make 
her password strong?

Note: Here's the set of types of characters in a form you can paste in your solution:

        numbers = "0123456789"
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        special_characters = "!@#$%^&*()-+"
"""

# ***********
# ** SOL 1 **
# ***********
import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    chars_to_add = 0
    
    if not re.search(r'\d', password):
        chars_to_add += 1

        
    if not re.search(r'[a-z]', password):
        chars_to_add += 1

        
    if not re.search(r'[A-Z]', password):
        chars_to_add += 1

    
    if not re.search(r'[!@#$%^&*()\-+]', password):
        chars_to_add += 1

        
    if n + chars_to_add <= 6:
        return (6-n)
    else:
        return chars_to_add
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
