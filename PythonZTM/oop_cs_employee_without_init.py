# class setup without __init__
class Employee:
	pass

emp1 = Employee()
emp2 = Employee()

print(emp1)
print(emp2)

emp1.first_name = 'Corey'
emp1.last_name = 'Schafer'
emp1.email = 'corey@company.com'
emp1.pay = 5000

emp2.first_name = 'test'
emp2.last_name = 'user'
emp2.email = 'test@company.com'
emp2.pay = 8000

print(f'{emp1.first_name} {emp1.last_name}')
print(f'{emp2.first_name} {emp2.last_name}')

