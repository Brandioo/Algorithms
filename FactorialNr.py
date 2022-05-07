def factorial(n):
    number = n

    f = 1
    f *= number

    while number > 1:
        number -= 1
        f *= number

    print(f'The Factorial of number {n} is {f}')
