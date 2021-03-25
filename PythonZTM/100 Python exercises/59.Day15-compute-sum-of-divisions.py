""" 
    Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

    Example: If the following n is given as input to the program:

    5

    Then, the output of the program should be:

    3.55
"""

# SOLUTION 1
def sum_div(n):
  result = 0
  for i in range(1,n+1):
    result += i/(i+1)
  print(round(result,2))

sum_div(int(input('n=')))


# SOLUTION 2
def question_59(n):
    print(round(sum(map(lambda x: x/(x+1), range(1, n+1))), 2))

question_59(5)