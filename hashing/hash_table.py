class HashTable:
    """
        Basic Hash Table example
    """

    def __init__(self, size_table, *args, **kwargs):
        self.size_table = size_table
        self.values = [None] * self.size_table
        self.keys = [None] * self.size_table
        self.charge_factor = 1

    @property
    def balanced_factor(self):
        return sum([slot for slot in self.values if slot is not None]) / (self.size_table *
                                                                          self.charge_factor)

    def __hash_function(self, key):
        return key % self.size_table

    def is_prime(self, number):
        return all([number % i for i in range(2, number)])

    def double_next_prime(self):
        i = 2
        value = 2 * self.size_table

        while not self.is_prime(value + i):
            value += i

        return value

    def __set_value(self, key, data):
        self.values[key] = data
        self.keys[key] = key

    def insert_key(self, data):
        key = self.__hash_function(data)

        if self.values[key] is None:
            self.__set_value(key, data)

        elif self.values[key] == data:
            pass

        else:
            new_key = self.__hash_function(key + 1)

            while self.values[new_key] is not None and self.values[new_key] != key:
                new_key += 1

            self.__set_value(new_key, data)

    def rehashing(self):
        aux = self.values
        self.size_table = self.double_next_prime()
        self.values = [None] * self.size_table
        self.keys = self.values
        [self.insert_key(value) for value in self.values]