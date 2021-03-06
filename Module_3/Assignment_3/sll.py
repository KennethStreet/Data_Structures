# Course: CS261 - Data Structures
# Student Name: Kenneth Street
# Assignment: Implementation of Linked Lists, ADTs using Linked Lists and Binary Search
# Description: Singly Linked List Class


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        :param -- value
        :returns -- None
        :description -- Adds a new node at the beginning of the list (right after the front sentinel)
        """

        if self.length() < 1:  # Create the front and back sentinels and set the head and tail
            front_sentinel = SLNode(None)
            back_sentinel = SLNode(None)
            self.head = front_sentinel
            self.tail = back_sentinel
            new_node = SLNode(value)
            front_sentinel.next = new_node
            new_node.next = back_sentinel
        else:  # Add to the beginning of linked list if there is more than one value in linked list
            node = self.head.next
            new_node = SLNode(value)
            new_node.next = node
            self.head.next = new_node

    def add_back(self, value: object, index=0, node=None) -> None:
        """
        :param -- value, index (Default of 0), node (Default of None)
        :returns -- None
        :description -- Adds a new node at the end of the linked list (right before the back sentinel)
        """

        if index == 0 and self.length() == 0:  # Create the front and back sentinels and set the head and tail
            front_sentinel = SLNode(None)
            back_sentinel = SLNode(None)
            self.head = front_sentinel
            self.tail = back_sentinel
            self.head.next = self.tail

        if index <= self.length():  # Make recursive call to get to the end of the linked list
            if node is not None:
                node = node.next
            else:
                node = self.head
            index += 1
            self.add_back(value, index, node)
        else:  # Reached the end so add new node
            new_node = SLNode(value)
            prev_node = node
            next_node = node.next
            prev_node.next = new_node
            new_node.next = next_node

    def insert_at_index(self, index: int, value: object, pointer=0, previous=None, current=None) -> None:
        """
        :param -- index, value, pointer (Default of 0), previous (Default of None), current (Default of None)
        :returns -- None
        :description -- Adds a new value at the specified index position. Index 0 refers to the beginning of the list
        """
        if self.length() < index or index < 0:
            raise SLLException

        if index == 0 and self.length() == 0:  # Create the front and back sentinels and set the head and tail
            front_sentinel = SLNode(None)
            back_sentinel = SLNode(None)
            self.head = front_sentinel
            self.tail = back_sentinel
            self.head.next = self.tail

        if current is None:
            current = self.head

        if index == 0 and pointer == 0 and self.length() == 0:
            new_node = SLNode(value)
            front_sentinel.next = new_node
            new_node.next = back_sentinel
            return

        if pointer - 1 == index:
            next_node = current
            current = SLNode(value)
            previous.next = current
            current.next = next_node
            return

        if current.next is not None:
            pointer += 1
            previous = current
            current = current.next
            self.insert_at_index(index, value, pointer, previous, current)

    def remove_front(self) -> None:
        """
        :param -- None
        :returns -- None
        :description -- Removes the first node from the list
        """
        if self.length() <= 0:
            raise SLLException
        elif self.length() == 1:
            self.head.next = self.tail
        else:
            previous = self.head
            current = self.head.next
            previous.next = current.next

    def remove_back(self, pointer=0, previous=None, current=None) -> None:
        """
        :param -- pointer (Default of 0), previous (Default of None), current (Default of None)
        :returns -- None
        :description -- Removes the last node from the list
        """
        if self.length() <= 0:
            raise SLLException

        if current is None:
            current = self.head

        if pointer == self.length():
            previous.next = current.next
        else:
            pointer += 1
            previous = current
            current = current.next
            self.remove_back(pointer, previous, current)

    def remove_at_index(self, index: int, pointer=0, previous=None, current=None) -> None:
        """
        :param -- index, pointer (Default of 0), previous (Default of None), current (Default of None)
        :returns -- None
        :description -- Removes a node from the given index
        """
        if self.length() <= 0 or self.length() <= index or index < 0:
            raise SLLException

        if index == 0:
            self.remove_front()
            return

        if current is None:
            current = self.head

        if pointer - 1 == index:
            previous.next = current.next
        else:
            pointer += 1
            previous = current
            current = current.next
            self.remove_at_index(index, pointer, previous, current)

    def get_front(self) -> object:
        """
        :param -- None
        :returns -- Object
        :description -- Returns the value of the first node in the list without removing it
        """
        if self.length() <= 0:
            raise SLLException

        return self.head.next.value

    def get_back(self, pointer=0, current=None) -> object:
        """
        :param -- pointer (Default of 0), current (Default of None)
        :returns -- Object
        :description -- Returns the value of the last node in the list without removing it
        """
        if self.length() <= 0:
            raise SLLException

        if current is None:
            current = self.head

        if pointer == self.length():
            return current.value
        else:
            pointer += 1
            current = current.next
            return self.get_back(pointer, current)

    def remove(self, value: object, pointer=0, previous=None, current=None) -> bool:
        """
        :param -- value, pointer (Default of 0), previous (Default of None), current (Default of None)
        :returns -- bool
        :description -- Traverses the linked list and removes the first instance of the value passed
        """
        if self.length() <= 0 or self.length() <= pointer:
            return False

        if current is None:
            previous = self.head
            current = previous.next

        if current.value == value:
            previous.next = current.next
            return True
        else:
            pointer += 1
            previous = current
            current = current.next
            return self.remove(value, pointer, previous, current)

    def count(self, value: object, count=0, current=None) -> int:
        """
        :param -- value, count (Default of 0), current (Default of None)
        :returns -- int
        :description -- Counts the number of elements in the linked list that match the provided value
        """
        if self.length() <= 0:
            raise SLLException

        if current is None:
            current = self.head

        if value == current.value:
            count += 1

        if current.next is not None:
            current = current.next
            return self.count(value, count, current)
        else:
            return count

    def slice(self, start_index: int, size: int, subset=None, pointer=0, current=None) -> object:
        """
        :param -- start_index, size, subset (Default of None), pointer (Default of 0), current (Default of None)
        :returns -- Object
        :description -- Creates and returns a subset of the linked list starting at the start_index to size
        """

        if start_index < 0 or self.length() < size \
                or size < 0 \
                or start_index == self.length() \
                or start_index + size > self.length():
            raise SLLException

        if current is None:
            current = self.head
            subset = LinkedList()

        if pointer <= self.length():
            if start_index <= pointer - 1 <= start_index + size - 1:
                subset.add_back(current.value)
            current = current.next
            pointer += 1
            self.slice(start_index, size, subset, pointer, current)

        return subset


if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    list = LinkedList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)


    print('\n# add_back example 1')
    list = LinkedList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)


    print('\n# insert_at_index example 1')
    list = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)
        except Exception as e:
            print(type(e))


    print('\n# remove_front example 1')
    list = LinkedList([1, 2])
    print(list)
    for i in range(3):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))


    print('\n# remove_back example 1')
    list = LinkedList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)


    print('\n# remove_at_index example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)


    print('\n# get_front example 1')
    list = LinkedList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))


    print('\n# get_back example 1')
    list = LinkedList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())


    print('\n# remove example 1')
    list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)


    print('\n# count example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))


    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")


    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")

