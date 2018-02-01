class HashTable:
    """
        Basic Hash Table example
    """

    def __init__(self, size_table, charge_factor = None):
        self.size_table = size_table
        self.values = [None] * self.size_table
        self.keys = [None] * self.size_table
        self.charge_factor = 1 if charge_factor is None else charge_factor


    @property
    def balanced_factor(self):
        return sum([slot for slot in self.values
                    if slot is not None]) / (self.size_table * self.charge_factor)

    def __hash_function(self, key):
        return key % self.size_table

    def __check_prime(self, number):
        return all([number % i for i in range(2, number)])

    # def __step_by_step(self, step_num):
    #     print("step %s".format(step_num))
    #

    def double_next_prime(self):
        i = 2
        value = 2 * self.size_table

        while not self.__check_prime(value + i):
            value += i

        return value

    def __set_value(self, key, data):
        self.values[key] = data
        self.keys[key] = key

    def colision_resolution(self, key):
        new_key = self.__hash_function(key + 1)

        while self.values[new_key] is not None \
                and self.values[new_key] != key:
            new_key += 1

        return new_key

    def insert_data(self, data):
        key = self.__hash_function(data)

        if self.values[key] is None:
            self.__set_value(key, data)

        elif self.values[key] == data:
            pass

        else:
            self.__set_value(self.colision_resolution(key), data)

    def rehashing(self):
        survivor_values = self.values
        self.size_table = self.double_next_prime()
        self.keys = self.values = [None] * self.size_table
        map(self.insert_data, survivor_values)
