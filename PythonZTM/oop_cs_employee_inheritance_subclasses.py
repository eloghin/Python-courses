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


#  INHERITANCE - class Developer and Manager
class Developer(Employee):
	# define a different raise_amount
	raise_amount = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang


class Manager(Employee):
	# define a different raise_amount
	raise_amount = 1.3

	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees:
			self.employees = employees
		else:
			self.employees = []


	def add_employee(self, employee):
		if employee not in self.employees:
			self.employees.append(employee)


	def remove_employee(self, employee):
		if employee in self.employees:
			self.employees.remove(employee)


	def print_employees(self):
		if self.employees:
			for employee in self.employees:
				print(f'--> {employee.fullname()}')
		else:
			print('This manager does not supervise any employees')



dev_1 = Developer('Corey', 'Schafer', 5000, "python")
dev_2 = Developer('test', 'user', 8000, "java")


# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

mng_1 = Manager('Joey', 'Jones', 9000, [])
# mng_1.remove_employee(dev_1)
# mng_1.add_employee(dev_1)
mng_1.print_employees()
print(mng_1.email)

# print(dev_1.email)
# print(dev_2.email)
