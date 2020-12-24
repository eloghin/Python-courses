"""
    Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

    Suppose the following input is supplied to the program:

Hello world!

    Then, the output should be:

UPPER CASE 1
LOWER CASE 9


"""

# ***********
# ***SOL 1***
# ***********
# sentence = input('Enter the sentence:')

# upper_letter = 0
# lower_letter = 0

# for char in sentence:
#   if char.isalpha():
#   	if char == char.lower():
#   		lower_letter += 1
#   	else:
#   		upper_letter += 1


# print('UPPER: ', upper_letter)
# print('LOWER: ', lower_letter)

# ***********
# ***SOL 2***
# ***********
sentence = input('Enter the sentence:')

upper_letter = 0
lower_letter = 0

for char in sentence:
  	lower_letter += char.islower()
  	upper_letter += char.isupper()

print('UPPER: ', upper_letter)
print('LOWER: ', lower_letter)
