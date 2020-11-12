# class setup with __init__
class Employee:
	# class variables/attributes:
	raise_amount = 1.04
	num_of_employees = 0

	def __init__(self, first_name, last_name, pay):
		# instance variables/attributes:
		self.first_name = first_name
		self.last_name = last_name
		self.pay = pay
		self.email = first_name + '.' + last_name + '@company.com'

		Employee.num_of_employees += 1 

	def fullname(self):
		return(f'{self.first_name} {self.last_name}')

	def apply_raise(self):
		self.pay = self.pay * self.raise_amount

print(Employee.num_of_employees)
emp1 = Employee('Corey', 'Schafer', 5000)
emp2 = Employee('test', 'user', 8000)

# emp1.raise_amount = 1.05
# print(emp1.__dict__) #print dictionary for instance variables (if defined)
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
 
print(Employee.num_of_employees)
# help(emp1)


