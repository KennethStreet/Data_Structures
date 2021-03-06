# Course: CS261 - Data Structures
# Student Name: Kenneth Street
# Assignment: Implementation of Linked Lists, ADTs using Linked Lists and Binary Search
# Description: Circular Doubly Linked List Class with Deque and Bag ADT interfaces


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next == self.sentinel

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        :param -- value
        :returns -- None
        :description -- Adds a new node at the beginning of the list (right after the sentinel)
        """
        new_node = DLNode(value)
        if self.sentinel.next == self.sentinel:  # If linked list is empty then set self.sentinel link to new_node
            new_node.next = self.sentinel
            new_node.prev = self.sentinel
            self.sentinel.prev = new_node
            self.sentinel.next = new_node
        else:
            new_node.next = self.sentinel.next
            new_node.prev = self.sentinel
            self.sentinel.next.prev = new_node
            self.sentinel.next = new_node

    def add_back(self, value: object) -> None:
        """
        :param -- value
        :returns -- None
        :description -- Adds a new node at the end of the list
        """
        new_node = DLNode(value)
        new_node.next = self.sentinel
        new_node.prev = self.sentinel.prev
        self.sentinel.prev.next = new_node
        self.sentinel.prev = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        :param: index, value
        :returns: None
        :description: Inserts a value at the specified index
        """
        if index < 0 or index > self.length():
            raise CDLLException

        if index == 0:
            self.add_front(value)
            return
        elif index == self.length() + 1:
            self.add_back(value)
            return

        pointer = 0
        new_node = DLNode(value)
        current = self.sentinel.next

        while pointer <= index:
            if pointer == index:
                current.prev.next = new_node
                new_node.prev = current.prev
                current.prev = new_node
                new_node.next = current
                return
            pointer += 1
            current = current.next

    def remove_front(self) -> None:
        """
        :param: None
        :returns: None
        :description: Removes the front node from the circular doubly linked list
        """
        if self.sentinel.next == self.sentinel:
            raise CDLLException
        self.sentinel.next = self.sentinel.next.next
        self.sentinel.next.prev = self.sentinel

    def remove_back(self) -> None:
        """
        :param: None
        :returns: None
        :description: Removes the last node from the circular doubly linked list
        """
        if self.sentinel.next == self.sentinel:
            raise CDLLException
        self.sentinel.prev.prev.next = self.sentinel
        self.sentinel.prev = self.sentinel.prev.prev

    def remove_at_index(self, index: int) -> None:
        """
        :param: index
        :returns: None
        :description: Takes an index value and removes the node at the specified index
        """
        if index < 0 or index >= self.length():
            raise CDLLException

        if index == 0:
            self.remove_front()
            return
        elif index == self.length() - 1:
            self.remove_back()
            return

        pointer = 0
        current = self.sentinel.next

        while current != self.sentinel:
            if pointer == index:
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            pointer += 1
            current = current.next

    def get_front(self) -> object:
        """
        :param: None
        :returns: DLNode Object
        :description: Returns the first value in the list without removing it.
        """
        if self.is_empty():
            raise CDLLException
        return self.sentinel.next.value

    def get_back(self) -> object:
        """
        :param: None
        :returns: DLNode Object
        :description: Returns the last value in the list without removing it.
        """
        if self.is_empty():
            raise CDLLException
        return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        :param: value
        :returns: bool
        :description: Traverses the list from beginning to end and removes the first instance that matches value
        """
        current = self.sentinel.next
        while current != self.sentinel:
            if current.value == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                return True
            current = current.next
        return False

    def count(self, value: object) -> int:
        """
        :param: value
        :returns: int
        :description: Counts the number of times value is in the linked list
        """
        if self.is_empty():
            return 0

        count = 0
        current = self.sentinel.next

        while current != self.sentinel:
            if current.value == value:
                count += 1
            current = current.next

        return count

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        :param: index1, index2
        :returns: None
        :description: Swaps two nodes in the linked list by providing two indices
        """
        if index1 >= self.length() or index2 >= self.length() or index1 < 0 or index2 < 0:
            raise CDLLException

        if index1 == index2:  # No work needed if indices match
            return None

        current = self.sentinel.next
        pointer = 0
        first_node = None
        second_node = None

        while current != self.sentinel:
            if index1 == pointer:
                first_node = current  # Found node at index 1
            if index2 == pointer:
                second_node = current  # Found node at index 2
            pointer += 1
            current = current.next

        if first_node is not None and second_node is not None:  # Begin Swapping Nodes
            temp = first_node.next

            first_node.next = second_node.next
            first_node.next.prev = first_node

            second_node.next = temp
            second_node.next.prev = second_node

            temp = first_node.prev

            second_node.prev.next = first_node
            first_node.prev = second_node.prev

            second_node.prev = temp
            second_node.prev.next = second_node

    def reverse(self) -> None:
        """
        :param: None
        :returns: None
        :description: Reverses the order of the linked list
        """
        if self.is_empty():
            return

        first_node = self.sentinel.next
        second_node = self.sentinel.prev
        pointer = 0

        while pointer < self.length() / 2:
            temp = first_node.next  # Begin switching nodes

            first_node.next = second_node.next
            first_node.next.prev = first_node

            second_node.next = temp
            second_node.next.prev = second_node

            temp = first_node.prev

            second_node.prev.next = first_node
            first_node.prev = second_node.prev

            second_node.prev = temp
            second_node.prev.next = second_node

            temp = first_node.prev  # Increment/Decrement nodes for next switch
            first_node = second_node.next
            second_node = temp
            pointer += 1

    def sort(self) -> None:
        """
        :param: None
        :returns: None
        :description: Sorts the doubly linked list using bubble sort
        """
        if self.is_empty():
            return None

        change_made = False
        first_node = self.sentinel.next
        second_node = first_node.next

        while first_node != self.sentinel and second_node != self.sentinel:
            if first_node.value > second_node.value:
                while first_node.value > second_node.value:
                    change_made = True
                    temp = first_node.next  # Begin switching nodes

                    first_node.next = second_node.next
                    first_node.next.prev = first_node

                    second_node.next = temp
                    second_node.next.prev = second_node

                    temp = first_node.prev

                    second_node.prev.next = first_node
                    first_node.prev = second_node.prev

                    second_node.prev = temp
                    second_node.prev.next = second_node
                    second_node = first_node.next
                    if second_node == self.sentinel:
                        first_node = self.sentinel.next
                        second_node = first_node.next
                        break
            else:
                first_node = second_node
                second_node = first_node.next
                if second_node == self.sentinel and not change_made:
                    break
                elif second_node == self.sentinel:
                    first_node = self.sentinel.next
                    second_node = first_node.next
                    change_made = False

    def rotate(self, steps: int) -> None:
        """
        TODO: Write this implementation
        """
        pass

    def remove_duplicates(self) -> None:
        """
        :param: None
        :returns: None
        :description: Removes duplicates from the linked list
        """
        if self.is_empty():
            return None

        current = self.sentinel.next

        while current != self.sentinel:  # Iterate through the linked list
            if current.value == current.next.value:  # If duplicate has been found then remove current.next
                current.next = current.next.next
                current.next.prev = current
                if current.value != current.next.value:  # Remove current if duplicate has been found
                    current.prev.next = current.next
                    current.next.prev = current.prev
            else:
                current = current.next

    def odd_even(self) -> None:
        """
        TODO: Write this implementation
        """
        pass

    def add_integer(self, num: int) -> None:
        """
        TODO: Write this implementation
        """
        pass


if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    lst = CircularList()
    print(lst)
    lst.add_front('A')
    lst.add_front('B')
    lst.add_front('C')
    print(lst)

    print('\n# add_back example 1')
    lst = CircularList()
    print(lst)
    lst.add_back('C')
    lst.add_back('B')
    lst.add_back('A')
    print(lst)

    print('\n# insert_at_index example 1')
    lst = CircularList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# remove_front example 1')
    lst = CircularList([1, 2])
    print(lst)
    for i in range(3):
        try:
            lst.remove_front()
            print('Successful removal', lst)
        except Exception as e:
            print(type(e))

    print('\n# remove_back example 1')
    lst = CircularList()
    try:
        lst.remove_back()
    except Exception as e:
        print(type(e))
    lst.add_front('Z')
    lst.remove_back()
    print(lst)
    lst.add_front('Y')
    lst.add_back('Z')
    lst.add_front('X')
    print(lst)
    lst.remove_back()
    print(lst)

    print('\n# remove_at_index example 1')
    lst = CircularList([1, 2, 3, 4, 5, 6])
    print(lst)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))
    print(lst)

    print('\n# get_front example 1')
    lst = CircularList(['A', 'B'])
    print(lst.get_front())
    print(lst.get_front())
    lst.remove_front()
    print(lst.get_front())
    lst.remove_back()
    try:
        print(lst.get_front())
    except Exception as e:
        print(type(e))

    print('\n# get_back example 1')
    lst = CircularList([1, 2, 3])
    lst.add_back(4)
    print(lst.get_back())
    lst.remove_back()
    print(lst)
    print(lst.get_back())

    print('\n# remove example 1')
    lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [7, 3, 3, 3, 3]:
        print(lst.remove(value), lst.length(), lst)

    print('\n# count example 1')
    lst = CircularList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print('\n# swap_pairs example 1')
    lst = CircularList([0, 1, 2, 3, 4, 5, 6])
    test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5),
                  (4, 2), (3, 3), (1, 2), (2, 1))

    for i, j in test_cases:
        print('Swap nodes ', i, j, ' ', end='')
        try:
            lst.swap_pairs(i, j)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# reverse example 1')
    test_cases = (
        [1, 2, 3, 3, 4, 5],
        [1, 2, 3, 4, 5],
        ['A', 'B', 'C', 'D']
    )
    for case in test_cases:
        lst = CircularList(case)
        lst.reverse()
        print(lst)

    # print('\n# reverse example 2')
    # lst = CircularList()
    # print(lst)
    # lst.reverse()
    # print(lst)
    # lst.add_back(2)
    # lst.add_back(3)
    # lst.add_front(1)
    # lst.reverse()
    # print(lst)
    #
    # print('\n# reverse example 3')
    #
    #
    # class Student:
    #     def __init__(self, name, age):
    #         self.name, self.age = name, age
    #
    #     def __eq__(self, other):
    #         return self.age == other.age
    #
    #     def __str__(self):
    #         return str(self.name) + ' ' + str(self.age)
    #
    #
    # s1, s2 = Student('John', 20), Student('Andy', 20)
    # lst = CircularList([s1, s2])
    # print(lst)
    # lst.reverse()
    # print(lst)
    # print(s1 == s2)
    #
    # print('\n# reverse example 4')
    # lst = CircularList([1, 'A'])
    # lst.reverse()
    # print(lst)

    print('\n# sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)]
    )
    for case in test_cases:
        lst = CircularList(case)
        print(lst)
        lst.sort()
        print(lst)

    # print('\n# rotate example 1')
    # source = [_ for _ in range(-20, 20, 7)]
    # for steps in [1, 2, 0, -1, -2, 28, -100]:
    #     lst = CircularList(source)
    #     lst.rotate(steps)
    #     print(lst, steps)
    #
    # print('\n# rotate example 2')
    # lst = CircularList([10, 20, 30, 40])
    # for j in range(-1, 2, 2):
    #     for _ in range(3):
    #         lst.rotate(j)
    #         print(lst)
    #
    # print('\n# rotate example 3')
    # lst = CircularList()
    # lst.rotate(10)
    # print(lst)

    print('\n# remove_duplicates example 1')
    test_cases = (
        [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
        [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
        [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],
        list("abccd"),
        list("005BCDDEEFI")
    )

    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.remove_duplicates()
        print('OUTPUT:', lst)

    # print('\n# odd_even example 1')
    # test_cases = (
    #     [1, 2, 3, 4, 5], list('ABCDE'),
    #     [], [100], [100, 200], [100, 200, 300],
    #     [100, 200, 300, 400],
    #     [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E']
    # )
    #
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print('INPUT :', lst)
    #     lst.odd_even()
    #     print('OUTPUT:', lst)

    # print('\n# add_integer example 1')
    # test_cases = (
    #   ([1, 2, 3], 10456),
    #   ([], 25),
    #   ([2, 0, 9, 0, 7], 108),
    #    ([9, 9, 9], 9_999_999),
    #)
    # for list_content, integer in test_cases:
    #    lst = CircularList(list_content)
    # print('INPUT :', lst, 'INTEGER', integer)
    # lst.add_integer(integer)
    # print('OUTPUT:', lst)
