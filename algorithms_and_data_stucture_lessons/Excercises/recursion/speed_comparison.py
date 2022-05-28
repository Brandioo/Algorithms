"""
    Speed comparison of factiorial implemetations

    Syntax: timeit(<command>, setup=<setup_string>, number=<iterations>)

    To evaluate execution time, you can use a function called timeit() from a module that is also called timeit.
    timeit() first executes the commands contained in the specified <setup_string>.
    Then it executes <command> the given number of <iterations> and reports the cumulative execution time in seconds.
"""
from timeit import timeit

setup_recursive_string = """
print('Recursive')
def recursive_factorial(n):
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)
"""

setup_iterative_string = """
print('Iterative')
def iterative_factorial(n):
    number = n
    # Calculate the factorial of the number
    f = 1
    f *= number
    while number > 1:
        number -= 1
        f *= number
"""

setup_math_string = "from math import factorial"

print(timeit("iterative_factorial(5)", setup=setup_iterative_string, number=10000000))
print(timeit("recursive_factorial(5)", setup=setup_recursive_string, number=10000000))
print('Math')
print(timeit("factorial(5)", setup=setup_math_string, number=10000000))
