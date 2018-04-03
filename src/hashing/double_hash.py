#!/usr/bin/env python3

from .hash_table import HashTable
from number_theory.prime_numbers import next_prime, check_prime


class DoubleHash(HashTable):
    """
        Hash Table example with open addressing and Double Hash
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __hash_function_2(self, value, data):

        next_prime_gt = next_prime(value % self.size_table) \
            if not check_prime(value % self.size_table) else value % self.size_table  #gt = bigger than
        return next_prime_gt - (data % next_prime_gt)

    def __hash_double_function(self, key, data, increment):
        return (increment * self.__hash_function_2(key, data)) % self.size_table

    def _colision_resolution(self, key, data=None):
        i = 1
        colision_resolution_items = []
        colision_resolution_items.append(key)

        new_key = self.hash_function(data)
#                 i += 1

        while self.values[new_key] is not None and self.values[new_key] != key:
            if self.balanced_factor() >= self.lim_charge:
                new_key = None
                break
            else:
                colision_resolution_items.append(new_key)
                new_key = (i * self.__hash_function_2(key, data)) % self.size_table
                i += 1
        return colision_resolution_items, new_key
