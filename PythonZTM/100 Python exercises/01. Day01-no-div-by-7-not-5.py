"""
Write a program which will find all such numbers 
which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated 
sequence on a single line.
"""

from time import time

def performance(func):
	def wrapper(*args, **kwargs):
		t1 = time()
		result = func(*args, **kwargs)
		t2 = time()
		print(f'it took {t2-t1} s')
		return result
	return wrapper

@performance	
def function1():
	for i in range(2000, 3201):
		if i%7 == 0 and i%5 != 0:
			print(i, end=',')

@performance	
def function2():
	for i in range (2002, 3201, 7):
	  if i%5 !=0:
    	print(i, end=",")

function1()
function2()
