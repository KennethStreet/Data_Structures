# Course: CS261 - Data Structures
# Student Name: Kenneth Street
# Assignment: Project 2 - Your Very Own Dynamic Array
# Description: Bag data structure and it's methods

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        :param -- value
        :returns -- None
        :description -- Adds a new value to the Bag
        """
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        :param -- value
        :returns -- bool
        :description -- Removes the value from the Bag. Returns True if removal took place, otherwise False
        """
        removal = False
        index = None

        for bag_item in range(self.da.length()):
            if self.da.__getitem__(bag_item) == value:
                index = bag_item
                break

        if index is not None:
            self.da.remove_at_index(index)
            removal = True

        return removal

    def count(self, value: object) -> int:
        """
        :param -- value
        :returns -- int
        :description -- Returns a count of the number of items in the Bag that match the passed value
        """
        bag_count = 0
        for bag_item in range(self.da.length()):
            if self.da.__getitem__(bag_item) == value:
                bag_count += 1

        return bag_count

    def clear(self) -> None:
        """
        :param -- None
        :returns -- None
        :description -- Clears the contents of the Bag
        """
        self.da = DynamicArray()

    def equal(self, second_bag: object) -> bool:
        """
        :param -- second_bag
        :returns -- bool
        :description -- Compares the Bag object passed as a parameter to the current Bag object.
        If they equal each other, regardless of order, it returns True; otherwise False
        """
        # Begin edge case handling
        if second_bag.da.is_empty() and self.da.is_empty():
            return True

        if second_bag.size() != self.size():
            return False

        # Begin copying elements into new Bag as we don't want to make changes to existing arrays
        uncounted_items = []

        for item in range(second_bag.size()):
            uncounted_items.append(second_bag.da.__getitem__(item))

        uncounted_bag = Bag(uncounted_items)

        # Begin checking if the Bags equal each other by using the equal_count variable
        equal_count = 0
        for bag_item in range(self.size()):
            for second_bag_item in range(uncounted_bag.size()):
                if self.da.__getitem__(bag_item).__eq__(uncounted_bag.da.__getitem__(second_bag_item)):
                    # Increase variable count as Bag elements equal each other
                    # Remove so we don't double count
                    # If item found then break out of inner for loop
                    equal_count += 1
                    uncounted_bag.remove(uncounted_bag.da.__getitem__(second_bag_item))
                    break

        if equal_count == second_bag.size():
            return True
        else:
            return False


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)


    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)


    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))


    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)


    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
