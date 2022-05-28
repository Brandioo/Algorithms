""" Function to reverse a string using recursion """


def reverse(string):
    if string == "":
        return string
    else:
        return reverse(string[1:]) + string[0]


print(reverse('Aleks'))
