# Course: CS261 - Data Structures
# Student Name: Kenneth Street
# Assignment: Project 2 - Your Very Own Dynamic Array
# Description: Dynamic Array data structure and it's methods

from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.first = 0  # do not use / change this value
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        self.data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        :param -- new_capacity
        :returns -- None
        :description -- Increases the size of the array to the integer that is passed and copies everything from the
        old array into the new larger array.
        """
        # Error handling
        if new_capacity <= 0 or new_capacity < self.length():
            return

        # Copy everything from old array into new larger array
        new_array = StaticArray(new_capacity)

        for i in range(self.length()):
            new_array.__setitem__(i, self.__getitem__(i))

        # Begin updating fields
        self.size = self.length()
        self.capacity = new_capacity
        self.data = new_array

    def append(self, value: object) -> None:
        """
        :param -- value
        :return -- None
        :description -- Adds value to array, if the array is full then size is doubled and proceeds to add value
        """
        # Check if array still has capacity, if not then double
        if self.length() == self.capacity:
            self.resize(self.capacity * 2)

        self.data[self.length()] = value
        self.size = self.length() + 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        :param -- index, value
        :returns -- None
        :description -- Inserts value at specified index, then shifts everything. Resize the array if needed.
        """
        # Begin with error handling
        if index < 0 or self.capacity < index:
            raise DynamicArrayException

        # Check if list needs to be resized
        if self.length() == self.capacity:
            self.resize(self.length() * 2)

        insert_array = StaticArray(self.length() + 1)

        for current_index in range(insert_array.size()):
            if current_index == index:
                self.size += 1
                insert_array.__setitem__(current_index, value)
            else:
                if current_index <= index:
                    set_index = current_index
                else:
                    set_index = current_index - 1
                insert_array.__setitem__(current_index, self.__getitem__(set_index))

        self.data = insert_array

    def remove_at_index(self, index: int) -> None:
        """
        :param -- index
        :returns -- None
        :description -- Removes an element at the index position that is passed. If the array is 1/4 capacity then will
        reduce the size of the array.
        """
        # Begin error handling
        if index < 0 or self.length() <= index:
            raise DynamicArrayException

        if self.length() == 1 and index == 0:
            self.size -= 1
            self.data = []
            return

        if int(self.size * 4) < self.capacity and self.capacity > 10:
            self.capacity = int(self.size * 2)
            if self.capacity < 10:
                self.capacity = 10

        removal_array = StaticArray(self.length() - 1)

        for current_index in range(self.length()):
            if current_index == index:
                pass
            else:
                if current_index <= index:
                    set_index = current_index
                else:
                    set_index = current_index - 1
                removal_array.__setitem__(set_index, self.__getitem__(current_index))

        self.data = removal_array
        self.size -= 1

    def slice(self, start_index: int, size: int) -> object:
        """
        :param -- start_index, size
        :returns -- Dynamic Array Object
        :description -- Returns a new Dynamic Array object with a subset starting at the start_index and ending at size
        """
        # Begin error handling
        if start_index < 0 or self.length() < size or size < 0 or start_index == self.length():
            raise DynamicArrayException

        # Begin building subset
        starting_index = 0
        slice_array = []
        for current_index in range(start_index, abs(size + start_index), 1):
            slice_array.append(self.__getitem__(current_index))
            starting_index += 1

        dynamic_array = DynamicArray(slice_array)
        return dynamic_array

    def merge(self, second_da: object) -> None:
        """
        :param -- second_da
        :returns -- None
        :description -- Appends everything passed in via second_da to current dynamic array in order
        """
        for element in range(second_da.length()):
            self.append(second_da.__getitem__(element))

    def map(self, map_func) -> object:
        """
        :param -- map_func
        :returns -- Dynamic Array Object
        :description -- Creates new Dynamic Array Object by deriving each element from applying a map function to each
        element in the original array
        """
        derived_array = []

        for element in range(self.length()):
            derived_array.append(map_func(self.__getitem__(element)))

        dynamic_array = DynamicArray(derived_array)
        return dynamic_array

    def filter(self, filter_func) -> object:
        """
        :param -- filter_func
        :returns -- Dynamic Array Object
        :description -- Creates a new Dynamic Array Object by filtering the current list into a subset
        """
        filter_array = []

        for element in range(self.length()):
            if filter_func(self.__getitem__(element)):
                filter_array.append(self.__getitem__(element))

        dynamic_array = DynamicArray(filter_array)
        return dynamic_array

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        :param -- reduce_func, initializer=None
        :returns -- Dynamic Array Object
        :description -- Applies the reduce_func to every element in the existing dynamic array
        and returns the new subset
        """

        if self.length() == 0:
            if initializer is None:
                return None
            else:
                return initializer

        if self.length() == 1:
            if initializer is None:
                return self.__getitem__(0)
            else:
                return reduce_func(initializer, self.__getitem__(0))

        if initializer is None:
            for element in range(self.length() - 1):
                if element == 0:
                    sum = reduce_func(self.__getitem__(element), self.__getitem__(element + 1))
                else:
                    sum = reduce_func(sum, self.__getitem__(element + 1))
        else:
            for element in range(self.length()):
                if element == 0:
                    sum = reduce_func(initializer, self.__getitem__(element))
                else:
                    sum = reduce_func(sum, self.__getitem__(element))
        return sum


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)


    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)


    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)


    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)


    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)


    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)


    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)


    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)


    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)


    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)


    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")


    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")


    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)


    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)


    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))


    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))


    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))


    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))