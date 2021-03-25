
"""
Write a program to generate and print another tuple whose values are 
even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
"""

def create_tuple(t):
  t2 = tuple((i for i in t if i%2==1))
  print(t2)

create_tuple((1,2,3,4,5,6,7,8,9))



******* SOL 2 *******

tpl = (1,2,3,4,5,6,7,8,9,10)
tpl1 = tuple(filter(lambda x : x%2==0,tpl))  # Lambda function returns True if found even element.
                                             # Filter removes data for which function returns False
print(tpl1)
