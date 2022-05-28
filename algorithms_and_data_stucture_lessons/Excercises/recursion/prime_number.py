""" Function to check if a number is a Prime number using recursion """


def is_prime(number, div=2):
    if number <= 2:
        return True if number == 2 else False
    if number % div == 0:
        return False
    if div * div > number:
        return True
    return is_prime(number=number, div=div + 1)


nr = int(input("Pease input a number: "))
print(f'{nr} -> {is_prime(nr)}')
