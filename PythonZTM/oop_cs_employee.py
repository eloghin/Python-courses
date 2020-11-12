# class setup with __init__
class Employee:

	def __init__(self, first_name, last_name, pay):
		self.first_name = first_name
		self.last_name = last_name
		self.pay = pay
		self.email = first_name + '.' + last_name + '@company.com'

	def fullname(self):
		return(f'{self.first_name} {self.last_name}')

emp1 = Employee('Corey', 'Schafer', 5000)
emp2 = Employee('test', 'user', 8000)

print(emp1)
print(emp2)
 
# 2 series of prints with the same result
# 1st: the fullname method is called for the instance of the class
# the self is passed in automatically
print(emp1.fullname())
print(emp2.fullname())

# 2nd: the fullname method is called on the class and the instance 
# is passed in explicitly
print(Employee.fullname(emp1))
print(Employee.fullname(emp2))



