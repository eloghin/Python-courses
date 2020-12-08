"""
    Write a program that accepts sequence of lines as input and prints the lines after 
    making all characters in the sentence uppercase.

    Suppose the following input is supplied to the program:

			Hello world
			Practice makes perfect

    Then, the output should be:

			HELLO WORLD
			PRACTICE MAKES PERFECT




"""
# **********
# **SOL 1 **
# **********
import sys
msg = sys.stdin.readlines()

for item in msg:
  print(*(item.upper().splitlines()))

# **********
# **SOL 2 **
# **********

def user_input():
    while True:
        s = input()
        if not s:
            return
        yield s

for line in map(str.upper, user_input()):
    print(line)