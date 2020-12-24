"""
    Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

    Suppose the following input is supplied to the program:
			9

    Then, the output should be:
			11106



"""

# ***********
# ***SOL 1***
# ***********

a = input('Enter the digit:')
sum = 0

for i in range(1,5):
	sum += int(i*a)

print(sum)



# ***********
# ***SOL 2***
# ***********
# a = input('Enter the digit:')

# print(int(a)+int(2*a)+int(3*a)+int(4*a))

# ***********
# ***SOL 3***
# ***********
# a = input('Enter the digit:')

# print(sum(int(i*a) for i in range(1,5)))