"""
 Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, s, 
 determine how many letters of the SOS message have been changed by radiation.
"""

#!/bin/python3

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    letter_s = s[::3].count("S") + s[2::3].count("S")
    letter_o = s[1::3].count("O")
    
    return len(s) - (letter_s + letter_o)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
