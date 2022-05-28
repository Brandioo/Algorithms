""" Script to find the sum of 3 numbers """

# Variables to take the input of
# the 3 numbers
num1 = num2 = num3 = 0

# Variable to store the resultant sum
sum = 0

# Take the 3 numbers as input
try:
    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    num3 = int(input("Enter the 3rd number: "))
except ValueError:
    raise Exception("Only number are expected as input !")

# Calculate the sum using + operator
# and store it in variable sum
sum = num1 + num2 + num3

# Print the sum
print("\nSum of the 3 numbers is:", sum)
