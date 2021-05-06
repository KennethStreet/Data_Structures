# Course: CS261 - Data Structures
# Student Name: Kenneth Street
# Assignment: Project 2 - Your Very Own Dynamic Array
# Description: Max Stack data structure and it's methods

from max_stack_da import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new Queue based on two stacks
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.s1 = MaxStack()  # use as main storage
        self.s2 = MaxStack()  # use as temp storage

    def __str__(self) -> str:
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.s1.size()) + " elements. "
        out += str(self.s1)
        return out

    def is_empty(self) -> bool:
        """
        Return True if queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.size()

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        :param -- value
        :returns -- None
        :description -- Adds a new value to the end of the Queue
        """
        self.s1.push(value)

    def dequeue(self) -> object:
        """
        :param -- None
        :returns -- Max Stack Object
        :description -- Removes and returns the value at the beginning of the Queue
        """
        # Begin error handling
        if self.s1.is_empty():
            raise QueueException

        # Pop every value in the stack to get the first one pushed
        for value in range(self.s1.size()):
            popped_value = self.s1.top()
            self.s1.pop()
            self.s2.push(popped_value)

        # Last value in the stack is first in queue
        temp_queue = self.s2.pop()

        # Re-push every value into the stack
        for value in range(self.s2.size()):
            popped_value = self.s2.top()
            self.s2.pop()
            self.s1.push(popped_value)

        # Clear out temp storage
        self.s2 = MaxStack()

        return temp_queue


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# enqueue example 1')
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)


    print('\n# dequeue example 1')
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue(), q)
        except Exception as e:
            print("No elements in queue", type(e))
