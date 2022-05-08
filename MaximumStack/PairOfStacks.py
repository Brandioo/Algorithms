"""
    Python program to find the max in a stack without using another stack

    Approach: Instead of pushing a single element to the stack, push a pair instead.
              The pair consists of the (value, local_max) where local_max is the maximum value up to that element.

    -  When we insert a new element, if the new element is greater than the local maximum below it,
       we set the local maximum of a new element equal to the element itself.
    - Else, we set the local maximum of the new element equal to the local maximum of the element below it.
    - The local maximum of the top of the stack will be the overall maximum.
    - Now if we want to know the maximum at any given point,
      we ask the top of the stack for local maximum associated with it.

"""


class Block:
    # A block has two elements as components  (i.e. value and local_max)
    def __init__(self, value, local_max):
        self.value = value
        self.local_max = local_max

    def __repr__(self):
        return f"{self.value, self.local_max}"


class Stack:

    def __init__(self, size):
        # Setting size of stack and initial value of top
        self.stack: list = [None] * size
        self.size: int = size
        self.top: int = -1

    def push(self, value):
        """ Function to push an element to the stack """

        # Don't allow pushing elements if stack is full
        if self.top == self.size - 1:
            print("Stack is full")
        else:
            self.top += 1

            # If the inserted element is the first element
            # then it is the maximum element, since no other
            # elements is in the stack, so the local_max
            # of the first element is the element itself
            if self.top == 0:
                self.stack[self.top] = Block(value, value)

            else:
                # If the newly pushed element is less
                # than the local_max of element below it,
                # Then the over all maximum doesn't change
                # and the local_max of the newly inserted
                # element is same as element below it
                if self.stack[self.top - 1].local_max > value:
                    current_local_max = self.stack[self.top - 1].local_max
                    self.stack[self.top] = Block(value, current_local_max)

                # Newly inserted element is greater than
                # the local_max below it, hence the local_max
                # of new element is the element itself
                else:
                    self.stack[self.top] = Block(value, value)

            print(value, "inserted in the stack")

    def pop(self):
        """ Function to remove an element from the top of the stack """

        # If stack is empty
        if self.top == -1:
            print("Stack is empty")

        # Remove the element if the stack is not empty
        else:
            self.top -= 1
            print("Element popped")

    def max(self):
        """ Function to find the maximum element from the stack """

        # If stack is empty
        if self.top == -1:
            print("Stack is empty")

        else:
            # The overall maximum is the local maximum of the top element
            print(
                "Maximum value in the stack:", self.stack[self.top].local_max
            )


if __name__ == '__main__':
    # Create stack of size 5
    stack = Stack(5)
    print(f'Stack: {stack.stack}, Top: {stack.top}')

    stack.push(2)
    print(f'Stack: {stack.stack}, Top: {stack.top}')

    stack.push(6)
    print(f'Stack: {stack.stack}, Top: {stack.top}')

    stack.push(3)
    print(f'Stack: {stack.stack}, Top: {stack.top}')

    stack.max()

    stack.pop()
    print(f'Stack: {stack.stack}, Top: {stack.top}')

    stack.max()

    stack.push(10)
    print(f'Stack: {stack.stack}, Top: {stack.top}')