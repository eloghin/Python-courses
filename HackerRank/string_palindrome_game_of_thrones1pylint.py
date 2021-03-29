"""
 Given a string, determine if it can be rearranged into a palindrome.
 Return the string YES or NO.
"""

#!/bin/python3

import os

# Complete the gameOfThrones function below.
def game_of_thrones(s_string):
    """
    Palindromes longer than 1 character are made up
    of pairs of characters. Function checks this and
    returns YES or NO.
    """
    flag = 0
    s_set = set(s_string)
    if len(s_string) % 2 == 1:
        for char in s_set:
            if s_string.count(char) % 2 == 1:
                if flag:
                    return "NO"
                else:
                    flag += 1
    else:
        for char in s_set:
            if s_string.count(char) % 2 == 1:
                return "NO"

    return "YES"

if __name__ == '__main__':
    FPTR = open(os.environ['OUTPUT_PATH'], 'w')

    S = input()

    R = game_of_thrones(S)

    FPTR.write(R + '\n')

    FPTR.close()
