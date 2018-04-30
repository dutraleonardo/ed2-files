from avl_tree.avl_weiss import AVL as AvlTree
from .quadratic_probing import QuadraticProbing

class HMA(QuadraticProbing):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _set_value(self, key, data):
        self.values[key] = AvlTree() if self.values[key] is None else self.values[key]
        self.values[key].insert(data)
        self._keys[key] = self.values[key].nodes
    
    