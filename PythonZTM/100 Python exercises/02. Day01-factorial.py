"""
Write a program which can compute the factorial of a given number.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320
"""


n = int(input())

#**************
# Using for loop
#**************

# fact = 1
# for i in range(1,n+1):
#   fact = fact*i
# print(fact)


#**************
# Using lambda function
#**************

def shortFact(x): 
  return 1 if x <= 1 else x*shortFact(x-1)
  
print(shortFact(n))