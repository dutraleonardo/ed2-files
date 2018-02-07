#!/usr/bin/env python3

from .hash_table import HashTable


class QuadraticProbing(HashTable):
    """
        Basic Hash Table example with open addressing using Quadratic Probing 
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def colision_resolution(self, key):
        i = 1
        new_key = self.hash_function(key + i*i)

        while self.values[new_key] is not None \
                and self.values[new_key] != key:

            if self.balanced_factor() >= self.lim_charge:
                new_key = None
                break

            else:
                i += 1
            new_key = self.hash_function(key + i*i)

        return new_key
