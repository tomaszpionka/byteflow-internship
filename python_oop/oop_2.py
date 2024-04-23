# Classes and instances

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+"."+last+"@email.com"
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Bartosz', 'Dyk', 60000)
emp_2 = Employee('Test', 'User', 100000)

emp_1.raise_amount = 1.05

print(Employee.num_of_emps)
print(emp_1.raise_amount)
print(emp_2.raise_amount)