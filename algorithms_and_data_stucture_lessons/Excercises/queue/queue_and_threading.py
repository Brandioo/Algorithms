"""
    Program that shows how Threading and Queue cam work together
"""
from queue import Queue
import threading
import time

queue = Queue()
for j in range(10):
    queue.put(j)


# Function that uses an infinite while loop, so it can run forever
# This function gets a task from the queue
# time.sleep(2) -> is used just to simulate a time-consuming task
# By using q.task_done(), we let the system know that this task is finished
def complete_task(q, thread_no):
    while True:
        task = q.get()
        time.sleep(2)
        q.task_done()
        print(f'Thread #{thread_no} is doing task #{task} in the queue.')


# Creating a Queue instance (FIFO)

# Creating 4 threads that will run the complete_task() function
# Sending the queue instance and the number of the queue as an argument
# Starting all the 4 Threads
for i in range(4):
    worker = threading.Thread(target=complete_task, args=(queue, i,), daemon=True)
    worker.start()

# Putting 10 new tasks to the current queue
# So the Threads will contiunue working on solving these tasks

# This command will terminate the program
# When all the tasks on the queue are finished
queue.join()
