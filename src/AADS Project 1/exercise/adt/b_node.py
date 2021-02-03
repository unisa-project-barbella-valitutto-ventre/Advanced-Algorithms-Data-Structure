from exercise.adt.BtreeSortMap import BtreeSortMap


class BTreeNode:
    __slots__ = '_children', '_map'

    def __init__(self, parent=None):
        self._map = BtreeSortMap()
        self._children = []

    def __lt__(self, other):
        max = self.get_map().find_max()
        other_max = other.get_map().find_max()
        return max < other_max

    def __len__(self):
        return len(self._map)

    def get_map(self):
        return self._map

    def get_children(self):
        return self._children

    def set_child(self, node):
        self._children.append(node)
        self._children.sort()

    def insert_element(self, key, value):
        self._map.__setitem__(key, value)

    def delete_element(self, key):
        self._map.__delitem__(key)

    def get_element(self, key):
        return self._map.__getitem__(key)

    def pop_child(self, index):
        self._children.pop(index)

    def get_index(self, key):
        return self._map.get_index(key)

    def set_at_index(self, index, value):
        self._map.set_at_index(index, value)

    def get_at_index(self, index):
        return self._map.get_at_index(index)

    def list_keys(self):
        return list(self._map.keys())

    def print_branch(self, indexofchild):
        print("Parent", indexofchild, self.list_keys())
        for i in range(len(self._children)):
            print("     Children: ", i, list(self._children[i].get_map().keys()))
