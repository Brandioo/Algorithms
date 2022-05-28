"""
    The first example is a function called countdown(),
     which takes a positive number as an argument
     and prints the numbers from the specified argument down to zero
"""


def countdown(number):
    print(number)
    if number == 0:  # The Base Case when number is 0
        return  # Terminate recursion
    countdown(number=number - 1)  # Recursive call with parameter closer to the base care


# Call the function with the inputed number
nr = int(input("Pease input a number: "))
countdown(number=nr)
