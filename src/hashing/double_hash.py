#!/usr/bin/env python3

from .hash_table import HashTable
from number_theory.prime_numbers import next_prime


class DoubleHash(HashTable):
    """
        Hash Table example with open addressing and Double Hash
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __hash_function_2(self, value):
        print("key: {0}".format(value))
        next_prime_gt = next_prime(value % self.size_table) #gt = bigger than
        print("next_prime_after")
        print(next_prime_gt)
        return next_prime_gt - (value % next_prime_gt)

    def hash_function(self, value, factor=1):
        return factor * self.__hash_function_2(value) % self.size_table

    def colision_resolution(self, key):
        i = 1
        new_key = self.hash_function(key, i)

        while self.values[new_key] is not None \
                and self.values[new_key] != key:

            if self.balanced_factor() >= self.lim_charge:
                new_key = None
                break

            else:
                i += 1
                new_key = self.hash_function(key, i)


        return new_key