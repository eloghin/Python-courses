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

	# CLASS METHODS
	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	# REGULAR METHODS
	def fullname(self):
		return(f'{self.first_name} {self.last_name}')


	def apply_raise(self):
		self.pay = self.pay * self.raise_amount


	# STATIC METHODS
	@staticmethod
	def is_working_day(day):
		if day.weekday() in [5,6]:
			return False
		return True

# emp1 = Employee('Corey', 'Schafer', 5000)
# emp2 = Employee('test', 'user', 8000)

# # CLASSMETHOD usage
# emp1.set_raise_amt(1.06)

# Employee.set_raise_amt(1.05)
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

# # use from_string() constructor
# emp_str1 = "John-Doe-40000"
# new_emp_1 = Employee.from_string(emp_str1)

# print(new_emp_1.fullname())

# # STATIC METHOD Usage
import datetime
my_date = datetime.date(2020, 7, 10)
print(Employee.is_working_day(my_date))
