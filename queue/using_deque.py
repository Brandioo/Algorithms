"""
    Python program to demonstrate queue implementation using "deque" from collections module

    Instead of enqueue and deque, append() and popleft() functions are used.
"""
from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.appendleft('a')
q.appendleft('b')
q.appendleft('c')

print("Initial queue")
print(q)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.pop())
print(q.pop())
print(q.pop())

print("\nQueue after removing elements")
print(q)

# Uncommenting q.popleft()
# will raise an IndexError as queue is now empty
