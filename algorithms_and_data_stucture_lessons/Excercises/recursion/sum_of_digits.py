""" Function to find the sum of digits of a number using recursion"""


def sum_of_digits(no):
    if no == 0:
        return 0
    else:
        return int(no % 10) + sum_of_digits(int(no / 10))


number = int(input('Enter the number to find the sum of its digits: '))
print(f'The sum of digits of {number} is {sum_of_digits(number)}')
