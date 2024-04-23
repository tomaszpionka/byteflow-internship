# Classes and instances
import datetime


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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Bartosz', 'Dyk', 60000)
emp_2 = Employee('Test', 'User', 100000)

emp_str_1 = 'John-Doe-70000'

new_emp = Employee.from_string(emp_str_1)

my_date = datetime.date(2016, 7, 20)
print(Employee.is_workday(my_date))


Employee.raise_amount = 1.07

print(Employee.num_of_emps)
print(emp_1.raise_amount)
print(emp_2.raise_amount)