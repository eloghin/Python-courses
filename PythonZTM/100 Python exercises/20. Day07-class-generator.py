"""
    Define a class with a generator which can iterate the numbers, which are divisible by 7, 
    between a given range 0 and n.

    Suppose the following input is supplied to the program:

		17

    Then, the output should be:

		0
		7
		14

"""

# ***********
# ***SOL 1***
# ***********

class NumGen():
	def __init__(self, n):
		self.n = n

	def print_num(self):
		num = 0
		while num <= self.n:
			print(num)
			num += 7

num_gen = NumGen(20)
num_gen.print_num()

# ***********
# ***SOL 2***
# ***********

class NumGen():
	def __init__(self, n):
		self.n = n

	def div_by_seven(self):
		for i in range (self.n//7 +1):
			yield i*7

num_gen = NumGen(10)
for num in num_gen.div_by_seven():
	print(num)