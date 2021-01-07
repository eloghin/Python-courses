"""Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

Function Description

Complete the caesarCipher function in the editor below.

caesarCipher has the following parameter(s):

    string s: cleartext
    int k: the alphabet rotation factor

Returns

    string: the encrypted string

Input Format

The first line contains the integer, n, the length of the unencrypted string.
The second line contains the unencrypted string, s.
The third line contains k, the number of letters to rotate the alphabet by.

Sample Input
        11
        middle-Outz
        2

Sample Output
        okffng-Qwvb
"""

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    result = ''
    
    for char in s:
        if 65 <= ord(char) <= 90:
            result += chr((ord(char) -65 + k)%26 + 65)
        elif 97 <= ord(char) <= 122:
            result += chr((ord(char) -97 + k)%26 + 97)
        else:
            result += char
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
