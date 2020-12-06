"""
Define a class which has at least two methods:

        getString: to get a string from console input
        printString: to print the string in upper case.

    Also please include simple test function to test the class methods.
"""
# **********
# **SOL 1 **
# **********
# import math

# C, H = 50, 30

# D = input().split(',')

# SQ = [round(math.sqrt(2*C*int(d)/H)) for d in D]

# print(','.join(str(x) for x in SQ))

# **********
# **SOL 2 **
# **********
my_list = [int(x) for x in input('').split(',')]
C, H, x = 50, 30, []

for D in my_list:
    Q = ((2*C*D)/H)**(1/2)
    x.append(round(Q))

# print(','.join(map(str, x)))
print(','.join(str(i) for i in x))