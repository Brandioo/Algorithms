""" This is the exaple that shows there is a limit in recursion """
from sys import getrecursionlimit, setrecursionlimit

# Function used to show the recursion limit
print(f"Default Recursion Limit: {getrecursionlimit()}")
# Function used to change the recursion limit
setrecursionlimit(500)
# Print to se the changed limt
print(f"Changed Recursion Limit: {getrecursionlimit()}")


# There is no problem when defining the function
def function():
    x = 10
    function()


# An RecursionError is thrown when you try to execute the function
function()
