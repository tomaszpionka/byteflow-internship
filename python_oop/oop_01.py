# Classes and instances

class Employee:


    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+"."+last+"@email.com"
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('Bartosz', 'Dyk', 60000)
emp_2 = Employee('Test', 'User', 100000)

print(emp_1.first)
print(emp_2.email)
print(Employee.fullname(emp_1))