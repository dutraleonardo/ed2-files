#!/usr/bin/env python3
from number_theory.prime_numbers import next_prime
from terminaltables import AsciiTable

class HashTable:
    """
        Basic Hash Table example with open addressing and linear probing.
        This class works as father of other hash table variations
    """

    def __init__(self, size_table, charge_factor=None, lim_charge=None):
        """

        :param size_table: recommended a prime number
        :param charge_factor: define the charge per slot
        :param lim_charge: define when rehashing must be done
        """
        self.size_table = size_table
        self.values = [None] * self.size_table #the hash table start with empty slots
        self.lim_charge = 0.75 if lim_charge is None else lim_charge
        self.charge_factor = 1 if charge_factor is None else charge_factor
        self.__aux_list = []
        self._keys = {} # the result of hash_function operation



    def keys(self):
        return self._keys

    def balanced_factor(self):
        return sum([1 for slot in self.values
                    if slot is not None]) / (self.size_table * self.charge_factor)

    def hash_function(self, key):
        """
        :param key: value of slot
        :return: a key that represent the position of key-value in array
        """
        return key % self.size_table

    def mount_table(self):
        table = [
            [index for index in range(len(self.values))],
            [value for value in self.values]
        ]
        return AsciiTable(table).table

    def _step_by_step(self, step_ord, data_insert_tuple):

        # print(data_insert_tuple)
        print("step {0}".format(step_ord))
        if data_insert_tuple is not None:
            if len(data_insert_tuple) == 2:
                key, data = data_insert_tuple
                print("{0} mod {1} = {2}".format(data, self.size_table, key))
            elif len(data_insert_tuple) > 2:
                # print(data_insert_tuple)
                data, colision_list_items, new_key = data_insert_tuple
                if len(colision_list_items) > 0:
                    [print("colision: {0} mod {1} = {2}".format(data + index, self.size_table, item)) for index, item
                     in enumerate(colision_list_items)]
                    print("{0} insert in bucket {1}".format(data, new_key))
            else:
                print("Rehashing")

        else:
            print()
        print(self.mount_table())

    def bulk_insert(self, values):
        i = 1
        self.__aux_list = values
        for value in values:
            # self.insert_data(value)
            self._step_by_step(i, self.insert_data(value))
            i += 1

    def _set_value(self, key, data):
        self.values[key] = data
        self._keys[key] = data

    def _colision_resolution(self, key, data=None):

        colision_resolution_items = []
        colision_resolution_items.append(key)
        new_key = self.hash_function(key + 1)

        while self.values[new_key] is not None \
                and self.values[new_key] != key:

            if self.values.count(None) > 0:
                colision_resolution_items.append(new_key)
                new_key = self.hash_function(new_key + 1)
            else:
                new_key = None
                break

        return colision_resolution_items, new_key

    def rehashing(self):
        survivor_values = [value for value in self.values if value is not None]
        self.size_table = next_prime(self.size_table, factor=2)
        self._keys.clear()
        self.values = [None] * self.size_table #hell's pointers D: don't DRY ;/
        map(self.insert_data, survivor_values)

    def insert_data(self, data):
        key = self.hash_function(data)

        if self.values[key] is None:
            self._set_value(key, data)
            return key, data

        elif self.values[key] == data:
            pass

        else:
            colision_list_items, new_key = self._colision_resolution(key, data)
            if new_key is not None:
                self._set_value(new_key, data)
                return data, colision_list_items, new_key
            else:
                self.rehashing()
                print("rehashing {0}".format(self.size_table))
                self.insert_data(data)




