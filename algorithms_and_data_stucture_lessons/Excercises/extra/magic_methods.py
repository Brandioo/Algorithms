from typing import Any


class Employee:
    raise_amt = 0.80

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)

    def __call__(self):
        print('Employee has earned a raise !')
        self.apply_raise()

    def __eq__(self, other):
        if self.pay == other.pay:
            return True
        return False


if __name__ == "__main__":
    emp_1 = Employee('Alex', 'Duka', 50000)
    emp_2 = Employee('Test', 'Employee', 60000)

    print(emp_1 == emp_2)

    print(emp_1 + emp_2)

    print(len(emp_1))
