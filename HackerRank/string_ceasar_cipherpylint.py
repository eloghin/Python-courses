"""
Solve Caesar cipher problem.
"""

import os

# Complete the caesarCipher function below.

def caesar_cipher(s_string, k):
    """
    Caesar cipher function
    """
    result = ''

    for char in s_string:
        if 65 <= ord(char) <= 90:
            result += chr((ord(char) -65 + k)%26 + 65)
        elif 97 <= ord(char) <= 122:
            result += chr((ord(char) -97 + k)%26 + 97)
        else:
            result += char

    return result

if __name__ == '__main__':
    FPTR = open(os.environ['OUTPUT_PATH'], 'w')

    S = input()

    K = int(input())

    R = caesar_cipher(S, K)

    FPTR.write(R + '\n')

    FPTR.close()
