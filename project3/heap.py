"""To create this project we used Lecture 20 slides of CSE 331 Spring 2018 as a template"""


class Heap(object):  # base class defines _Item
    """A max-oriented priority queue implemented with a binary heap."""

    # ------------------------------ nested _Item class ------------------------------
    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value', '_time'

        def __init__(self, k, v):
            self._key = k
            self._value = v
            self._time = 0

        def __gt__(self, other):
            if self._key == other._key:
                return self._time > other._time
            return self._key > other._key  # compare items based on their keys

        def __repr__(self):
            return '({0},{1},{2})'.format(self._key, self._value, self._time)

    # ------------------------------ nonpublic behaviors ------------------------------

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)  # index beyond end of list?

    def _has_right(self, j):
        return self._right(j) < len(self._data)  # index beyond end of list?

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] > self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)  # recur at position of parent

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            large_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] > self._data[left]:
                    large_child = right
            if self._data[large_child] > self._data[j]:
                self._swap(j, large_child)
                self._downheap(large_child)  # recur at position of large child

    # ------------------------------ public behaviors ------------------------------
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = []
        self._landed = 0
        self._average_time = 0

    def __str__(self):
        result = ""
        for item in self._data:
            result += str(item)+", "
        return f"[{result[:-2]}]"

    def __repr__(self): return self.__str__()


    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)  # upheap newly added position
        # self._sum_time+=

    def max(self):
        """Return but do not remove (k,v) tuple with maximum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            return
        item = self._data[0]
        return (item._key, item._value)

    def remove_max(self):
        """Remove and return (k,v) tuple with maximum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            return
        self._swap(0, len(self._data) - 1)  # put minimum item at the end
        item = self._data.pop()  # and remove it from the list;
        self._downheap(0)  # then fix new root

        self.increase_time()
        self._landed += 1
        if self._landed ==5:
            self.increase_priotity()
            self._landed = 0
        return (item._key, item._value)

    def increase_time(self):
        """
        Increases the time attribute value of every plane in the heap
        :return: None
        """
        if self.is_empty():
            return

        sum_time = 0
        for i in self._data:
            i._time += 1
            sum_time += i._time
        self.average_time = sum_time/len(self._data)

        return

    def increase_priotity(self, ):
        """
        Increases the priority of every plane in the heap that has been waiting for longer
        than the average amount of time of the total planes in the heap
        :return: None
        """
        for j, i in enumerate(self._data):
            if i._time > self.average_time:
                i._key += self._data[0]._key//2
                self._upheap(j)
