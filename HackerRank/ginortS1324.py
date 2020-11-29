"""
You are given a string .
contains alphanumeric characters only.
Your task is to sort the string in the following manner:

    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.
"""

#********
#**SOL1**
#********

# S = Sorting1234
# a = list(S)
# a[:] = sorted([x for x in S if x.islower()]) + \
#         sorted([x for x in S if x.isupper()]) + \
#         sorted([x for x in S if (x.isdigit() and int(x)%2==1)]) + \
#         sorted([x for x in S if (x.isdigit() and int(x)%2==0)])
# print(*a, sep='')
# # print(*S, sep='')


#********
#**SOL2**
#********
S = Sorting1234
print(*(sorted(S, key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')

# 1. if isdigit, give higher priority. so alphas come before digits now
# Ex- Sorting1234 => Sorting1234

# 2. if isevendigit, give higher priority. so, among the digits, now even have higher priority. While the 1st part in key is maintained
# Ex- Sorting1234 => Sorting1324

# 3. next priority goes to upper case keeping both previous keys maintained. so uppercase can't go after the numbers as that key has higher priority.
# Ex - Sorting1234 => ortingS1324

# 4. next priority is given to lowercase characters, but that isn't required as it's the only ones left in alphanumeric characters. We will get the same output either way
# Ex - Sorting1234 => ortingS1324

# 5. now sort according to the characters, but keeping all the previous keys in mind, all the characters will be sorted in place, keeping their order as defined in previous keys
# Ex - Sorting1234 => ginortS1324
