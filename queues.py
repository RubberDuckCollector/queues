import time
from random import randint

def first_come_first_served():

    # does the first task, then the next sequeuntially until the queue is empty
    
    # the numbers represent the time taken to finish the task
    queue = [3, 2, 1, 2, 3, 2, 3, 3, 1, 2]
    #        0  1  2  3  4  5  6  7  8  9
    
    for i in range(len(queue)):
        print(f"tasks: {queue}")
        print(f"waiting for task {i+1}...")
        time.sleep(queue[0])
        print(f"task {i+1} complete!")
        queue.pop(0)

    if len(queue) == 0:
            print("finished!")

# first_come_first_served()
print()

def round_robin():

    # goes through the queue sequentially giving each task a time slice
    # until all the tasks are complete

    # the numbers in the list represent the time left to finish computing them (see line 39 comment)
    queue = [1, 3, 2, 2, 1, 4, 1, 3, 4, 1]
    #        0  1  2  3  4  5  6  7  8  9
    task = 1
    index = 0

    while len(queue) != 0:
        print(f"queue: {queue}")
        print(f"on task {task}...")
        time.sleep(1) # waiting 1 second because 1 second is the time slice
        
        queue[index] -= 1 # minus 1 from the task because it has been given the time slice

        if queue[index] == 0:
            print(f"task {task} complete!")
            queue.pop(index)
            task += 1
            
        index += 1 # go to the next element in the list

        '''there was an IndexOutOfRange error because the following >= was ==.
        this was because if index was already
        the same value as the length of the list,
        it would again be incremented by one before being checked.
        == only checked for exact equality,
        so index would never be reset to 0 when it should have been.'''
        
        if index >= len(queue):
            index = 0

        if len(queue) == 0:
            print("finished!")
    
# round_robin()
print()

def least_time_remaining():

    # picks the task executed first is the one that takes the least time left to compute
    # excludes task's original size

    # the numbers in the list represent the time left to finish computing them
    queue = [3, 3, 2, 3, 2, 2, 3, 1, 1, 1]
    #        0  1  2  3  4  5  6  7  8  9

    task = 1
    index = 0

    while len(queue) != 0:
        print(f"queue: {queue}")
        print(f"index with shortest time remaining: {queue.index(min(queue))}, time remaining: {(min(queue))}") # the time remaining is the actual value of the smallest element in the queue
        print(f"on task {task}...")
        time.sleep(min(queue))
    
        print(f"task {task} complete!")
        queue.pop(queue.index(min(queue))) # deletes the element at the index of the smalles value
        task += 1
    

least_time_remaining()
