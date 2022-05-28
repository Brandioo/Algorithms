"""
    Python program to demonstrate queue implementation using list
"""

queue = list()

# Adding elements to the queue
queue.insert(0, 'a')
queue.insert(0, 'b')
queue.insert(0, 'c')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop())
print(queue.pop())
print(queue.pop())

print("\nQueue after removing elements")
print(queue)

# Uncommenting print(queue.pop(0))
# will raise and IndexError as the queue is now empty
