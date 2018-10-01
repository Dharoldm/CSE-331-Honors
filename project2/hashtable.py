class Node:

    def __init__(self, key, value):
        """
        initialization of a node
        :param key: key of the node
        :param value: value stored in the node
        :return: nothing
        """
        self._key = key
        self._value = value

    def __str__(self):
        """
        Defines string represntation of the node
        :return: string represetation of the hash table
        """
        return f"{self._key}:{self._value}"

    def val(self):
        """
        Returns the value of the node
        :return: the value of the node
        """
        return self._value

    def key(self):
        """
        Returns the value of the node
        :return: the key of the node
        """
        return self._key


class HashTable:

    def __init__(self, capacity=11):
        """
        initialization of an empty hash table
        :return: nothing
        """
        self._capacity = capacity
        self._size = 0
        self._data = [[] for i in range(capacity)]

    def __repr__(self):
        """
        Defines string represntation of the hash table
        :return: string represetation of the hash table
        """
        disp = ""
        for bucket in self._data:
            disp += "[ " + ', '.join([str(item) for item in bucket]) + " ], "
        return "Size: " + str(self._size) + " Capacity: " + str(self._capacity) + '\n{ ' + disp[:-2] + ' }'

    def __str__(self):
        """
        Calls __repr to create the string representation of the hash table
        :return: string representation of the hash table
        """
        return self.__repr__()

    def __setitem__(self, key, value):
        """
        Calls setitem
        :return: None
        """
        self.setitem(key, value)

    def __getitem__(self, key):
        """
        Calls get
        :return: None
        """
        return self.get(key)

    def __delitem__(self, key):
        """
        Calls delete
        :return: None
        """
        self.delete(key)

    def __len__(self):
        """
        Returns the size of the hash table
        :return: The number of nodes in the hash table
        """
        return self._size

    def __iter__(self):
        """
        Iterates through the hash table
        :return: None
        """
        for bucket in self._data:
            for item in bucket:
                yield item

    def setitem(self, key, value):
        """
        Adds a node to the hash table given the key and value, if the lambda of the hash table is greater
        than 2/3 then calls the grow function before adding the function.
        :param item: The node being added to the table
        :return: None
        """
        if (self._size/self._capacity) >= (2 / 3):
            self.grow()
        index = hash(key) % self._capacity
        self._data[index].append(value)
        self._size += 1

    def get(self, key):
        """
        Searches the hash table for the given key
        :param key: The key being searched for
        :return: The node of the key being searched for or None
        """
        index = hash(key) % self._capacity
        bucket = self._data[index]

        for item in reversed(bucket):
            if item.key() == key:
                return item
        return None

    def delete(self, key):
        """
        Deletes the item with the given key in the hash table
        :param key: The key of the item to be deleted
        :return:
        """
        index = hash(key) % self._capacity
        for i, item in enumerate(reversed(self._data[index])):
            if item.key() == key:
                del self._data[index][-i-1]
                self._size -= 1

    def grow(self):
        """
        Grows the hash table by twice the current capacity
        :return: None
        """
        temp = self._data
        self._size = 0
        self._capacity *= 2
        self._data = [[] for i in range(self._capacity)]

        for bucket in temp:
            for item in bucket:
                self.setitem(item.key(), item)

    def capacity(self):
        """
        Returns the capacity of the hash table
        :return: The capacity if the hash table
        """
        return self._capacity
