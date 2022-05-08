""" Python program to reverse a string using stack """


# Function to create an empty stack.
def create_stack():
    stack = []
    return stack


# Function to determine the size of the stack
def size(stack):
    return len(stack)


# Stack is empty if the size is 0
def is_empty(stack):
    if size(stack) == 0:
        return True


# Function to add an item to stack .
def push(stack, item):
    stack.append(item)


# Function to remove an item from stack.
def pop(stack):
    if is_empty(stack):
        return
    return stack.pop()


# A stack based function to reverse a string
def reverse(string):
    n = len(string)

    # Create an empty stack
    stack = create_stack()

    # Push all characters of string to stack
    for i in range(0, n, 1):
        push(stack, string[i])

    # Making the string empty since all
    # characters are saved in stack
    string = ""

    # Pop all characters of string and
    # put them back to string
    for i in range(0, n, 1):
        string += pop(stack)

    return string


# Driver program to test above functions
new_string = "Python Course"
reverse_string = reverse(new_string)
print("Reversed string is " + reverse_string)