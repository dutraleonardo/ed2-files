#!/usr/bin/env python3

from .hash_table import HashTable
from .number_theory.prime_numbers import next_prime, check_prime


class DoubleHash(HashTable):
    """
        Hash Table example with open addressing and Double Hash
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __r(self, data):
        next_prime_gt = next_prime(len(self.values) // 2)
        return next_prime_gt - (data % next_prime_gt)

    def __hash_double_function(self, key, data, increment):
        return (increment * self.__r(data)) % self.size_table

    def _colision_presentation(self, **kwargs):
        return 'colision: ({i}*{r}) mod {size_table} = {new_key}'.format(**kwargs)#i, r, self.size_table, new_key)

    def _colision_resolution(self, key, data=None ):
        i = 1
        print('colision: {0} mod {1} = {2}'.format(data, len(self.values), key))
        new_key = self.hash_function(data)
<<<<<<< HEAD
# <<<<<<< HEAD

#         while self.values[new_key] is not None and self.values[new_key] != key:
#             new_key = self.__hash_double_function(key, data, i) if \
#                 self.balanced_factor() >= self.lim_charge else None
#             if new_key is None:
#                 break
#             else:
#                 i += 1
# =======
        while self.values[new_key] is not None \
                 and self.values[new_key] != key:
=======
        r = self.__r(data)
        
        while self.values[new_key] is not None and self.values[new_key] != key:
>>>>>>> corrections in presentation
            if self.balanced_factor() >= self.lim_charge:
                new_key = None
                break
            
            else:
                if (i == 1):
<<<<<<< HEAD
                    print("second hash= {0}".format(hd))
                print('colision: ({0}*{1}) mod {2} = {3}'.format(i, hd, self.size_table, new_key))
                new_key = (i * hd) % self.size_table
                i += 1
<<<<<<< HEAD
# <<<<<<< HEAD
# <<<<<<< HEAD
        # while self.values[new_key] is not None and self.values[new_key] != key:
        #     new_key = self.__hash_double_function(key, data, i) if \
        #         self.balanced_factor() >= self.lim_charge else None
        #     if new_key is None: break
        #     else: i += 1
# >>>>>>> alternative double changed to initial code

        return new_key
# =======
        # return colision_resolution_items, new_key
# >>>>>>> double hash partially refactored to presentation
# =======
# =======
        print("{0} insert in bucket {1}".format(data, new_key))
# >>>>>>> presentation double hash finished
        return colision_resolution_items, new_key

    # def _str_hash_function(self, data, key):
    #     return "f({0}) = "
    def _step_by_step(self, step_ord, data_insert_tuple):
        if len(data_insert_tuple) == 2:
            key, data = data_insert_tuple
            print("{0} insert in bucket {1}".format(data, key))
        print(self._mount_table())
# >>>>>>> open hashing with linked list presentation finished
# =======
                    print("r = {0}".format(r))
                new_key = self.__hash_double_function(new_key, data, i)
                if self.values[new_key] is not None and self.values[new_key] != key:
                    print(self._colision_presentation(
                            i=i, r=r, size_table=self.size_table, new_key=new_key))
                i += 1  
                
        print("{0} insert in bucket {1}".format(data, new_key))
        return new_key
# >>>>>>> corrections in presentation
