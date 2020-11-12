class Employee:

	# class variables/attributes:
	raise_amount = 1.04

	def __init__(self, first_name, last_name, pay):
		# instance variables/attributes:
		self.first_name = first_name
		self.last_name = last_name
		self.pay = pay
		self.email = first_name + '.' + last_name + '@company.com'


	# REGULAR METHODS
	def fullname(self):
		return(f'{self.first_name} {self.last_name}')


	def apply_raise(self):
		self.pay = self.pay * self.raise_amount


	def __repr__(self):
	 	# format ready to copy_paste into the code
	 	return (f"Employee('{self.first_name}', '{self.last_name}', '{self.pay}')")

	def __str__(self):
		# format end user friendly
		return (f'{self.fullname()}, {self.email}')


emp_1 = Employee('Corey', 'Schafer', 5000)

emp_2 = Employee('test', 'user', 8000)

print(emp_1)
print(repr(emp_1))

print(emp_1.__str__())
print(emp_1.__repr__())

