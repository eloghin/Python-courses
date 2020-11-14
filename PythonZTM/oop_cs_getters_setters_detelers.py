class Employee:

	# class variables/attributes:
	raise_amount = 1.04

	def __init__(self, first_name, last_name):
		# instance variables/attributes:
		self.first_name = first_name
		self.last_name = last_name
		self.email = first_name + '.' + last_name + '@company.com'


	# REGULAR METHODS
	def fullname(self):
		return(f'{self.first_name} {self.last_name}')



emp_1 = Employee('Corey', 'Schafer')

emp_1.first_name = 'Jim'

print(emp_1.first_name)
print(emp_1.email)
print(emp_1.fullname())

