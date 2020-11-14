class Employee:

	def __init__(self, first_name, last_name):
		# instance variables/attributes:
		self.first_name = first_name
		self.last_name = last_name


	# property decorators
	@property
	def email(self):
		return(f'{self.first_name}.{self.last_name}@email.com')

	@property
	def fullname(self):
		return (f'{self.first_name} {self.last_name}')
	
	@fullname.setter
	def fullname(self, name):
		first_name, last_name = name.split(' ')

	@fullname.deleter
	def fullname(self):
		self.first_name = None
		self.last_name = None


emp_1 = Employee('Corey', 'Schafer')

emp_1.first_name = 'Jim'

print(emp_1.first_name)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.fullname)

