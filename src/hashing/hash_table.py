class HashTable:
    """
        Basic Hash Table example with open addressing and linear probing
    """

    def __init__(self, size_table, charge_factor=None):
        self.size_table = size_table
        self.values = [None] * self.size_table
        self.keys = [None] * self.size_table
        self.charge_factor = 1 if charge_factor is None else charge_factor

    def balanced_factor(self):
        return sum([1 for slot in self.values
                    if slot is not None]) / (self.size_table * self.charge_factor)

    def __hash_function(self, key):
        return key % self.size_table

    def __check_prime(self, number):
        """
            it's not the best solution
        """
        return all([number % i for i in range(2, number)])

    def __step_by_step(self, step_ord):

        print("step {0}".format(step_ord))
        print([i for i in range(len(self.values))])
        print(self.values)

    def bulk_insert(self, values):
        i = 1
        for value in values:
            self.insert_data(value)
            self.__step_by_step(i)
            i += 1

    def double_next_prime(self):
        i = 1
        value = 2 * self.size_table

        while not self.__check_prime(value):
            value += i

        return value

    def __set_value(self, key, data):
        self.values[key] = data
        self.keys[key] = key

    def colision_resolution(self, key):
        new_key = self.__hash_function(key + 1)

        while self.values[new_key] is not None \
                and self.values[new_key] != key:

            if self.values.count(None) > 0:
                new_key += 1
            else:
                new_key = None
                break
        return new_key

    def rehashing(self):
        survivor_values = [value for value in self.values if value is not None]
        print(survivor_values)
        self.size_table = self.double_next_prime()
        self.keys = [None] * self.size_table
        self.values = [None]*self.size_table #hell's pointers D: don't DRY ;/
        list(map(self.insert_data, survivor_values))

    def insert_data(self, data):
        key = self.__hash_function(data)

        if self.values[key] is None:
            self.__set_value(key, data)

        elif self.values[key] == data:
            pass

        else:
            colision_resolution = self.colision_resolution(key)
            if colision_resolution is not None:
                self.__set_value(colision_resolution, data)
            else:
                self.rehashing()
    


