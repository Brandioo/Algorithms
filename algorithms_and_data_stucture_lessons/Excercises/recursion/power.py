""" Function to find the power of a number using recursion"""


def power_of_number(num, topwr):
    if topwr == 0:
        return 1
    else:
        return num * power_of_number(num, topwr - 1)


print('{} to the power of {} is {}'.format(5, 2, power_of_number(5, 2)))
