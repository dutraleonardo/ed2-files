from .hash_table import HashTable
from collections import deque
from terminaltables import AsciiTable



class HashTableWithLinkedList(HashTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _set_value(self, key, data):
        self.values[key] = deque([]) if self.values[key] is None else self.values[key]  
        self.values[key].appendleft(data)
        self._keys[key] = self.values[key]

    def balanced_factor(self):
        return sum([self.charge_factor - len(slot) for slot in self.values if slot is not None])\
               / self.size_table * self.charge_factor
    
    def _colision_resolution(self, key, data=None):

        if not (len(self.values[key]) == self.charge_factor
                and self.values.count(None) == 0):
            return key
        return super()._colision_resolution(key, data)

    def _decompose_linked_list(self):
        table = [
            ["bucket", "linked_list_values"]
            ]
        for key, linked_list in sorted(self._keys.items(), key=lambda tup: tup[0]):
            line = [key]
            if linked_list is not None:
                line.append(self.set_line(linked_list)[:-2])
            table.append(line)
        return table

    def set_line(self, list):
        st = ""
        for item in list:
                st += str(item) + "=>"
        return st

    def _mount_table(self):
        table = self._decompose_linked_list()
        return AsciiTable(table).table

