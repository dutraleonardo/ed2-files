#!/usr/bin/env python3
from number_theory.prime_numbers import next_prime


class HashTable:
    """
        Basic Hash Table example with open addressing and linear probing
    """

    def __init__(self, size_table, charge_factor=None, lim_charge=None):
        self.size_table = size_table
        self.values = [None] * self.size_table
        self.lim_charge = 0.75 if lim_charge is None else lim_charge
        self.charge_factor = 1 if charge_factor is None else charge_factor
        self.__aux_list = []
        self.__keys = {}

    def keys(self):
        return self.__keys

    def balanced_factor(self):
        return sum([1 for slot in self.values
                    if slot is not None]) / (self.size_table * self.charge_factor)

    def hash_function(self, key):
        return key % self.size_table

    def __step_by_step(self, step_ord):

        print("step {0}".format(step_ord))
        print([i for i in range(len(self.values))])
        print(self.values)

    def bulk_insert(self, values):
        i = 1
        self.__aux_list = values
        for value in values:
            self.insert_data(value)
            self.__step_by_step(i)
            i += 1

    def __set_value(self, key, data):
        self.values[key] = data
        self.__keys[key] = data

    def colision_resolution(self, key):
        new_key = self.hash_function(key + 1)

        while self.values[new_key] is not None \
                and self.values[new_key] != key:

            if self.values.count(None) > 0:
                new_key = self.hash_function(new_key + 1)
            else:
                new_key = None
                break

        return new_key

    def rehashing(self):
        survivor_values = [value for value in self.values if value is not None]
        self.size_table = next_prime(self.size_table, factor=2)
        self.__keys.clear()
        self.values = [None] * self.size_table #hell's pointers D: don't DRY ;/
        map(self.insert_data, survivor_values)

    def insert_data(self, data):
        key = self.hash_function(data)

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
                self.insert_data(data)


