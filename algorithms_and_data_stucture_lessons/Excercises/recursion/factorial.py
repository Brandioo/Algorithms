""" A recursive Python function to calculate factorial """


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


number = int(input('Input a number: '))
print(factorial(number))


# ------------------------------------------------------------------------


# To used to better understand the calls in a recursive function
def factorial_expained(n):
    print(f"factorial() called with n = {n}")
    return_value = 1 if n <= 1 else n * factorial_expained(n - 1)
    print(f"-> factorial({n}) returns {return_value}")
    return return_value


factorial_expained(number)
