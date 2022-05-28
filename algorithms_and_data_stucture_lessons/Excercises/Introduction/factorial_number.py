""" Function to print the factorial of a number """


def factorial(n):
    number = n
    # Calculate the factorial of the number
    f = 1
    while number > 1:
        f *= number
        number -= 1

    print(f'The factorial of number {n} is {f}')
