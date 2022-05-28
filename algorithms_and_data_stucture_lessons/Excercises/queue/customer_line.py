""" Python program to build a CustomerLine class and use it as a FIFO Queue """
import abc
import random
import time
from abc import abstractmethod
from collections import deque
from typing import Union

from cinema_customers import Child, Man, Woman


class CustomerLine(abc.ABC):

    @abstractmethod
    def __init__(self):
        self.line = None

    def __str__(self):
        return f'Line of Customers => {[customer for customer in self.line]}'

    @property
    def customers_waiting(self):
        return len(self.line)

    @property
    def is_empty(self):
        if self.customers_waiting > 0:
            return False
        return True

    @abstractmethod
    def append(self, customer: Union['Man', 'Woman', 'Child']):
        pass

    def pop(self):
        if self.is_empty:
            return
        self.line.pop()


class NormalCustomerLine(CustomerLine):

    def __init__(self):
        self.line = list()

    def append(self, customer):
        self.line.insert(0, customer)


class FasterCustomerLine(CustomerLine):

    def __init__(self):
        self.line = deque()

    def append(self, customer):
        self.line.appendleft(customer)


if __name__ == '__main__':

    customers = [
        Man('Alex', 'Duka'),
        Woman('Angelina', 'Jolie'),
        Child('Alex', 'Jr')
    ]
    start = time.time()

    normal_line = NormalCustomerLine()
    for i in range(10000):
        client = random.choice(customers)
        normal_line.append(client)
    for i in range(10000):
        normal_line.pop()

    # print(min(timeit.repeat(partial(process_line), number=1000000)))   convert it to try with timeit
    print(f'Processing the customer in Normal Line took: {time.time() - start}')

    start = time.time()

    faster_line = FasterCustomerLine()
    for i in range(10000):
        client = random.choice(customers)
        faster_line.append(client)
    for i in range(10000):
        faster_line.pop()

    print(f'Processing the customer in Fast Line took: {time.time() - start}')
