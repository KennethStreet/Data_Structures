# Course: CS261 - Data Structures
# Student Name: Kenneth Street
# Assignment: Project 2 - Your Very Own Dynamic Array
# Description: Max Stack data structure and it's methods

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class MaxStack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da_val = DynamicArray()
        self.da_max = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "MAX STACK: " + str(self.da_val.length()) + " elements. ["
        out += ', '.join([str(self.da_val[i]) for i in range(self.da_val.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        :param -- value
        :returns -- None
        :description -- Adds a new value to the Stack
        """
        self.da_val.append(value)

        if not self.da_max.is_empty():
            if self.da_max.__getitem__(self.da_max.length() - 1) <= value:
                self.da_max.append(value)
        else:
            self.da_max.append(value)

    def pop(self) -> object:
        """
        :param -- None
        :returns -- Max Stack Object
        :description -- Removes the element at the top of the stack
        """
        # Exception handling
        if self.is_empty():
            raise StackException

        top_stack = self.size() - 1
        popped_element = self.da_val.__getitem__(top_stack)

        self.da_val.__setitem__(top_stack, None)
        self.da_val.size -= 1

        max_stack = self.da_max.length() - 1

        if self.da_max.__getitem__(max_stack) == popped_element:
            self.da_max.__setitem__(max_stack, None)
            self.da_max.size -= 1

        return popped_element

    def top(self) -> object:
        """
        :param -- None
        :returns -- Object
        :description -- Returns the element at the top of the stack without removing it. Similar to peak()
        """
        if self.is_empty():
            raise StackException

        top_stack = self.size() - 1
        popped_element = self.da_val.__getitem__(top_stack)
        return popped_element

    def get_max(self) -> object:
        """
        :param -- None
        :returns -- Object
        :description -- Returns the max element in the Stack
        """

        if self.is_empty():
            raise StackException

        top_stack = self.da_max.size - 1
        top_element = self.da_max.__getitem__(top_stack)

        return top_element


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = MaxStack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)


    print("\n# pop example 1")
    s = MaxStack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))


    print("\n# top example 1")
    s = MaxStack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)


    print('\n# get_max example 1')
    s = MaxStack()
    for value in [1, -20, 15, 21, 21, 40, 50]:
        print(s, ' ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
        s.push(value)
    while not s.is_empty():
        print(s.size(), end='')
        print(' Pop value:', s.pop(), ' get_max after: ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
