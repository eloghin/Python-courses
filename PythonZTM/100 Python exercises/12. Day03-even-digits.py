"""     Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.The numbers obtained should be printed in a 
comma-separated sequence on a single line.
"""
# ***********
# ** SOL 1 **
# ***********

def check_even(digit):
  if digit%2 == 0:
    return True
  return False

for j in range(1000, 3001):
  i = str(j)
  if check_even(int(i[0])) and check_even(int(i[1])) and check_even(int(i[2])) and check_even(int(i[3])):
    print(j, end=",")

# ***********
# ** SOL 2 **
# ***********

lst = []

for i in range(1000,3001):
    flag = 1
    for j in str(i):          # every integer number i is converted into string
        if ord(j)%2 != 0:     # ord returns ASCII value and j is every digit of i
            flag = 0          # flag becomes zero if any odd digit found
    if flag == 1:
        lst.append(str(i))    # i is stored in list as string

print(",".join(lst))

# ***********
# ** SOL 3 **
# ***********

def check(element):
    return all(ord(i)%2 == 0 for i in element)  # all returns True if all digits i is even in element

lst = [str(i) for i in range(1000,3001)]        # creates list of all given numbers with string data type
lst = list(filter(check,lst))                   # filter removes element from list if check condition fails
print(",".join(lst))